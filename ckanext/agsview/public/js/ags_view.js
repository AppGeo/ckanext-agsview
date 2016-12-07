// geojson preview module
ckan.module('agsview', function (jQuery, _) {
  console.log(jQuery.jquery);
  return {
    options: {
      table: '<div class="table-container"><table class="table table-striped table-bordered table-condensed"><tbody>{body}</tbody></table></div>',
      row:'<tr><th>{key}</th><td>{value}</td></tr>',
      style: {
        opacity: 0.7,
        fillOpacity: 0.1,
        weight: 2
      },
      i18n: {
        'error': _('An error occurred: %(text)s %(error)s')
      }
    },
    projs: {},
    cache: {},
    initialize: function () {
      var self = this;

      self.el.empty();
      self.el.append($("<div></div>").attr("id","map"));
      self.map = ckan.commonLeafletMap('map', this.options.map_config);

      // hack to make leaflet use a particular location to look for images
      L.Icon.Default.imagePath = this.options.site_url + 'img/leaflet';
      var path = this.options.path;
      if (path.match(/\/(?:MapServer|FeatureServer)\/\d{1,3}\/?$/)) {
          this.loadJson(path);
      } else if (path.match(/\/MapServer$/)) {
        this.loadDynamic(path);
      }
    },
    loadJson: function (path) {
      var self = this;
      this.layer =  L.esri.featureLayer({
          url: path
      })
      this.layer.addTo(map);
      this.getMetaData();
    },
    isTiled: function(metadata) {
      return metadata.singleFusedMapCache
        && metadata.tileInfo
        && metadata.tileInfo.spatialReference
        && metadata.tileInfo.spatialReference.wkid === 102100;
    },
    getInfo: function (path) {
      if (this.cache[path]) {
        return Promise.resolve(this.cache[path]);
      }
      var self = this;
      return Promise.resolve(jQuery.ajax({
        url: path,
        dataType: 'jsonp',
        data: {
          f: 'json'
        }
      }).done(function (d) {
        this.cache[path] = d;
      }));
    },
    loadDynamic: function (path) {
      var self = this;
      this.getInfo(path).then(function (metadata) {
        if (self.isTiled(metadata)) {
          self.layer =  L.esri.tiledMapLayer({
              url: path
          });
        } else {
          self.layer =  L.esri.dynamicMapLayer({
              url: path
          });
        }
        self.layer.addTo(map);
        var extent = metadata.extent || metadata.initialExtent || metadata.fullExtent;
        var wkid = extent.spatialReference.latestWkid;
        return self.getProj(wkid).then(function (d) {
          var prj = proj4(d);
          var bl = prj.inverse([extent.xmin, extent.ymin]);
          var tr = prj.inverse([extent.xmax, extent.ymax]);
          self.map.fitBounds([bl.reverse(), tr.reverse()]);
        });
      });
    },
    getProj: function(wkid) {
      var self = this;
      if (!this.projs[wkid] && proj4.defs('EPSG:' + wkid)) {
        this.projs[wkid] = proj4.defs('EPSG:' + wkid);
      }
      if (this.projs[wkid]) {
        return Promise.resolve(this.projs[wkid]);
      }
      var url = 'http://epsg.io/' + wkid + '.proj4';

      return Promise.resolve(jQuery.ajax(url).done(function (d) {
        self.projs[wkid] = d;
        return d;
      }));
    },
    showError: function (jqXHR, textStatus, errorThrown) {
      if (textStatus == 'error' && jqXHR.responseText.length) {
        this.el.html(jqXHR.responseText);
      } else {
        this.el.html(this.i18n('error', {text: textStatus, error: errorThrown}));
      }
    },
    showPreview: function (geojsonFeature) {
      var self = this;
      var gjLayer = L.geoJson(geojsonFeature, {
        style: self.options.style,
        onEachFeature: function(feature, layer) {
          var body = '';
          if (feature.properties) {
            Object.keys(feature.properties).forEach(function(key){
              var value = feature.propertiesp[key];
              if (value != null && typeof value === 'object') {
                value = JSON.stringify(value);
              }
              body += L.Util.template(self.options.row, {key: key, value: value});
            });
            var popupContent = L.Util.template(self.options.table, {body: body});
            layer.bindPopup(popupContent);
          }
        }
      }).addTo(self.map);
      self.map.fitBounds(gjLayer.getBounds());
    }
  };
});

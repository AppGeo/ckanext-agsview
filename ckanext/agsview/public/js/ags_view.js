// geojson preview module
ckan.module('agsview', function (jQuery, _) {
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
      this.layer.metadata(function(error, metadata){
        if (error) {
          throw error;
        }
        self.map.fitBounds(L.esri.Util.extentToBounds(metadata.extent))
        console.log(metadata);
      });
    },
    loadDynamic: function (path) {
      this.layer =  L.esri.dynamicMapLayer({
            url: path,
            opacity: 0.25,
            useCors: false
        });
        this.layer.addTo(map);
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

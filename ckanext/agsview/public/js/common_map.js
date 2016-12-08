(function (ckan, jQuery) {

  /* Returns a Leaflet map to use on the different spatial widgets
   *
   * All Leaflet based maps should use this constructor to provide consistent
   * look and feel and avoid duplication.
   *
   * container               - HTML element or id of the map container
   * mapConfig               - (Optional) CKAN config related to the base map.
   *                           These are defined in the config ini file (eg
   *                           map type, API keys if necessary, etc).
   * leafletMapOptions       - (Optional) Options to pass to the Leaflet Map constructor
   * leafletBaseLayerOptions - (Optional) Options to pass to the Leaflet TileLayer constructor
   *
   * Examples
   *
   *   // Will return a map with attribution control
   *   var map = ckan.commonLeafletMap('map', mapConfig);
   *
   *   // For smaller maps where the attribution is shown outside the map, pass
   *   // the following option:
   *   var map = ckan.commonLeafletMap('map', mapConfig, {attributionControl: false});
   *
   * Returns a Leaflet map object.
   */
  ckan.commonLeafletMap = function (container,
                                    config) {

      var isHttps = window.location.href.substring(0, 5).toLowerCase() === 'https';
      var mapConfig =  {type: 'stamen'};
      if (config.basemap && typeof config.basemap === 'string') {
        mapConfig = {
          type: 'custom',
          url: config.basemap
        }
      }

      var leafletBaseLayerOptions = {
                maxZoom: 18
                }

      map = new L.Map(container, leafletBaseLayerOptions);

      if (mapConfig.type == 'custom') {
          // Custom XYZ layer
          baseLayerUrl = mapConfig.url;
      } else {
          // Default to Stamen base map
          baseLayerUrl = 'https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}.png';
          leafletBaseLayerOptions.subdomains = mapConfig.subdomains || 'abcd';
          leafletBaseLayerOptions.attribution = mapConfig.attribution || 'Map tiles by <a href="http://stamen.com">Stamen Design</a> (<a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>). Data by <a href="http://openstreetmap.org">OpenStreetMap</a> (<a href="http://creativecommons.org/licenses/by-sa/3.0">CC BY SA</a>)';
      }

      var baseLayer = new L.TileLayer(baseLayerUrl, leafletBaseLayerOptions);
      map.addLayer(baseLayer);

      return map;

  }

})(this.ckan, this.jQuery);

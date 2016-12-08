# todo

- [x] split into two classes ags_ms_view / ags_fs_view
- [x] set extent defaults dynamically
- [x] allow for multiple inputs

  - [x] layer (JSON)
  - [x] mapserver tiled
  - [x] mapserver dynamic

- [ ] esri basemap options???

- [ ] set default values in config file (.ini)

  - [ ] ags_url
  - [ ] layer_ids
  - [ ] basemap_url

# setup

## install extension on ckan machine

- activate ckan python environment
- cd into folder with the setup.py file
- run setup.py

  - use install if no development is needed
  - use develop if you are developing files locally (e.g. Updating template file)

```
. /usr/lib/ckan/default/bin/activate
cd ~/git/guidos/ckanext-agsview/
python setup.py install
```

## update config file on ckan machine

- add ags_fs_view and/or ags_ms_view to plugins in the ini file
- add the following config attributes to the ini file

  - ckanext.agsview.default_ags_url
  - ckanext.agsview.default_basemap_url

## reload apache ckan Service

# useful endpoints

- dynamic mapserver: http://gis.cityofboston.gov/arcgis/rest/services/CityServices/OpenData/MapServer
- tiled mapserver: http://gis.cityofboston.gov/arcgis/rest/services/Basemaps/base_map_webmercatorV2/MapServer
- layer: http://gis.cityofboston.gov/arcgis/rest/services/CityServices/OpenData/MapServer/0

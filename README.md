# todo

- [x] split into two classes ags_ms_view / ags_fs_view
- [x] set extent defaults dynamically
- [x] allow for multiple inputs

  - [x] layer (JSON)
  - [x] mapserver tiled
  - [x] mapserver dynamic

- [ ] esri basemap options???

- [ ] make default basemap configurable (.ini)

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
- add ckanext.agsview.default_basemap_url parameter to the config file in the plugin section

```
sed -i.bak -e "s/ckan.plugins = /ckan.plugins = ags_fs_view ags_ms_view /g" /etc/ckan/default/production.ini
sed -i.bak '/^ckan.plugins/a ckanext.ags_view_default_basemap_url = Gray' /etc/ckan/default/production.ini
```

## reload apache ckan Service

```
sudo service apache2 reload
```

# useful endpoints

- dynamic mapserver: <http://gis.cityofboston.gov/arcgis/rest/services/CityServices/OpenData/MapServer>
- tiled mapserver: <http://gis.cityofboston.gov/arcgis/rest/services/Basemaps/base_map_webmercatorV2/MapServer>
- layer: <http://gis.cityofboston.gov/arcgis/rest/services/CityServices/OpenData/MapServer/0>

# setup for development

```
. /usr/lib/ckan/default/bin/activate
pip install --upgrade pip
cd ~/git/guidos/ckanext-geoview/
python setup.py develop

```

# add geojson_view

```
sed -i.bak -e "s/ckan.plugins = stats text_view image_view recline_view datastore/ckan.plugins = stats text_view image_view recline_view datastore ags_view/g" /etc/ckan/default/production.ini
sed -i.bak -e "s/ckan.views.default_views = image_view text_view recline_view/ckan.views.default_views = image_view text_view recline_view ags_view/g" /etc/ckan/default/production.ini
sudo service apache2 reload

```

# get json query in spatial ref from ags_view

```
http://gis.cityofboston.gov/arcgis/rest/services/Planning/OpenData/MapServer/0/query?where=0=0&Fields=*&returnGeometry=true&returnIdsOnly=false&f=json&outSR=3857&geometryType=esriGeometryEnvelope&groupByFieldsForStatistics=

&geometryType=esriGeometryEnvelope
&returnGeometry=true
&returnIdsOnly=false
&returnCountOnly=false
&groupByFieldsForStatistics=sub_region
&outStatistics=[{"statisticType":"sum","onStatisticField":"pop2007","outStatisticFieldName":"Population_2007"},{"statisticType":"avg","onStatisticField":"AVE_FAM_SZ","outStatisticFieldName":"Average_Family_Size"}]
&f=pjson
```

# potential configuration

[] split into two classes ags_ms_view / ags_fs_view
[] set defaults in configuration
    [] extent (x,y,z)
    [] basemap tile set (url)
[] allow for 2 urls
    [] feature class or dynamic map
    [] tile map
[] allow to pass extent values
[] esri basemap options???

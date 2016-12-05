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

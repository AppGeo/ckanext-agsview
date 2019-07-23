======================================================
ckanext-agsview - Esri ArcGIS Server CKAN resources
======================================================

This extension contains view plugins to display ArcGIS Map services (cached,
dynamic) and Feature layer services in CKAN. It uses an `Esri Leaflet Viewer <https://github.com/Esri/esri-leaflet>`_ for display.

-----------------
Available plugins
-----------------

* `ArcGIS Feature Layer Viewer (ags_fs_view)`_
* `ArcGIS MapService Viewer (ags_ms_view)`_


ArcGIS Feature Layer Viewer (ags_fs_view)
-----------------------------------------

The ArcGIS Feature Layer Viewer provides access to different ArcGIS Feature Layers within a MapService or FeatureService. Each instance of a view has the following configuration options:

* `ags_url`: ArcGIS Server layer end point with layer id included::

    http://gis.cityofboston.gov/arcgis/rest/services/CityServices/OpenData/MapServer/0

* `basemap_url`: Can accept `Esri basemap name <http://esri.github.io/esri-leaflet/api-reference/layers/basemap-layer.html>`_ or generic tile url template::

    Gray

  ::

    http://gis.cityofboston.gov/arcgis/rest/services/Basemaps/base_map_webmercatorV2/MapServer/tile/{z}/{x}/{y}

ArcGIS MapService Viewer (ags_ms_view)
--------------------------------------

The ArcGIS MapServer Viewer provides access to MapService and the ability to set which layers are to view within that MapService. Each instance of a view has the following configuration options:

* `ags_url`: ArcGIS Server MapService end point::

    http://gis.cityofboston.gov/arcgis/rest/services/CityServices/OpenData/MapServer

* `list_ids`: Comma delimited list of ids to include in the map (an empty list will return all the layers)::

    0,5

* `basemap_url`: Can accept `Esri basemap name <http://esri.github.io/esri-leaflet/api-reference/layers/basemap-layer.html>`_ or generic tile url template::

    Gray

  ::

    http://gis.cityofboston.gov/arcgis/rest/services/Basemaps/base_map_webmercatorV2/MapServer/tile/{z}/{x}/{y}

----------------------------
Configuration Options (.ini)
----------------------------

**ckanext.agsview.default_basemap_url**

Can accept `Esri basemap name <http://esri.github.io/esri-leaflet/api-reference/layers/basemap-layer.html>`_ or generic tile url template::

  ckanext.ags_view_default_basemap_url = Gray

::

  ckanext.ags_view_proxy = '{}'


------------------------
Installation
------------------------

To install ckanext-agsview for development:

1. Clone the source::

    cd /usr/lib/ckan/default/src
    git clone https://github.com/OpenGov-OpenData/ckanext-agsview.git

2. Activate your CKAN virtual environment, for example::

    . /usr/lib/ckan/default/bin/activate

3. Install the ckanext-agsview Python package into your python virtual environment::

    cd ckanext-agsview
    python setup.py install

* When running in a development environment, replace install with develop::

    python setup.py develop

4. Add ``ags_fs_view`` and/or ``ags_ms_view`` to the ``ckan.plugins`` setting in your CKAN config (ini) file (by default the config file is located at ``/etc/ckan/default/production.ini``)::

    ckan.plugins = ... ags_fs_view ags_ms_view

5. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload

Quick development Install
-------------------------

1. Copy the following code into a shell script named **setup-agsview.sh** and update the paths as needed::

    . /usr/lib/ckan/default/bin/activate
    cd ~/projects/ckanext-agsview/
    python setup.py develop
    sed -i.bak -e "s/ckan.plugins = /ckan.plugins = ags_fs_view ags_ms_view /g" /etc/ckan/default/production.ini
    sed -i.bak '/^ckan.plugins/a ckanext.ags_view_default_basemap_url = Gray' /etc/ckan/default/production.ini
    sed -i.bak '/^ckan.plugins/a ckanext.ags_view_proxy = {"http://mapservices.bostonredevelopmentauthority.org":"https://jqnatividad-prod.apigee.net/mapservices-bostonredevelopmentauthority-org","http://maps.cityofboston.gov":"https://jqnatividad-prod.apigee.net/maps.cityofboston.gov"}' /etc/ckan/default/production.ini
    sudo service apache2 reload

3. Run the shell script from the command line::

    sh setup-agsview.sh

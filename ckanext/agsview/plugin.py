# encoding: utf-8
import six
import json
import logging
import ckan.plugins as p
from ckan.common import config
from packaging.version import Version


log = logging.getLogger(__name__)

ignore_empty = p.toolkit.get_validator('ignore_empty')

DEFAULT_AGS_FORMATS = ['ags', 'esri rest', 'arcgis geoservices rest api']


def ags_view_default_basemap_url():
    return config.get('ckanext.ags_view_default_basemap_url', '')

def version_builder(text_version):
    return Version(text_version)


class AGSFSView(p.SingletonPlugin):
    '''This plugin makes views of arcgis FeatureServer services'''

    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IResourceView, inherit=True)
    p.implements(p.ITemplateHelpers, inherit=True)

    # IConfigurer

    def update_config(self, config):
        p.toolkit.add_public_directory(config, 'public')
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_resource('public', 'ckanext-agsview')

    # IResourceView

    def can_view(self, data_dict):
        if 'url' not in data_dict['resource']:
            return False
        format_lower = data_dict['resource'].get('format', '').lower()
        return format_lower in DEFAULT_AGS_FORMATS

    def view_template(self, context, data_dict):
        return 'agsview/ags_fs_view.html'

    def form_template(self, context, data_dict):
        return 'agsview/ags_fs_form.html'

    def info(self):
        return {
            'name': 'ags_fs_view',
            'title': p.toolkit._('ArcGIS FeatureServer Service'),
            'icon': 'compass',
            'schema': {
                'ags_url': [ignore_empty, six.text_type],
                'basemap_url': [ignore_empty, six.text_type]
            },
            'iframed': False,
            'default_title': p.toolkit._('ArcGIS FeatureServer Service')
        }

    # ITemplateHelpers

    def get_helpers(self):
        return {
            'ags_view_default_basemap_url': ags_view_default_basemap_url,
            'version': version_builder
        }


class AGSMSView(p.SingletonPlugin):
    '''This plugin makes views of arcgis MapServer services'''

    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IResourceView, inherit=True)
    p.implements(p.ITemplateHelpers, inherit=True)

    def update_config(self, config):
        p.toolkit.add_public_directory(config, 'public')
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_resource('public', 'ckanext-agsview')

    def info(self):
        return {
            'name': 'ags_ms_view',
            'title': p.toolkit._('ArcGIS MapServer Service'),
            'icon': 'compass',
            'schema': {
                'ags_url': [ignore_empty, six.text_type],
                'basemap_url': [ignore_empty, six.text_type],
                'layer_ids': [ignore_empty, six.text_type]
            },
            'iframed': False,
            'default_title': p.toolkit._('ArcGIS MapServer Service')
        }

    def can_view(self, data_dict):
        if 'url' not in data_dict['resource']:
            return False
        format_lower = data_dict['resource'].get('format', '').lower()
        return format_lower in DEFAULT_AGS_FORMATS

    def view_template(self, context, data_dict):
        return 'agsview/ags_ms_view.html'

    def form_template(self, context, data_dict):
        return 'agsview/ags_ms_form.html'

    def get_helpers(self):
        return {
            'version': version_builder
        }

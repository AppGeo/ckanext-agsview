# encoding: utf-8

import logging
import ckan.plugins as p

log = logging.getLogger(__name__)
ignore_empty = p.toolkit.get_validator('ignore_empty')


DEFAULT_AGS_FORMATS = ['ags']


def get_config_item():
    return 'test'


class AGSFSView(p.SingletonPlugin):
    '''This plugin makes views of arcgis FeatureServer services'''

    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IResourceView, inherit=True)
    p.implements(p.ITemplateHelpers, inherit=True)

    def update_config(self, config):
        p.toolkit.add_public_directory(config, 'public')
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_resource('public', 'ckanext-agsview')

    def info(self):
        return {'name': 'ags_fs_view',
                'title': p.toolkit._('ArcGIS FeatureServer Service'),
                'icon': 'compass',
                'schema': {
                    'ags_url': [ignore_empty, unicode],
                    'basemap_url': [ignore_empty, unicode]
                },
                'iframed': False,
                'default_title': p.toolkit._('ArcGIS FeatureServer Service'),
                }

    def can_view(self, data_dict):
        return (data_dict['resource'].get('format', '').lower()
                in DEFAULT_AGS_FORMATS)

    def view_template(self, context, data_dict):
        return 'ags_fs_view.html'

    def form_template(self, context, data_dict):
        return 'ags_fs_form.html'

    def get_helpers(self):
        h = {'ags_view_get_config_item': get_config_item}
        return h


class AGSMSView(p.SingletonPlugin):
    '''This plugin makes views of arcgis MapServer services'''

    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IResourceView, inherit=True)

    def update_config(self, config):
        p.toolkit.add_public_directory(config, 'public')
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_resource('public', 'ckanext-agsview')

    def info(self):
        return {'name': 'ags_ms_view',
                'title': p.toolkit._('ArcGIS MapServer Service'),
                'icon': 'compass',
                'schema': {
                    'ags_url': [ignore_empty, unicode],
                    'basemap_url': [ignore_empty, unicode],
                    'layer_ids': [ignore_empty, unicode]
                },
                'iframed': False,
                'default_title': p.toolkit._('ArcGIS MapServer Service'),
                }

    def can_view(self, data_dict):
        return (data_dict['resource'].get('format', '').lower()
                in DEFAULT_AGS_FORMATS)

    def view_template(self, context, data_dict):
        return 'ags_ms_view.html'

    def form_template(self, context, data_dict):
        return 'ags_ms_form.html'

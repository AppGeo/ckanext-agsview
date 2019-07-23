# encoding: utf-8
import json
import logging
import ckan.plugins as p

try:
    # CKAN 2.7 and later
    from ckan.common import config
except ImportError:
    # CKAN 2.6 and earlier
    from pylons import config


log = logging.getLogger(__name__)
ignore_empty = p.toolkit.get_validator('ignore_empty')


DEFAULT_AGS_FORMATS = ['ags', 'esri rest']


def ags_view_default_basemap_url():
    return config.get('ckanext.ags_view_default_basemap_url', '')


def ags_view_proxy():
    return config.get('ckanext.ags_view_proxy', '{}')


def with_proxy(url):
    text = url
    proxies = json.loads(ags_view_proxy())
    for p in proxies:
        text = text.replace(p, proxies[p])
    return text


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
        return (data_dict['resource'].get('format', '').lower()
                in DEFAULT_AGS_FORMATS)

    def view_template(self, context, data_dict):
        return 'ags_fs_view.html'

    def form_template(self, context, data_dict):
        return 'ags_fs_form.html'

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

    # ITemplateHelpers

    def get_helpers(self):
        h = {'ags_view_default_basemap_url': ags_view_default_basemap_url,
             'ags_view_proxy': ags_view_proxy,
             'with_proxy': with_proxy}
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

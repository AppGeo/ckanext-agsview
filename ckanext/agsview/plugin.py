# encoding: utf-8

import logging
import ckan.plugins as p

log = logging.getLogger(__name__)
ignore_empty = p.toolkit.get_validator('ignore_empty')

DEFAULT_AGS_FORMATS = ['ags']


class AGSView(plugins.SingletonPlugin):
    '''This plugin makes views of arcgis online resources'''

    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IResourceView, inherit=True)

    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'templates')

    def info(self):
        return {'name': 'ags_view',
                'title': p.toolkit._('ArcGIS Server'),
                'icon': 'compass',
                'schema': {'map_url': [ignore_empty, unicode]},
                'iframed': False,
                'always_available': True,
                'default_title': p.toolkit._('ArcGIS Server'),
                }

    def can_view(self, data_dict):
        return (data_dict['resource'].get('format', '').lower()
                in DEFAULT_AGS_FORMATS)

    def view_template(self, context, data_dict):
        return 'ags_view.html'

    def form_template(self, context, data_dict):
        return 'ags_form.html'

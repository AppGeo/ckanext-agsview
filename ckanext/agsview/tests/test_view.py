import ckan.plugins as p
from ckan.tests import factories

def test_ags_fs_view_on_resource_page():
    sysadmin = factories.Sysadmin()
    dataset = factories.Dataset()
    resource = factories.Resource(
        package_id = dataset['id'],
        url = 'https://sampleserver6.arcgisonline.com/arcgis/rest/services/Wildfire/FeatureServer/0',
        format = 'Esri REST'
    )
    resource_view = factories.ResourceView(
        resource_id = resource['id'],
        title = 'ArcGIS FeatureServer Service',
        view_type = 'ags_fs_view'
    )

    response = p.toolkit.get_action('resource_view_show')(
        {'user': sysadmin.get('name')},
        {'id': resource_view.get('id')}
    )

    assert response.get('title') == 'ArcGIS FeatureServer Service'
    assert response.get('view_type') == 'ags_fs_view'


def test_ags_ms_view_on_resource_page():
    sysadmin = factories.Sysadmin()
    dataset = factories.Dataset()
    resource = factories.Resource(
        package_id = dataset['id'],
        url = 'https://sampleserver6.arcgisonline.com/arcgis/rest/services/USA/MapServer/0',
        format = 'Esri REST'
    )
    resource_view = factories.ResourceView(
        resource_id = resource['id'],
        title = 'ArcGIS MapServer Service',
        view_type = 'ags_ms_view'
    )

    response = p.toolkit.get_action('resource_view_show')(
        {'user': sysadmin.get('name')},
        {'id': resource_view.get('id')}
    )

    assert response.get('title') == 'ArcGIS MapServer Service'
    assert response.get('view_type') == 'ags_ms_view'

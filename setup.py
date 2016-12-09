# -*- coding: utf-8 -*-
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='''ckanext-agsview''',
    version='0.1.1',

    description='''An extension contains that display ArcGIS Map services (cached,
    dynamic) and Feature layer services in CKAN.''',
    long_description=long_description,
    url='https://github.com/AppGeo/ckanext-agsview',

    author='''Guido Stein''',
    author_email='''gstein@appgeo.com''',
    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='''CKAN esri ArcGIS Server MapServer FeatureServer GIS''',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    namespace_packages=['ckanext'],
    entry_points='''
        [ckan.plugins]
        ags_fs_view=ckanext.agsview.plugin:AGSFSView
        ags_ms_view=ckanext.agsview.plugin:AGSMSView
    '''
)

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#from plugins import typo

AUTHOR = u'Juda Kaleta'
SITENAME = u'Zápisník'
SITEURL = 'http://zapisnik.glor.cz'

TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = u'cs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

WITH_FUTURE_DATES = False

DEFAULT_CATEGORY = u'Článek'

SLUGIFY_SOURCE = 'basename'
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

AUTHORS_SAVE_AS = None
CATEGORY_SAVE_AS = 'kategorie/{slug}.html'
CATEGORIES_SAVE_AS = 'kategorie.html'
TAGS_SAVE_AS = 'nalepky.html'
ARCHIVES_SAVE_AS = 'archiv.html'
TAG_SAVE_AS = 'nalepka/{slug}.html'

AUTHOR_URL = 'autor/{slug}.html'
CATEGORY_URL = 'kategorie/{slug}.html'
TAG_URL = 'nalepka/{slug}.html'


#DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
#SITEMAP_SAVE_AS = 'sitemap.xml'

TYPOGRIFY = True

PLUGIN_PATHS = ['./pelican-plugins/', ]
#PLUGINS = ['sitemap', 'render_math', 'simple_footnotes', 'related_posts', 'plugins.unveil']
PLUGINS = ['sitemap', 'render_math', 'simple_footnotes', 'related_posts']


RELATED_POSTS_MAX = 10

SITEMAP = {
    'format': 'xml',
}

# Theming
THEME = 'theme'
THEME_STATIC_PATHS = ('static',)

STATIC_PATHS = (
    'images',
)

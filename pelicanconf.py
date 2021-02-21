#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Taisei Project'
SITENAME = 'Taisei Project'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

THEME = 'theme/taisei-orig'

ARTICLE_PATHS = ['news']

PAGE_PATHS = ['pages']

ARCHIVES_SAVE_AS = 'news/index.html'
CATEGORIES_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAGS_SAVE_AS = ''
INDEX_SAVE_AS = '' # disabled
AUTHOR_SAVE_AS = ''

ARTICLE_URL = 'news/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'news/{date:%Y}/{date:%m}/{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# displayname, pagename, path, subscript

TAISEI_VERSION = '1.3.1'

NAVBAR = (
    ('Home', 'home', SITEURL + '/', ''),
    ('News', 'news', SITEURL + '/news', ''),
    ('Media', 'media', SITEURL + '/media', ''),
    ('Download', 'download', SITEURL + '/download', TAISEI_VERSION),
    ('GitHub', 'github', 'https://github.com/taisei-project/taisei', ''),
    ('Play In Browser', 'play', SITEURL + '/play', 'Beta'),
)

# Blogroll
LINKS = (
         ('GameManual', 'https://github.com/taisei-project/taisei/blob/master/doc/GAME.rst'))

# Social widget
SOCIAL = (('Discord', 'https://discord.gg/JEHCMzW'))

DEFAULT_PAGINATION = 5

PLUGINS = [
    "jinja2content",
    "pelican_youtube",
]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

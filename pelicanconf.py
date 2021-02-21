#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Taisei Project'
SITENAME = 'Taisei Project'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

THEME = 'theme/taisei-orig'

INDEX_SAVE_AS = 'news/index.html'

ARTICLE_PATHS = ['news']


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Github', 'https://github.com/taisei-project/taisei'),
         ('GameManual', 'https://github.com/taisei-project/taisei/blob/master/doc/GAME.rst'))

# Social widget
SOCIAL = (('Discord', 'https://discord.gg/JEHCMzW'))

DEFAULT_PAGINATION = 5

PLUGINS = [
    "jinja2content",
    "pelican_youtube",
]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

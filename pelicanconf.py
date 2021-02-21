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

PLUGIN_PATHS = ['pelican-plugins']

# change this when a new version is released
TAISEI_VERSION = '1.3.1'

TAISEI_GIT = 'https://github.com/taisei-project/taisei'
TAISEI_RELEASE_URL = '{0}/releases/download/v{1}/Taisei-{1}-'.format(TAISEI_GIT, TAISEI_VERSION)

RELEASE_LINKS = {
    'windows-x64-setup': ('setup-x86_64.exe', '64-bit (installer)'),
    'windows-x86-setup': ('setup-x86.exe', '32-bit (installer)'),
    'windows-x64-zip': ('windows-x86_64.zip', '64-bit (zip)'),
    'windows-x86-zip': ('windows-x86.zip', '32-bit (zip)'),
    'macos': ('macOS-x86_64.dmg', '64-bit (macOS 10.7 or later required)'),
    'linux': ('linux-x86_64.tar.xz', '64-bit (glibc 2.24 or later)'),
    'switch': ('switch-aarch64.zip', '(Homebrew)'),
}

NAVBAR = (
    ('Home', 'home', SITEURL + '/', ''),
    ('News', 'news', SITEURL + '/news', ''),
    ('Media', 'media', SITEURL + '/media', ''),
    ('GitHub', 'github', TAISEI_GIT, ''),
    ('Download', 'download', SITEURL + '/download', TAISEI_VERSION),
    ('Play In Browser', 'play', SITEURL + '/play', 'Beta'),
)

# Blogroll
LINKS = (('GameManual', TAISEI_GIT + '/blob/master/doc/GAME.rst'),)

# Social widget
SOCIAL = (('Discord', 'https://discord.gg/JEHCMzW'))

DEFAULT_PAGINATION = 5

PLUGINS = [
    "jinja2content",
    "pelican_youtube",
    "release_links",
]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

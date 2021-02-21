# -*- coding: utf-8 -*-
"""
Heavily based off of "interlinks" official pelican plugin

"""

import re

from pelican import signals
from pelicanconf import TAISEI_RELEASE_URL, TAISEI_VERSION

from bs4 import BeautifulSoup
from bs4 import SoupStrainer

release_links = {}

def getSettings(generator):
    global release_links

    if 'RELEASE_LINKS' in generator.settings:
        for key, value in generator.settings['RELEASE_LINKS'].items():
            release_links[key] = value

def parse_links(instance):
    if instance._content is not None:
        content = instance._content

        if '<a' in content:
            text = BeautifulSoup(
                content, "html.parser", parse_only=SoupStrainer("a"))
            for link in text.find_all("a", href=True):
                old_url = link.decode()
                old_text = link.get_text()
                url = link.get('href')
                name = url.replace('!', '')
                if name in release_links:
                    hi = url.replace(name + "!", TAISEI_RELEASE_URL + release_links[name][0])
                    link['href'] = hi
                    link.string = "v{0} ".format(TAISEI_VERSION) + release_links[name][1]
                content = content.replace(old_url, link.decode())
        instance._content = content

def register():
    signals.generator_init.connect(getSettings)
    signals.content_object_init.connect(parse_links)

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'grupy-sp'
SITENAME = u'GruPy-SP'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_PAGES_ON_MENU = True

THEME = "./themes/bootstrap"

# Blogroll
LINKS = (('Sobre nós', 'http://grupy-sp.github.io/pages/about.html'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/grupy-sp/encontros'),
         ('Facebook', 'https://www.facebook.com/grupysp'),
         ('Twitter', 'https://twitter.com/grupysp/'),
         ('Slack', 'https://grupysp.herokuapp.com/'),
         ('Google Groups',
          'https://groups.google.com/forum/#!forum/grupy-sp'),
         ('Meetup', 'http://www.meetup.com/pt/Grupy-SP/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

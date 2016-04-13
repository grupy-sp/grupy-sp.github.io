#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)
from themes.malt.functions import *
from collections import OrderedDict

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

THEME = "./themes/malt"

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

GITHUB_REPO = "https://github.com/grupy-sp/grupy-sp.github.io"
GITHUB_BRANCH = "pelican"

ARTICLE_BANNERS_FOLDER = "images/banners"
SITE_BACKGROUND_IMAGE = "images/sp.jpg"
SITE_LOGO = "images/logo-grupy.png"

MALT_BASE_COLOR = "blue"

# Membros do Grupy
MEMBROS = OrderedDict((
    ("Eric Hideki", {
        "twitter": "@erichideki",
        "github": "erichideki",
        "site": {
            "nome": "Aprendendo Python",
            "href": "https://ericstk.wordpress.com/",
            }
        }),
))

FOOTER_ABOUT = "O Grupy-SP é um grupo de usuários de Python da cidade de São Paulo/SP."

# Links sociais do rodapé
SOCIAL_LINKS = (
    {
        "href": "https://github.com/grupy-sp/grupy-sp.github.io",
        "icon": "fa-github",
        "text": "Grupy-SP",
    },
    {
        "href": "https://www.facebook.com/grupysp",
        "icon": "fa-facebook",
        "text": "Facebook",
    },
    {
        "href": "https://twitter.com/grupysp/",
        "icon": "fa-twitter",
        "text": "Twitter",
    },
    {
        "href": "https://grupysp.herokuapp.com/",
        "icon": "fa-slack",
        "text": "Slack",
    },
    {
        "href": "https://groups.google.com/forum/#!forum/grupy-sp",
        "icon": "fa-envelope",
        "text": "Google Groups",
    },
    {
        "href": "http://wiki.python.org.br/",
        "icon": "fa-globe",
        "text": "Python Brasil",
    },
    {
        "href": "https://python.org",
        "icon": "fa-globe",
        "text": "Python",
    },
)
NAVBAR_HOME_LINKS = [
]

NAVBAR_BLOG_LINKS = NAVBAR_HOME_LINKS + [
    {
        "title": "Autores",
        "href": "authors.html",
    },
    {
        "title": "Categories",
        "href": "categories.html",
    },
    {
        "title": "Tags",
        "href": "tags.html",
    },
    {
        "title": "Sobre Nos",
        "href": "pages/about.html",
    },
]

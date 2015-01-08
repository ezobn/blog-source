#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Evgeny Zobnitsev'
SITENAME = u'FGTS Blog'
SITEURL = ''
#Custom for fresh teame
GOOGLE_CUSTOM_SEARCH = '010876618395126198893:3pktv5ynnok'
#HIDE_CATEGORIES_FROM_MENU = True
SHARETHIS_PUB_KEY = 'c6a57063-7758-43f1-8987-728852dc33b8'

#global
DISQUS_SITENAME = 'blogfgtsru'
#GOOGLE_ANALYTICS = ''
GITHUB_URL = 'https://ezobn.github.io/blog'

PATH = 'content'
#THEME = '/home/ez/virtualenvs/pelican/src/pelican/pelican/themes/github/BT3-Flat'
#THEME = '/home/ez/virtualenvs/pelican/src/pelican/pelican/themes/github/blue-penguin'
#THEME = '/home/ez/virtualenvs/pelican/src/pelican/pelican/themes/github/built-texts'
#THEME = '/home/ez/virtualenvs/pelican/src/pelican/pelican/themes/github/crowsfoot'
#THEME = '/home/ez/virtualenvs/pelican/src/pelican/pelican/themes/github/pure'
#THEME = '/home/ez/virtualenvs/pelican/src/pelican/pelican/themes/github/html5-dopetrope'
#THEME = '/home/ez/virtualenvs/pelican/src/pelican/pelican/themes/github/elegant'
#THEME = '/home/ez/virtualenvs/pelican/src/pelican/pelican/themes/github/fresh'
THEME = 'fresh'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Factor Group', 'http://fgts.ru/'),
         ('Factor Group blog', 'http://blog.fgts.ru/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/ezobn'),
          ('github', 'http://github.com/ezobn'),)

DEFAULT_PAGINATION = 10

#TWITTER_USERNAME = 'ezobn'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#STATIC_PATHS = ['images',
#                'other/robots.txt',
#                'other/favicon.ico',
#                'other/arbitrary.html',
#                ]

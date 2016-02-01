#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'hackrole'
SITENAME = u"hackrole's note"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

DEFAULT_LANG = u'zh'

SUMMARY_MAX_LENGTH = 20

# use filename for blog title
SLUGIFY_SOURCE = 'basename'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# ignore directory and files
IGNORE_FILES = ['note', ]

# static path for favion.icon
STATIC_PATHS = [
    'static',
]
EXTRA_PATH_METADATA = {
    'static/favicon.ico': {
        'path': 'favicon.ico'
    },
}

# theme
THEME = 'aboutwilson'

# Blogroll
LINKS = [
    ('向日葵的博客', 'http://zshou.is-programmer.com/'),
    ('solos的网络日志', 'http://solos.so/'),
]

SOCIAL = [
    ('github', 'http://github.com/hackrole'),
    ('coding', 'https://coding.net/u/hackrole'),
]

PLUGIN_PATHS = [
    '/home/daipeng/hr-conf/pelican-plugins',
]
PLUGINS = [
    "disqus_static",
    "series",
    # "sitemap",
    "plantuml",
]

# disqus comment
DISQUS_SITENAME = "hackrole"
DISQUS_PUBLIC_KEY = ('X83kWZqXZ1xbOxi0QS2P9qnbxerhA5C59a80O7M'
                     'W3G0qsDOpEwklaAcR3oVcG0uv')
DISQUS_SECRET_KEY = ('za2LQQnPg7oRPOYmVrFkEt2HD6KWIrjolR3icno'
                     'yxmqxSOaATH6MoFROXlrrFQqA')

# define sitemap
# SITEMAP = {
#     'format': 'xml',
#     'priorities': {
#         'articles': 0.5,
#         'indexes': 0.5,
#         'pages': 0.5
#     },
#     'changefreqs': {
#         'articles': 'monthly',
#         'indexes': 'daily',
#         'pages': 'monthly'
#     }
# }

# add templates for sitemaps
DIRECT_TEMPLATES = ('index', 'tags', 'categories',
                    'archives', 'sitemap', 'drafts')
SITEMAP_SAVE_AS = 'sitemap.xml'
DRAFTS_SAVE_AS = 'drafts.html'

# page size
DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

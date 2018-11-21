# -*- coding: utf-8 -*- #

# pylint: disable=missing-docstring

from __future__ import unicode_literals

from os import path

# 项目跟目录
BASE_DIR = path.dirname(path.realpath(__file__))

AUTHOR = u'hackrole'
SITENAME = u"hackrole's note"
SITEURL = ''
SITESUBTITLE = u"愿所有英雄气概都得以归宿"

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

# === theme ====
# THEME = 'new-bootstrap2'
THEME = path.join(BASE_DIR, 'themes/gum')
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# foundation-default-colours theme config
# THEME = 'foundation-default-colours'
# FOUNDATION_PYGMENT_THEME = 'vs'


# Blogroll
LINKS = [
    ('向日葵的博客', 'http://zshou.is-programmer.com/'),
    ('solos的网络日志', 'http://solos.so/'),
    ('leei blog', 'https://leeifrankjaw.github.io'),
]

SOCIAL = [
    ('github', 'http://github.com/hackrole'),
    ('coding', 'https://coding.net/u/hackrole'),
    ('TWITTER_URL', ''),
    ('FACEBOOK_URL', ''),
]
GITHUB_URL = 'http://github.com/hackrole'


PLUGIN_PATHS = [
    path.join(BASE_DIR, "plugins"),
]
PLUGINS = [
    # need: pip install disqus-python
    # "disqus_static",
    "series",
    "tag_cloud",
    # "sitemap",
    "plantuml",
    # 'ga_page_view',
]

# disqus comment
DISQUS_SITENAME = "hackrole"
DISQUS_PUBLIC_KEY = ('X83kWZqXZ1xbOxi0QS2P9qnbxerhA5C59a80O7M'
                     'W3G0qsDOpEwklaAcR3oVcG0uv')
DISQUS_SECRET_KEY = ('za2LQQnPg7oRPOYmVrFkEt2HD6KWIrjolR3icno'
                     'yxmqxSOaATH6MoFROXlrrFQqA')

# tag cloud
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 50
TAG_CLOUD_BADGE = True

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
# TODO tmp remove sitemap and drafts
# DIRECT_TEMPLATES = ('index', 'tags', 'categories',
#                     'archives', 'sitemap', 'drafts')
# SITEMAP_SAVE_AS = 'sitemap.xml'
# DRAFTS_SAVE_AS = 'drafts.html'
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives')

# page size
DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

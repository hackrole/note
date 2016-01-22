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

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# static path for favion.icon
# STATIC_PATHS = [
    # 'static/favicon.ico',
# ]
# EXTRA_PATH_METADATA = {
    # 'static/favicon.ico': {
        # 'path': 'favicon.ico'
    # },
# }

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
    # u"disqus_static",
]

# disqus comment
DISQUS_SITENAME = u'http://note.hackrole.com/'
DISQUS_PUBLIC_KEY = u'X83kWZqXZ1xbOxi0QS2P9qnbxerhA5C59a80O7MW3G0qsDOpEwklaAcR3oVcG0uv'
DISQUS_SECRET_KEY = u'za2LQQnPg7oRPOYmVrFkEt2HD6KWIrjolR3icnoyxmqxSOaATH6MoFROXlrrFQqA'

# page size
DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

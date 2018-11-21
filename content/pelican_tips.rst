pelican使用tips
===============

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-29 11:15:34
:status: published
:tags: pelican

不要配置SITEURL
---------------

在pelicanconf.py里配置SITEURL后，生成的页面里所有url都会带上这个url.
使用起来反而更加麻烦.

.. code-block:: html

   <!-- 不设置SITE_URL生成的链接 -->
   <a href="/chrome_tips.html" />

   <!-- 设置SITE_URL生成的链接 -->
   <a href="http://www.blog.com/chrome_tips.html" />

设置时间默认的格式
------------------

默认的时间格式看着挺不习惯. 在pelicanconf.py里加入如下配置修改.

.. code-block:: python

   TIMEZONE = 'Asia/Shanghai'
   DEFAULT_DATE_FORMAT = '%Y-%m-%d'

使用文件名做url
---------------

默认情况下pelican生成的页面使用article的标题的中文拼音做页面的url.

如果你博客的标题是 **chrome_开发tips**, 文件名是 **chrome_dev_tips**.
默认情况下生成的文件名为 **chrome_kai_fa_tips.html**.

通过设置 `SLUGIFY_SOUTCE` 来修改.

.. code-block:: python

   SLUGIFY_SOUTCE = 'basename' # use filename. default use article title.

忽略部分文件
------------

有时会想再content目录下放些暂时不想被pelican解析的内容.
比如用org做的临时性笔记.

.. code-block:: python

   # 目录和文件都可以
   IGNORE_FILES = ['org-note', 'not-me.html']

处理静态文件
------------

可以把静态文件(图片/视频/css等)放到content/images目录, 之后在article/page中引用。
在pelican build的时候会把images整个目录拷贝到output里.

但是有时希望把图片和其他格式静态资源分开. 可是使用如下设置.

.. code-block:: python

   # default is ['images']. set it to ['static'].
   # and make images/css/video directory under the static directory
   STATIC_PATHS = [
       'static',
   ]

默认是直接把STATIC整个目录拷贝过去. 也可以指定不同的STATIC拷贝到不同的目录.

.. code-block:: python

   EXTRA_PATH_METADATA = {
       'static/images/favicon.ico': {
           'path': 'favicon.ico',
        },
        'static/robot.txt': {
            'path': 'robot.txt',
        }
    }

增加友链和社交帐号
------------------

.. code-block:: python

   # 友链
   LINKS = [
       ('朋友A的博客', 'http://a.blog.com'),
       ('朋友B的博客', 'http://b.blog.com'),
   ]

   # 社交帐号
   SOCIAL = [
       ('github', 'http://your.github.com'),
       ('twiier', 'http://twitter.com/your'),
   ]

设置分页大小
------------

.. code-block:: python

   DEFAULT)_PAGINATION = 6

新增模板
--------

如果希望新加个页面来查看所有的drafts状态的博客列表，
或者想生成个sitemap.xml文件优化搜索引擎.可以使用如下配置.

.. code-block:: python

    # add sitemap and drafts
    DIRECT_TEMPLATES = ('index', 'tags', 'categories',
                        'archives', 'sitemap', 'drafts')
    SITEMAP_SAVE_AS = 'sitemap.xml'
    DRAFTS_SAVE_AS = 'drafts.html'

之后需要在themes里添加 **sitemap.html(不是xml)** 和 drafts.html文件.
重新 `fab rebuild` 就可以了.

如果使用pelican-themes管理themes, 要使用如下命令更新themes.

.. code-block:: bash

   pelican-theme -U <theme-dir>


插件管理及常用插件
------------------

**TODO**

文章serial
----------

**TODO**

添加disqus评论功能
------------------

**TODO**

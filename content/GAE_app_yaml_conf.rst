app.yaml configue for google app engine
=======================================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2013-09-08 15:51:45
:status: draft
:tags: GAE, yaml

elements
--------

application
~~~~~~~~~~~

application id
应用程序id, gae id

version
~~~~~~~

应用程序版本号,用于多版本管理和切换

runtime
~~~~~~~

运行环境, 如python27

handlers  
~~~~~~~~~~

路由配置,最重要的配置项
参考  script handler与static handler::

    handlers:
    1. url: /images
       static_dir: static/images
    2. url: /.*
       script: hello.app

api_version
~~~~~~~~~~~

threadsafe
~~~~~~~~~~

default_expiration
~~~~~~~~~~~~~~~~~~

静态文件默认缓存时间
例子:
default_expiration: "4d 5h"

script heandler
---------------

example
~~~~~~~
::

    handlers:
      url: /list/(.*?)/(.*)
        script: hello.app
        login:
        autho_fail_action:
        secure:

static handler
--------------

elements
~~~~~~~~

Directory:
""""""""""

1) url

2) static_dir

3) application_readable: make the app can read the files

4) mime_type

5) http_headers

6) expiration

FIle:
"""""

1) url

2) static_files: 使用\1\2正则匹配

3) upload: ??

4) application_readable:

5) mimetype

6) http_headers

7) expiration

example
~~~~~~~

builtin handlers
----------------

例子
~~~~
::

    builtions:
    1. datasotore_admin: on
    2. appstats: on

??
~~

1) /_ah/admin

2) /_ah/stats/

3) /_ah/datastore_admin

4) /_ah/remote_api

5) /_ah/queue/deferred

includes
--------


libraries
---------
::

    - name: jinja2
      version: latest


admin console custom page
-------------------------
::

    admin_console:
      pages:
      - name:
         url:

error_handlers
--------------


Rewriters
---------


总结
----


| title        | status         | desc |
| Rewrite      | TODO           |      |
| includes     | TODO           |      |
| /_ah         | TODO           |      |
| skip_files   | not understadn |      |
| Env variable | os.environment |      |

待整理
------

**TODO**


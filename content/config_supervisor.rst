superviosr配置小节
==================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-26 16:10:34
:status: draft
:tags: python,supervisord
:category: tools

概述
----

supervisor主要用与监控其他进程状态, 并支持 **启动/重启/停止/自动重启** 进程。

supervisor采用client/server模式.

1) 一个supervisord进程负责实际的 **进程监控和操作**.

2) 一个supervisorctl负责连接到superviosrd, 并接受转发用户的操作.

supervisor将所有要监控和管理进程启动为自己的子进程。
为了配合supervisor使用，所有进程都要设置为 **no-deamon** 模式.
当子进程 **exit** 时，superviosrd可以接受到SIGCHLG信号.
supervisord通过向子进程发送信号的方式来控制子进程行为，所有需要子进程能正确相应信号.

配置相关
--------

supervisor使用ini格式的配置文件. 配置大体可以分为几个 **section** ,
每个 **section** 都有自己对应的参数.
这里不一一熬述，只列举重要的一些.
具体内容可以参阅 supervisord官网: http://supervisord.org/configuration.html

配置中可以使用环境变量, 语法如下.

.. code-block:: ini

   [program:x]
   command = cat -f ${HOME}/cat.log


unix_http_server section
~~~~~~~~~~~~~~~~~~~~~~~~

配置一个 **unix-socket** 用来完成supervisor服务端和客户端的通信.

:file: 配置unix-socket文件路径.

:chmod: 设置unix-socket文件权限.

:chuser: 设置unix-socket所属用户

实例如下:

.. code-block:: ini

    [unix_http_server]
    file = /tmp/supervisor.sock
    chmod = 0777
    chown= nobody:nogroup
    username = user
    password = 123

inet_http_server section
~~~~~~~~~~~~~~~~~~~~~~~~

配置的 **http** 完成supervisord和supervisorctl的通信.
**unix-socket** 的模式只用用于单机, **http** 服务和客户可以在不同主机上.

:port: ip:port

.. code-block:: ini

    [inet_http_server]
    port = 127.0.0.1:9001
    username = user
    password = 123

supervisord Section
~~~~~~~~~~~~~~~~~~~

配置supervisord相关内容.

:directory: change目录

:umask: 进程权限屏蔽

:pidfile: pid文件

:environment: 环境变量

.. code-block:: ini

    [supervisord]
    logfile = /tmp/supervisord.log
    logfile_maxbytes = 50MB
    logfile_backups=10
    loglevel = info
    pidfile = /tmp/supervisord.pid
    nodaemon = false
    minfds = 1024
    minprocs = 200
    umask = 022
    user = chrism
    identifier = supervisor
    directory = /tmp
    nocleanup = true
    childlogdir = /tmp
    strip_ansi = false
    environment = KEY1="value1",KEY2="value2"


supervisorctl Section
~~~~~~~~~~~~~~~~~~~~~

配置supervisorctl.

:serverurl:
    **unix-socket file** or **inet http ip:port**

.. code-block:: ini

    [supervisorctl]
    serverurl = unix:///tmp/supervisor.sock
    username = chris
    password = 123
    prompt = mysupervisor

program:x Section
~~~~~~~~~~~~~~~~~

配置要管理的进程，可以配置多个.

**TODO**

include Section
~~~~~~~~~~~~~~~

group Section
~~~~~~~~~~~~~

event-listener Section
~~~~~~~~~~~~~~~~~~~~~~

见其他博客内容

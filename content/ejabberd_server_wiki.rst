ejabberd服务器配置与常见问题汇总
================================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-08 14:51:58
:tags: ejabberd,

pt-get安装后无法启动server
--------------------------


1) 查看下/etc/ejabberd/目录下文件的所有者和文件权限

2) 查看下/var/log/ejabberd/目录下的文件所有者和文件权限

3) ps aux | grep ejabberd 查看是否有运行中的ejabberd服务

admin登录失败
-------------


1) 用户名应使用admin@localhost,而不是admin

2) 调用sudo ejabberdctl register admin localhost admin

3) 检查/etc/ejabberd/ejabberd.cfg配置文件::

    1) {acl, admin, {user, "admin", "localhost"}}.

    2) {hosts, ["localhost", "192.168.1.106"]}.

    3) {access, configure, [{allow, admin}]}.

    4)   {5280, ejabberd_http, [
             %%{request_handlers,
             %% [
             %%  {["pub", "archive"], mod_http_fileserver}
             %% ]},
             %%captcha,
             http_bind,
             http_poll,
             web_admin
            ]}


配置外部认证
~~~~~~~~~~~~

1) 配置 auth_method: ext, ext_auth_path: '',

2) 重启服务查看日志，外部日志是否正常

3) ejabberdctl check* 检查是否生效

4) 外部认证书写可以参考官网


配置离线推送
------------

1) 编写一个erlang模块，注册offline-hooks.

2) 在offline-hooks里调用apns的http方法

编写扩展模块
------------


python sleekxmpp
----------------


机器人client.
~~~~~~~~~~~~~

sleekxmpp.ClientXmpp


server component
""""""""""""""""

sleekxmpp.ComponentXmpp

全局的filter/hooks
~~~~~~~~~~~~~~~~~~

new plugin/extension/stanze
"""""""""""""""""""""""""""


erlang mode
~~~~~~~~~~~


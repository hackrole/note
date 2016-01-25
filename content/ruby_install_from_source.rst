编译安装ruby问题总结
====================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2014-01-14 17:59:31
:status: published
:tags: ruby, make, source-install

多版本ruby与rvm问题
-------------------

rvm是用来管理ruby多版本的gem包, 可以用来在多个ruby版本间切换或安装ruby.

rvm是通过修改环境变量的方式, 所以配合gvim等时会有些不方便。
建议还是在系统里编译个最新版的ruby好些.

.. note::

    多版本管理不能和virtualenv相互替代，用途不同.
    rvm和python virtualenv作用不同.

卸载ruby导致vim/gvim无法启动
----------------------------

vim/gvim如果有+ruby特性，在找不到 libruby-*.so.* 时，是无法启动.

解决方法.
.. code-block:: ruby

    sudo aptitude purge ruby vim-common vim vim-gnome
    sudo aptitude install ruby vim vim-gnome

卸载ruby导致emacs启动报错问题
-----------------------------

原因应该是因为我装了evernote-mode这个插件，这个插件依赖ruby
重新安装下ruby就解决了

ldd实用命令
-----------

解决ruby问题时，偶尔发现的一个帖子. **TODO** 帖子url

.. code-block:: shell

    ldd `which vim`

可以查看对应软件依赖的共享库(.so)
配合grep可以很好的定位依赖库找不到导致的问题

编译ruby
--------

编译前记得安装readline库, 不然无法使用补全。

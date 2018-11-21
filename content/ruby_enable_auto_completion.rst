ruby下的irb/iruby如何使用补全
=============================
:date: 2016-01-08 10:20
:author: hackrole
:email: daipeng123456@gmail.com
:tags: ruby,tips
:category: programming


概述
----

ruby补全需要先安装readline-dev包

.. code-block:: shell

    sudo aptitude install libreadline6 libreadline6-dev

如果已经编译过ruby,并且不支持补全，需要先安装readline.然后重新编译ruby.

irb补全
~~~~~~~

ruby下自带irb交互式环境， 开启irb补全需要将一下内容加入到 ~/.irbrc文件.

.. code-block:: ruby

    require 'irb/completion'

bond补全
~~~~~~~~

更好的补全: http://tagaholic.me/2009/07/22/better-irb-completion-with-bond.html

bond是一个ruby-gems, 用来增强irb的补全功能.

1) 需要安装bond-gem.

.. code-block:: ruby

   sudo gem install bond

2) 需要修改~/.irbrc.

.. code-block:: ruby

    require 'bond'
    require 'bond/completion'

iruby补全
~~~~~~~~~

iruby是ruby下配合ipython一个工具，可以使用jupyter notebook在web上编辑和保存.

安装方式见官网:: https://github.com/SciRuby/iruby

只要配置和bond或irb,iruby就可以使用补全.

iruby notebook类似jupyter notebook的体验.
比较适合用来学习和记录笔记。

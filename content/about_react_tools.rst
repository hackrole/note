react相关工具
=============

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-02-16 11:45:30
:status: draft
:tags: react, javascript
:category: programming

写在前面
--------

react最近火的不行，但是想入门却比angular之类的难不少, 但真要说的话react内容并不多，应该比anuglar简单很多才对。
原因个人觉的有以下几点:


一:版本问题
~~~~~~~~~~~

react至今仍在开发开素迭代中，官方最新版本版本是0.14.x(真不知道啥时才能有1.x版本).
但是很多教程上一般都还在使用0.12版本，所以一般照教程做都很难做下去.

二:内容真不少
~~~~~~~~~~~~~

react这玩意内容说多不多，说少也不少.
jsx说白了就是个语法糖，但是为了这个语法糖你就要搞明白 babel/browserify/watchify等一系列的工具.
偏偏很多教程还喜欢用es6来写react, 无疑雪上加霜。

最搞的莫过于flux,官方文档实在不敢恭维. 官方tutorial和github里的example完全对不上.看好多flux教程上
的博主也是被flux折腾过。

三:思维方式
~~~~~~~~~~~

基于组建的方式方式和以前的开放方式还是有些区别的。虽然照观望做tutorial时没多大感觉,
但真要自己写的时候还是要时间来转变思维方式的.


本文主要是列下一些常用工具，方便做个区分.

工具
----

babel
~~~~~

js转化工具, 主要用于吧es6/jsx等转化成es5.

browserify
~~~~~~~~~~

javascript包管理, 引入require/exports属性，方便js里的命名空间文件.
最后把文件合并为一个文件.

watchify
~~~~~~~~

相当与browserify的扩展，增加watch功能.

baelify
~~~~~~~

browserify的插件, 是babel和browserify和配合使用.

es6
~~~

新的javasciprt规范， 新增 括号lambda， 类等特性.


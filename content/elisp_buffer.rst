elisp buffer处理相关
====================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-08 14:55:08
:tags: elisp, emacs

buffer基本概念
--------------

buffer是一个elisp对象，包含一些必要的属性,
部分属性可以直接通过变量访问,部分属性要通过函数才能访问

buffer一般会关联一个打开的文件，也可不关联

buffer都有一个唯一name属性

buffer-local变量使得可以对不同buffer保存不同的状态等

bufferp函数测试symbal是否为buffer


buffer基本属性
--------------


the current buffer
------------------


buffer name
-----------

buffer file name
~~~~~~~~~~~~~~~~

buffer modify
~~~~~~~~~~~~~

read-only buffer
~~~~~~~~~~~~~~~~

buffer list
~~~~~~~~~~~


buffer操作函数
--------------


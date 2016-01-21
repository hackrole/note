lisp 基本概念与内建数据类型简介
===============================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2014-08-07 14:56:20
:status: draft
:tags: elisp

lisp的基本特性
--------------

+ 变量不需要提前声明

+ 几种基本类型(integer,list, buffer等)是内建实现

+ 通过函数判断数据类型，可以属于多个类型，但只能属于一种你基本类型


integer type
------------

+ 在32位机器中,  range(-2**29 to -2**29 -1)

+ lisp函数不做溢出判断，程序要注意溢出危险

float type
----------

+ 使用c语言double实现

char type
---------

+ 使用integer表示

+ range(0-4194303)

+ 读入语法形式 ?a, ?A ?\\ ?\( ?\a

...

symbol type
-----------

+ unique唯一性

+ :开头为常量

sequence types
--------------

+ 包含list和arrays两种类型

list type 与 arrays type
~~~~~~~~~~~~~~~~~~~~~~~~

+ list可以包含任意对象

+ list长度可以任意调整

cons cell and list type
-----------------------

**TODO**

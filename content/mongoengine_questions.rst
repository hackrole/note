mongodb库设计问题
=================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2014-07-31 17:49:57
:status: draft
:tags: mongodb, mongoengine, python


**TODO**

项目地址:: **TODO** ref

mongodb本身是无模式的，但是使用时都要在application层实现模式约束.

mongoengine是个mongodb ORM库。已相当成熟稳定, 使用广泛, 开发活跃.
性能相对也不错(可以参见项目下的bench).

使用下来发现mongoengine还是很不错的库，但是有部分特性使用起来并不方便.

mongoengine问题
---------------

索引问题
~~~~~~~~

索引应该跟document分开.并且有自动化建立和删除的command.

把索引定在Document/meta/indexes里很糟糕：

1) 写法很乱，不易管理。

2) 有时会失效，没有建立对应的索引

listField校验问题
~~~~~~~~~~~~~~~~~

listField没法做长度限制
set/sortset/max-len list/ sort-list等结构没有实现

不支持自定义字段验证/文档级验证
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


pre_save/after_save hooks
~~~~~~~~~~~~~~~~~~~~~~~~~


不可存储的EmbdDocumment
~~~~~~~~~~~~~~~~~~~~~~~
**TODO** 待考虑

可扩展的Document
~~~~~~~~~~~~~~~~
**TODO** 待考虑

mongodb索引建立和优化
=====================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2014-06-27 17:38:06
:status: draft
:tags: mongodb,tips

**TODO**: 来源

+ 索引可以加快读取操作，但是会降低写入和更新操作，
  一般要根据文档的读写比决定是否使用索引

+ 可以使用hint和explain来比较和测试索引的实际效果，
  但要注意mongodb热数据缓存带来的影响

+ 对于较小的集合，使用索引查询反而会让查询更慢, 因为一次大的顺序读变成了多次随机读

+ nosqlfan是个学习和找问题的好地方

mongodb索引简介
---------------

基本操作
~~~~~~~~

索引一般使用B+树结构，来优化查询操作， 建立的索引应该符合查询要求，才能发挥作用::

    db.things.ensureIndex({j:1})


默认单列/文档/组合索引
~~~~~~~~~~~~~~~~~~~~~~

+ 每个集合都会有个默认索引 `_id` ,该字段不能删除

+ 单列索引可以是独立字段，也可以是嵌套文档字段

+ 建立文档索引会导致 必须使用严格匹配的查询才能返回结果，一般用组合索引替代 **TODO**

+ 稀疏索引的概念与sql中的稀疏索引概念不同

+ mongodb不会为字段值不存在的文档加入索引,null值不能被查出

+ 唯一索引

.. code::

    db.ensureIndex({j:1}, {unique: true})
    db.ensureIndex({j:1}. {unique: true, dropDups: true})

特殊索引
--------

mongodb支持2d索引，用于地理位置服务。

mongodb支持text全文索引，但是功能较弱.

须注意：

1) mongodb 2d索引使用B+树结构，不会造成性能上的问题。勿轻信性能问题
   http://blog.nosqlfan.com/html/1811.html

2) mongodb 2d索引返回的距离不会实际距离，而是坐标点距离. 根据实际情况做 /111, 或是/65535处理

mongodb支持两种2d索引:

1) 平面2d索引

2) 球面2d索引（最新特性，距离计算更加准确）

不同的索引在用于地理位置服务时的处理方式不同，具体可以参见：
http://www.tuicool.com/articles/MVrqAn

索引管理
--------

建立索引:

.. code::

    db.ensureIndex({j:1})
    db.ensureIndex({j:1}, {name: "j"})
    db.ensureIndex({j:1}, {background: true})
    db.ensureIndex({j: -1})
    db.ensureIndex({j:1, i: 1})
    db.ensureIndex({j:1, i.j: 1})
    db.ensureIndex({j:1}, {unique: true, dropDups: true})
    db.ensureIndex({j: "2d"}, {'min': -1000, "max": 1000})


查看索引:

.. code::

    db.colletions.getIndexes()
    db.system.indexes.find()

更新索引:

.. code::

    db.collection.reIndex()

删除索引:

.. code::

    db.collection.dropIndexes()
    db.collection.dropIndex()

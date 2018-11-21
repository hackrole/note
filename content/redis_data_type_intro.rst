redis数据结构介绍
=================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-08 14:31:57
:tags: redis
:title: redis数据结构介绍
:summary: redis中string/list/hash/set/sorted-set/bit介绍
:category: programming


概述
----

redis并不是单纯的缓存服务器，而是被设计为一个数据结构服务器。为服务提供有用高效的数据类型.

redis中主要包含如下数据类型:

1) 字符串,二进制安全。
2) 列表list， 链表实现。不是array.
3) 集合set, 值不可重复.
4) 排序集合ordered-set. 同时存储一个value和一个score. score用于排序.
5) 字典hash, 类似python的字典和ruby的hash,但是field-key/field-value只能是字符串.
6) bit-array或bitmaps.
7) HyperLogLogs, 概率行数据结构. **TODO**

不同数据结构可以根据需要解决不同的任务集。

类型具体说明
------------

redis-key
~~~~~~~~~

redis-key只能是字符串，并且是2进制安全。

1) 空字符串也能做为key.
2) 太长的key不被推荐，compare性能不好.
3) 太短的key不好，可读性不好 u1000flw => user:1000:followers
4) 对键做良好的管理，引入命名空间和键前缀等概念. user:1000, comment:1234.replys
5) 最大长度512MB, 不会成为限制。
6) exists判断key是否存在, del用于删除key, keys用于列出keys.type获取key类型.
7) ttl/expire用于获取和设置过期时间. persist移除key的过期设置。pttl/pexpire返回/设置millsecond级别的过期时间.

redis-string
~~~~~~~~~~~~

最简单的数据结构，应该也是最常用的数据结构(缓存).

1) 通过get/set设置和换取

2) set在没有key时会创建key,在key存在时做update.同时可以制定second/millsecond级别的过期时间.

3) 可以支持incr/incrby/decr/decrby，把字符串作为数字执行原子性的+/-.底层使用的是同一个命令。

4) getset获取key的old-value, 同时设置为最新的value.

5) mset/mget一次对多个key做操作.

redis-list
~~~~~~~~~~

列表, 链表实现, 在列表中间插入/移除元素的复杂度为O(1), 查找元素的复杂度为O(N).

1) 大多数操作都支持左右两个方向， lpush/rpush. l->list前缀/r->reverse-order

2) 两个方向的push/pop可以作为队列/栈使用. lrange用于获取列表内容.常用的场景: 

   A) 任务队列.

   B) 返回最新内容.

3) ltrim用于截断list, 可以用来做mongodb的固定长度集合。不过需要自己手动调用.

4) 可用做堵塞队列(celery的实现依赖). brpop/blpop

   A) 可以监听多个list

   B) 可指定一个超时.

   C) 任务推送有顺序.

   D) brpoplpush/rpoplpush **TODO**

5) llen用于返回列表长度.

redis-hash
~~~~~~~~~~

redis上的hash实现,field/value只能是string.

1) hset/hget用于设置和获取field. 一次只能设置一个field.

2) hmset/hmget可用于处理多field.

3) hincrby用于递增.

主要用处:

1) 讲一系列key-value关联到一起。

2) 内存的利用率比多key-value更高, **XXX**.

redis-set
~~~~~~~~~

集合, 支持并集/交集，判断元素是否在操作.

1) sadd用于添加

2) smembers用于列出所有元素

3) sismember 判断元素是否已存在

4) **TODO**

redis-sorted-set
~~~~~~~~~~~~~~~~

排序列表, 不是按插入顺序而是人为自定的score来拍寻。底层使用的是复合机构实现.

1) zadd用于添加

2) zrange用于获取列表

3) 大多数命令都可以添加withscore,来返回score

4) **TODO** zrangebyscore/zrangebylex

redis-bitmaps
~~~~~~~~~~~~~

**TODO**

redis-HyperLogLogs
~~~~~~~~~~~~~~~~~~

**TODO**

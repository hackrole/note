redis复制配置相关
=================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-08 14:31:05
:tags: redis, redis_slave


原内容来自redis官方文档::

    redis-replication官方文档<http://redis.io/topics/replication>

基本来说，只要在配置文件里加上::

    slaveof <ip> <port>

就可以完成配置.

如下配置可能有用::

    repl-diskless-sync (不使用磁盘同步)
    repl-diskless-sync-delay (同步前的延时, 以等待其他的要链接的slave)


安全问题
--------

如果redis开启复制特性，同时master节点关闭持久化特性。
这时应该避免master节点的自动重启，避免slave节点上的数据被重启的master节点清空。


同步策略
--------

redis默认使用磁盘同步, 数据被存到RDB file文件, 之后通过同步该文件做full-sync.

但是如果磁盘太慢会导致性能不好，2.8新增直接通过socket来同步的方式.(该方式目前仍然是实验阶段)

只读复制
--------

redis默认slave是只读的,所有写操作会报错.
通过如下方式可以打开读写::

    slave-read-only no (配置文件)
    config set slave-read-only no (redis-cli运行时)


即便是只读slave也不应该暴露在公网下.
debug/config等命令仍会带来完全问题(使用rename-command配置)

读写slave在较少场景下会有用。未来redis有可能移除该特性.


认证
----

redis很快，所以需要设置足够强的密码，不然会很容易被破解。

master节点可以通过配置，要求所有链接需要认证::

    requirepass <password>

这时slave节点需要做如下配置::

    config set masterauth <password> (运行时)
    masterauth <password> (配置文件)


部分同步
--------

.. TODO:


控制slave链接数
---------------

.. TODO:

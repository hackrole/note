redis sentinel(redis监控)
=========================
author: hackrole
email: daipeng123456@gmail.com
date: 2015-12-31
tags: redis,redis-sentinel,high-avaliable
title: redis高可用监控sentinel配置和使用
summary: 如何通过配置sentinel实现redis集群高可用 

sentinel功能
------------

1) 监控集群中所有节点是否正常工作.

2) 在任一节点fail, 可以通过api通知管理员或pramgram

3) 自动故障转移， 如果一个master节点fail, 会自动把slaver节点提升为master节点.并通知client使用新的节点.

4) 配置提供， client通过链接sentinel获取所有节点信息等。相当与是proxy的作用, 类似mogos

5) 提供redis高可用性

sentinel分布式特性
------------------

sentinel天生具有分布式特性，sentinel被设计为使用多个sentinel进程协同合作。

这样做有以下好处:

1) 由多台sential做fail判断, 减少误判。

2) 避免sentinel单点故障。

快速试用
--------

sentinel当前稳定版本是2, 在redis2.8/redis3.0上工作.
早先的sentinel 1 在redis2.6上工作，已被depressed.

sentinel使用更好的预测算法重写而成。


使用如下方式启动sentinel::

    1) redis-sentinel sentinel.conf

    2) redis-server sentinel.conf --sentinel


sentinel默认使用 26379端口监听client和其他sentinel链接。确保打开这一端口。并正确设置防火墙.

sentinel部署须知
~~~~~~~~~~~~~~~~

1) 一个稳健的redis集群，应该使用至少三个sentinel实例，并且保证讲这些实例放到不同的机器上，甚至不同的物理区域。

2) sentinel无法保证强一致性, 大概分布式环境都会有这方面的权衡.

3) 确保client库支持sentinel.

4) sentinel需要通过不断的测试和观察，才能保证高可用。

5) sentinel配合docker使用时，要注意端口映射带来的影响.


sentinel配置
------------

实例如下::

    sentinel monitor mymaster 127.0.0.1 6379 2
    sentinel down-after-milliseconds mymaster 60000
    sentinel failover-timeout mymaster 180000
    sentinel parallel-syncs mymaster 1

    sentinel monitor resque 192.168.1.3 6380 4
    sentinel down-after-milliseconds resque 10000
    sentinel failover-timeout resque 180000
    sentinel parallel-syncs resque 5


只需指定master节点信息, slave节点是自动发现的.
sentinel会在运行时修改这个配置文件.

每个master节点需单独指定。为每个master节点指定一个特定的master-name

配置详解
--------

主要配置::

    sentinel monitor <master-group-name> <ip> <port> <quorum>

quorun指定fail的界限。
比如有5个sentinel实例，quorun为2. 则只要有两个sentinel认为该节点不可用。
则两个sentinel中会有一个发起failover, 只有大多数sentinel(3个以上)都同意failover的情况下,
failover才会实施


其他配置都有如下格式::

    sentinel <option_name> <master_name> <option_value>


所有的配置都可以在运行时通过 +sentinel set+ 修改.

部署exmaple
-----------

参见官网文档，不好整理。

1) 避免脑裂

2) 使用如下配置避免master节点失败后的数据丢失::

    min-slaves-to-write 1
    min-slaves-max-lag 10

快速教程
--------

配置好sentinel后，可通过如下命令查看sentinel状态::

    sentinel master mymaster
    SENTINEL slaves mymaster
    SENTINEL sentinels mymaster
    SENTINEL get-master-addr-by-name mymaster

可以使用如下命令模拟redis失败， 观察fallover过程::

    1) redis-cli -p 6379 DEBUG sleep 30

    或

    2) 直接停掉master节点

sentinel API
------------

可以通过通过sentinel提供的api获取相关通知.

有两种方式::

    1) 使用sentinel提供的命令获取最新的状态(http方式)

    2) 基于pub/sub模式获取实时通知

相关命令整理
~~~~~~~~~~~~

::

    PING 
    SENTINEL masters
    SENTINEL master <master name>
    SENTINEL slaves <master name>
    SENTINEL sentinels <master name>
    SENTINEL get-master-addr-by-name <master name> 
    SENTINEL reset <pattern> 
    SENTINEL failover <master name>
    SENTINEL ckquorum <master name>
    SENTINEL flushconfig 

    SENTINEL MONITOR <name> <ip> <port> <quorum>
    SENTINEL REMOVE <name>
    SENTINEL SET <name> <option> <value>


.. TODO:

    其他

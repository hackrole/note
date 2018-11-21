redis集群教程
=============

:title: redis集群教程整理
:tags: redis,cluster
:author: hackrole
:date: 2015-12-30
:category: programming

redis集群相关内容, 讲解如何设置集群，对集群做测试和常规操作。
不涵盖redis集群的细节，只从用户的角度讲如何使用redis集群, 以及redis的高可用性和一致性相关内容。
更具体内容参见::

    http://redis.io/topics/cluster-spec

redis集群的作用
---------------

1) 自动把数据分布到多台redis实例上.

2) 再部分节点失败后，保持可用性。再大多数redis节点失败后,redis集群仍然会失败.


redis集群tcp端口
----------------

redis集群需要所有节点开启两个端口.

1) normal-port. 如6379. 用于客户端的请求处理。

2) high-port(normal-port+10000). 如16379.
   用于集群内节点间使用2进制协议交换数据，
   同时完成节点的错误检测，配置更新，故障转移认证等.

确定开启这两个端口，并正确的设置防火墙。不然集群可以无法正常工作.

redis集群与docker
-----------------

redis集群无法的NAT网络下使用。

配合docker使用时，需要开启docker host-networking-mode. 具体参见docker相关文档。


redis集群数据共享方式
---------------------

redis集群不是通过一致性hash实现. 而且通过hash-slot概念实现(hash槽)
hash槽实现方式: CRC16(key) % 16384. 所以redis集群最多只能包含16384个实例。
每个redis实例都是复制一部分hash槽。如A: 1-5500. B: 5501-11000
这样的实现方式的好处是可以方便的增加和删除节点。只需将对应的槽做移动

如果一个操作涉及多个key, 只要这些key再同一个hash槽中，redis集群允许这类multi-key操作.
可以通过hash-tag的概念强制一系列键保存到同一个hash槽中。

hash-tag概念, 如果一个key里包含{tag}, 则只是用tag来做hash, 以此保证数据被hash到相同的槽中。
如: foo{bar} never{bar}


redis集群的主从模式
-------------------

redis的分片配置redis主从复制， 来保证高可用性。


数据一致性
----------

redis集群没法保证数据的一致性。再特定的场景下,redis会丢失部分数据.
主要原因在于redis的异步同步的方式上。这是在性能和一致性上的权衡.

还要注意处理集群分裂的问题. 如一个6节点的集群分裂为两个3节点集群，然后各自工作
导致两边数据不同步的问题.


redis集群配置
-------------

配置参数
~~~~~~~~

.. _TODO:

    pass

cluster-enabled <yes/no>

cluster-config-file <filename>. 用于保存集群状态和节点信息，由集群自动更新。

cluster-node-timeout <milliseconds> 超时时间，超时后认为节点不再可用.

cluster-slave-validity-factor <factor>

cluster-migration-barrier <count>

cluster-require-full-coverage <yes/no>

创建和使用redis集群
~~~~~~~~~~~~~~~~~~~

一般都需要安装ruby的redis包::

    gem install redis

如果是测试可以使用redis下提供的命令，快速启动集群做测试.如下::

    1) cd <reids>/utils/utils/create-cluster/

    2) read the readme and gem install redis.

    3) ./create-cluster start

    4) ./create-cluster create.

    5) test it now.

    6) ./create-cluster stop && ./create-cluster clean


当然最好是自己配置集群环境，这样能学到更多东西, 如下::

    1) mkdir cluster-test
       cd cluster-test
       mkdir 7000 7001 7002 7003 7004 7005

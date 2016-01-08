redis服务管理需要
=================


介绍一些redis部署时的注意事项

注意事项
--------

1) 建议使用linux部署。

2) sysctl vm.overcommit_memory=1 或者 vm.overcommit_memory = 1 (/etc/sysctl.conf)

3) echo never > /sys/kernel/mm/transparent_hugepage/enabled

4) 设置一个和内存一样大或更大的swap分区，不然redis有可能在内存不足时被系统杀死。

5) 设置一个明确的maxmemory. 这样redis会在内存到限后抛出错误，而不会falling.

6) 在写比较重的场景下需要有大约2倍于normal的内存。这些是来在内存中保留那些需要被写回磁盘的数据.

7) 配置supervisor类工具时，设置 daemonize no

8) 开启slave特性时，即便不使用持久化特性,redis也会perform RDB save. 除非使用实验性的diskless-sync.

9) 开启slaev特性时，要确保要么开发master节点的保存特性，要么关闭master节点的自动重启。

10) 注意开发redis安全相关配置. require-pass/rewrite-command/bind-ip

aws注意事项
-----------

1) 使用HWS实例，不要使用pv实例

2) 不要使用太老的实例。 m3 good than m1

3) redis在EBS的持久话需要注意，EBS可能会太慢。

4) 你可能想尝试diskless-sync. 如果replication-sync有问题的话。

redis升级或重启建议
-------------------

.. TODO:

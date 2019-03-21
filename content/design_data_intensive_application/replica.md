Title: design data-intension application: replica
Date: 2019-03-21
Category: programming
Tags: 
Author: hackrole
Email: hack.role@gmail.com
Status: draft


# replica复制

## word concept

### eventual consistency

最终一致性

### read-your-write

写后读

用户写入主库,读取未同步的从库


### monotonic read

单调读

多次读取使用不同的replica, 导致上次读到的内容在下次未同步完成

### 一致前缀读

多个读取来自不同的replica,导致处于后面的数据比前面的数据先出现
一般分片环境

### 版本向量

## replica algorithm

1) single leader

2) multi leader

3) leaderless


## synchronously vs asynchronously
同步与异步

完全同步replica会导致节点写入延迟高,容易失败.

完全异步写入有可能导致数据丢失,会读取的旧数据等数据不一致问题


## add new replica

基于某一时间快照和快照对应的binlog的偏移位置


## replica log

1) 基于语句

非确定函数等会导致数据不一致

2) 基于行(逻辑日志)

mysql新版使用这种方式


## 多主复制

### 冲突解决

### 拓扑结构


## ??
w + r > n


## TODO

[eventually consistent](https://queue.acm.org/detail.cfm?id=1466448)

[mysql-internals-manual](https://dev.mysql.com/doc/internals/en/)
[mysql-inline](https://www.percona.com/live/mysql-conference-2013)

[clock are bad, welcome to distrubuted system](http://basho.com/posts/technical/clocks-are-bad-or-welcome-to-distributed-systems/)

[eventually consistent detecting](http://messagepassing.blogspot.com/2011/10/eventual-consistency-detecting.html)

[if you must deploy multi-master replication](http://scale-out-blog.blogspot.com/2012/04/if-you-must-deploy-multi-master.html)

[kafka replica](https://www.slideshare.net/junrao/kafka-replication-apachecon2013)

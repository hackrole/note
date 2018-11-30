# partition or shared

## word concept

### data skew(数据偏斜)/hot_sport(热点)

数据分片不平衡,部分分片数据和负载过大.

高负载分片被称为热点

### consistent hashing(一致性hash)


### gossip protocol(流言协议)


## shared method


1) key-range shared

容易存在热点

2) key-hash shared

range-query in key-hash-shared must send to all shareds

3) consistent-hash shared(hash and range)

## 二级索引


## share route

1) Round-Robin Load Balancer: 服务器内部自动路由到正确位置,客户端透明

2) 路由层(mongos)

3) 完全在客户端实现(ruby redis client)


## TODO

[a fast, mini-memory consistent hash algorithm](https://arxiv.org/pdf/1406.2294v1.pdf)

[consistent hash random tree](https://www.akamai.com/us/en/multimedia/documents/technical-publication/consistent-hashing-and-random-trees-distributed-caching-protocols-for-relieving-hot-spots-on-the-world-wide-web-technical-publication.pdf)

[service discovery in cloud](http://jasonwilder.com/blog/2014/02/04/service-discovery-in-the-cloud/)

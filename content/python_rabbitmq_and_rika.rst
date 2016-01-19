rabbitmq和python-rika库入门
===========================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2014-07-10 17:07:40
:tags: python, rabbitmq, rika
:status: draft


**TODO** this note is not finish

rabbitmq 概念
-------------

:queue 队列: 很像一个先入先出的队列结构， 负责实际存储和传递 消息.

:exchange 转发器: 一般发送者不应该直接将消息压入消息队列中，
                  而应该转由转发器来替你完成消息的发送。
                  分为四种类型

    A) 默认值/direct

    B) headers

    C) topic

    D) fanout(群发)

:routing_key: 用于实现queue对exhange消息的过滤和选择, 不同的转发器对应不同的解释

    A) fanout会直接忽略该参数

    B) direct用此实现多发(群发，过滤)

:publish/consume: 发消息/收消息, 注意收消息会使程序进入无限堵塞，
                  为了可以配合tornado等使用，实现注意ioloop的设置

:basic/ctx: **TODO**

:connection: **TODO**

:channel: **TODO**

rabbitmq-server使用
-------------------

rabbitmqctl
~~~~~~~~~~~

+ list_queues
+ list_exchange
+ list...

pika库
------


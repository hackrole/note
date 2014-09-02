public: yes
tags: [数据库]
summary: |
    在数据库建模阶段，如何做布尔状态值和整型状态值之间作出选择

布尔还是整型状态
================

写在前面的话
------------

做后端开发3年了，后端的大头说白的就是一个数据库。所以每天都在与数据库打交道。
从业之处，那管你什么表结构，需要功能就加表加字段，要性能就做冗余或是缓存。
也算勉强混过了几个年头。表建的太多了，就会发现很多的表都有相似的结构，也有很多相似的考量方案。

其中一个比较常见的就是在选择数据状态位时，是选择多个bool_if值控制还是一个int_status值。

本文大量使用了 **表** 这一词,此处不单单指SQL数据库. nosql数据库,甚至是内存对象，类对象也应该有相似的处理。

布尔还是整型?
-------------

布尔和整型status的区别, **就是布尔只能是true/false,而整形一般可以是任意一个整数，当然没人会整出那么多状态的结构，一般都会再3-5,或是5-10之间**


布尔例子::

    if_live = BooleanField(help_text=u"是否还没死")
    if_gold = BooleanField(help_text=u"是否是金子做的")

整形例子::

    CHOICES = {
        'dead': -1, # 禁用
        'normal': 0, # 正常
        'closed': 1, # 关闭

    }
    status = IntField(choices=CHOICES, help_text=u"状态")

从上面可以看出两者最大的区别在于:

1) 互斥性

整形状态值具有互斥性(你只能设置一个状态值).
而多个布尔型之间就没这种特性，比如::

    # bool
    if_finish = BooleanField(help_text=u"是否是正式用户")
    if_gold = BooleanField(help_text=u"是否是黄金用户")

    # int
    CHOICES = {
        'not_finish': -1,  # 非正式用户
        'finish': 0,  # 正式用户
        'gold': 1,  # 黄金用户
    }
    user_status = IntField(choices=CHOICES, help_text=u"用户状态")

用户当然必须是正式用户才能是黄金用户.

但是bool的例子中数据结构中确实有可能使一个用户在成为正式用户前，变身黄金用户。
当然你可以通过代码的方式来控制这种逻辑，随着而来的就是代码的硬逻辑和维护负担。

反观int的例子就很好的解决了这个问题。

2) 多状态的记忆性

整形状态值一旦被重新设置后就会丢失之前的状态。
而多个布尔值的状态变化不会出现这种情况, 比如::

    # bool
    if_close = BooleanField(help_text=u"是否被禁用")
    if_gold = BooleanField(help_text=u"是否是黄金用户")

    # int
    CHOICES = {
        'closed': -1,  # 禁用
        'normal': 0,  # 普通用户
        'gold': 1,  # 黄金用户
    }
    user_status = IntField(choices=CHOICES, help_text=u"用户状态")

假若现在临时禁用一个用户，之后有取消禁用。
bool的例子没有问题，设置下is_close就好了。
int的例子有个问题，没法判断一个被禁用的用户之前是普通用户还是黄金用户, 之前的状态丢失了。

实践策略
--------

再设计表结构的状态位时，基本的考量也就是考虑在状态互斥和记忆性。
1) 允许一个非正式用户成为黄金用户，当然不能算一个好的数据结构设计。
2) 一旦禁用就不能返回以前状态当然更加糟糕。

除此之外，还有一些其他的方面需要考虑。
1) bool型字段应该在逻辑允许的情况下尽量少，但是前提是满足逻辑以及可以考虑的扩展的要求。

原因很简单, 当一个表结构中bool字段太多，那你可能就会有下面这样查询语句的对比::
    # bool
    user.objects(is_close=False, is_gold=True, is_finish=True,....)

    # int
    user.objects(status=CHOICES['gold'])

选择一目了然.

2) int型字段应该做好顺序的设置，这种顺序有时会发挥很好的副作用::

    # int 1
    CHOICES = {
        'normal': -2,  # 普通用户
        'closed': -1,  # 禁用
        'gold': 1,  # 黄金用户
    }
    status = IntField(choices=CHOICES, help_text=u"用户状态")

    # int 2
    CHOICES = {
        'closed': -1,  # 禁用
        'normal': 0,  # 普通用户
        'gold': 1,  # 黄金用户
    }
    status = IntField(choices=CHOICES, help_text=u"用户状态")

    # 查询正常或黄金用户
    # int 1
    user.objects(status__in=[CHOICES['normal'], CHOICES['gold']])
    # int 2
    user.objects(status__gte=CHOICES['normal']) 

3) 设计即多选一
一般的策略是一个int_status配合几个bool型做状态处理。
但是很多时候,尤其是状态位较多的情况，会出现的一个问题是如何做int型和bool型间做平衡。
应该设置几个bool型，那些应该放到bool型中，那些应该放到int型中，这些考量当然必须首先满足逻辑要求。
之后如果仍有多个选项，则可能要靠个人的经验和品味。

扩展思考
--------

bits/string状态位。
~~~~~~~~~~~~~~~~~~~

相信不少朋友碰到过这样的设计::
    # string
    status = "11" # 第一位if_close, 第二位if_gold
    # bits
    status = 4 # 2进制位控制，（00, 01, 11, 10)

现在在楼主看来这样的设计很糟糕.

1) 这中设计根本上就是无非把多个bool位合并成一个，带来的结果
   1) 设计结构可读性差。
   2) 可扩展和可维护性差(多状态被硬编码在一起)。
   3) 查询不便，必须手动拼接status值，甚至做位运算。
   4) 要说多省存储空间吧，也不见得。

2) 延伸的思考就是int型某种意义上来说也是多个bool合并的结构，但是很大的差别在于, 不会对int值做某种硬性规定.

一方面将int与原先的多个bool之间做了解耦合，解决了扩展性和可维护的问题.
另一方面，允许设计者对int值做自己的选择,一定程度上能解决可读性，和查询不变的问题。
存储的问题是最次要的问题，甚至不应该考虑.因为太便宜了。

其他可选方案
~~~~~~~~~~~~

1) int型状态位结合，status change_log(状态机模式), 解决记忆性问题

2) 多个bool型配合分表。

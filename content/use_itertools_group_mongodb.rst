使用python itertools库来取代mongodb的group分组操作.
===================================================
:author: hackrole
:email: daipeng123456@gmail.com
:date: 2015-06-09 15:40:50
:tags: python, mongodb
:category: programming


最近写项目用到mongodb数据库。后续要做后台管理的时候，有一个需要按（天/人）做聚合的需求(group_by)。

最开始实现上用bson.code.Code配置mongodb自带的group命令做的。不过问题很多。

使用group命令的问题
-------------------

1) 必须在python里混合编写js函数。

2) 调试起来及其麻烦, 真心麻烦。

3) 可扩展可维护行差，今天想按天，明天突然有想按月，或者就是要增加聚合字段或是修改聚合算法的规则。

使用python的itertools实现
-------------------------

后来也是和一朋友讨论后，决定用python itertools来实现.

总的思路就是把数据先查出来，然后在python里自己做聚合.
正好可以配合itertools提供的轮子简化下过程.

好处
~~~~

1) 只用写python代码, 避免混和js的麻烦.

2) 调试方便.

3) 写单元测试也方便很多，不在需要依赖外部的mongodb数据库.

4) 可扩展和可维护行好了很多，因为全是python集合的操作，看着改就可以了。

坏处或可能的问题
~~~~~~~~~~~~~~~~

1) 内存有可能会出问题.
一次查处所有数据，在内存在分组。并且使用python，内存一定要考虑下。

2) mongodb一次查处所有数据遍历有可能碰到的游标中断，数据量太大导致mongodb抛出异常
虽然mongodb有游标的概念, 不过不太确定游标能否正确遍历大数据集合。会不会被异常中断

3) 性能会相对差一些，不过由于后台不是频繁跑，而且对速度要其也不是太高，所以不算大问题.

大致思路
--------

1) 使用itertools.groupby把列表转化为 k-> groups(list)格式的字典.

2) 使用两层循环做聚合操作，第二层循环可以考虑使用reduce/map函数处理.

3) 最后要记得对结果做排序，使用sorted排序，OrderedDict来保存排序结果。

可能可以考虑的优化
------------------

1) 使用分页遍历防止游标中断或是数据过大的异常.
需要查看groupby是否支持，或能否使用其他方式处理

2) 如果不是实时的需要显示, 如更新用户的服务书好评率等。可以考虑不使用groupby, 改为居于双层循环的来处理.

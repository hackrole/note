mongodb与第一范式
=================

:tags: mongodb,SQL
:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-08
:category: programming



mongodb作为一个弱模型化的nosql数据库，被认为是不需要遵守SQL第一范式.
但是这样的想法其实应该是错误的.

what's 1NF
----------

第一范式, 一句话概括的话就是原子域约束.
SQL中一个字段(column)里应该只存储不可在分(原子)的值。

比如, A有5个号码. 我把5个号码连接起来存到一个字段，那就不是1NF.
因为这个值是可分的，能被分成5个号码.而这5个号码应该存为5条记录.

why mongodb not 1NF
-------------------

mongodb作为文档数据库，对数据模式要求很宽松.记录不必保持一直的模式.
缺失字段和字段类型不同都可以.

比如: A只有一个数据号，所以存为mobile: '<mobile>'. B有2个号码，所以存为 mobile: ['<m1>', '<m2>']
当然这里与1NF完全无关系。略过。

其次mongodb允许为字段存为列表和内嵌文档。如果一个字段里存了5个手机号的列表。是否明显违背了1NF


why mongodb is 1Nf
------------------

现在想想下 A姓名 王某某, 原子域,满足1NF.
然后来了新的需求, 必须拆分用户的姓和名，那上面明显又违背了1NF.

是否满足1NF更多的是看使用场景和我们的模型构建.
并且最重要的是所有的范式其目的都是为了指导我们设计出好的模型.

mongodb虽然灵活，但是也不应该乱用，比如把用户和姓名和电话存在一个数组里.
内嵌文档通常也不会将将用户的网银密码和博客站点的评论村到一起.

事实上，大多时候我们只会往数组里存放同一类数据，比较手机或是姓名或内嵌文档.

所以mongodb仍然是遵守1NF, 看你着眼的视角。
事实上1MF是要指导你良好的划分子域

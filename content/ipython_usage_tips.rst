ipython使用技巧
===============

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-19 17:18:33
:status: draft
:tags: python, ipython, tools


内容参考: 来自 **TODO**

调用timeit做性能测试
---------------------

%timeit range(10000)

ipython里run代码
----------------

在ipython里调用 `%run program`
跑程序,程序每次都会执行, 参数如下: **TODO**

ipython里load代码
-----------------

%load根据路径加载文件

debug调试代码
-------------

1) 在出异常后,调用 %debug进入pdb开始调试程序

2) 调用%pdb,在出异常时.会自动进入pdb调试

TODO ipython历史
----------------

TODO ipython代码宏
------------------

TODO ipython配置文件
--------------------

TODO 启动脚本文件
-----------------

调用ipython -i <pyfile> 在加载脚本文件后在启动ipython

在profile_default/startup目录下放置的脚本文件会依次在ipython启动前加载

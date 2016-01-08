http协议与restful-api设计
=========================
:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-08 15:25:47
:tags: http, restful, api

http简介
--------

http请求过程
~~~~~~~~~~~~

1) 基于tcp3次握手

2) 发送http请求获取http响应

3) 断链接

http基本概念
~~~~~~~~~~~~

URI identify
""""""""""""

1) URL location

   a) 方案

   b) 用户

   c) 密码

   d) 主机

   e) 断后

   f) 路径

   g) 参数

   h) 查询

   i) 片段

2) URN name 未流行

http方法
""""""""

1) GET

2) POST

3) delete

4) PUT

5) head

6) options

7) trace

8) patch

webDev扩展
''''''''''

lock/copy/move

http状态
""""""""

1) 100/101-> procotol update

2) 200 ok/201 created/202 accept/204 not content

3) 300错选/301永久move/302 303 307临时move/304 not modify

4) 400bad request/401not auth/403 forbidenn/404 not found/405 method not allow/410 gone

5) 500 error/501 not implement/502bad gate/503 service unable/504 timeout

http首部
""""""""

1) content-type

2) etags

3) expires

4) if-modify-since

5) location

6) authuration

7) set-cookies

http组件
""""""""

1) 代理

2) 缓存

3) 网关

4) 隧道

http版本 rfc
""""""""""""

1) 0.9

2) 1.0

3) 1.1

4) NG(2.0)未流行

rest概念
--------

可见性
~~~~~~

1) 无状态

2) 统一接口

3) 媒体类型

安全方法／幂等方法
~~~~~~~~~~~~~~~~~~

设置资源url
~~~~~~~~~~~

1) 识别资源

2) 资源粒度

3) 复合资源

4) 计算资源

链通性
~~~~~~

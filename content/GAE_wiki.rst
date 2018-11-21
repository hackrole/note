GAE碰到的小问题
===============

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2013-10-03 15:13:41
:status: draft
:tags: GAE
:category: programming

url匹配失败问题
---------------

在app.yaml中配置的url使用的是正则表达式,而不是通配符的形式,
所以要使用.* 代替 *

request method not allowed问题 :webapp2:
----------------------------------------

webapp2的get/post对应相应的http请求,
注意大小写和缩进问题

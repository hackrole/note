chrome extension开发tips
========================
:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-28 09:40:38
:status: draft
:tags:  chrome
:category: programming

localstorage
------------

extension可以通过html5新增的localstorage来存储数据。

localstoage有不少限制:

1) 类似cookie的域限制, 不同域的在javascript不能访问其他域数据

2) 只能存储字符串, 列表字典等需要先序列化.

3) 默认有个存储容量限制，大小5MB. 可以通过在manifest.json的permisses里指定unlimitStorage突破这一限制。

content_scirpt限制
------------------

chrome的大部分API在content-scripts下不可使用.

页面间通信的api可以使用.

.. code-block:: javascript

   // send message.
   // 制定exntesionid, 可以在扩展之间实现通信
   // 问题是extesionid都是随机生成的，如何获取其他扩展的extensionid??
   chrome.runtime.sendMessage(extensionid, message, options, callback)

   // listen message
   chrome.runtime.onMessage.addListener(callback)

chrome存储数据
--------------

chrome下有三种数据存储方式.

1) html5的localStorage. key-value存储.

2) chrome提供的存储API. 异步存储, 文档型存储.

3) web sql database. sql表.

chrome存储API
-------------
**TODO**

web sql database相关
--------------------

详细内容可以参考: https://www.w3.org/TR/webdatabase/

原生的API并不好用，可以考虑 https://github.com/KenCorbettJr/html5sql

数据是明文存储到本地。 如果是敏感数据，要考虑对数据做加密.

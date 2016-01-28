chrome extension开发tips
========================
:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-28 09:40:38
:status: draft
:tags: chrome, chrome-extension

localstorage
------------

extension可以通过html5新增的localstorage来存储数据。

localstoage有不少限制:

1) 类似cookie的域限制, 不同域的在javascript不能访问其他域数据

2) 只能存储字符串, 列表字典等需要先序列化.

3) 默认有个存储容量限制，大小5MB. 可以通过在manifest.json的permisses里指定unlimitStorage突破这一限制。


chrome extension调试
====================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-19 15:44:33
:status: draft
:tags: chrome, chrome-extension

调试须知
--------

1) 确保打开develop-mode, 然后正确的load本地开发中的extension.

2) 在extension管理页面可以看到, extension_id, 之后使用chrome-extension://<extension_id>/<filename>可以打开并调试对应文件.

3) 在extension的browser-action图标上右键选择inspect-popup也可以打开调试界面，之后要设置断点并reload页面.

4) 可以使用console.log/console.error接口来做简单的打印调试.

5) 修改extension后要正确的reload extension

6) 使用console.table可以输出更好用的调试数据，在处理列表字典时有用。

参考链接
--------

**TODO**

https://developer.chrome.com/extensions/tut_debugging
https://developers.google.com/web/tools/chrome-devtools/

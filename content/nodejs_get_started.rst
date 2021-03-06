nodejs入门
==========

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2014-01-06 16:01:57
:status: draft
:tags: nodejs, node
:category: programming

简介
----

nodejs适合做多人游戏,实时系统,联网软件，高并发应用

异步io与事件驱动
~~~~~~~~~~~~~~~~

CommonJS规范
~~~~~~~~~~~~

安装配置
--------

快速安装与编译安装
~~~~~~~~~~~~~~~~~~

node包管理安装npm
~~~~~~~~~~~~~~~~~

多版本管理nvm
~~~~~~~~~~~~~

快速入门
--------

入门
~~~~

安装supervisor，nodejs服务器支持自动重载，方便调试web应用
使用方式:
npm install -g supervisor
supervisor app.js

nodejs单线程不能利用cpu多核特性，需要时候cluster等方式提供这一支持

异步变成方式不符合传统思维，有不好解决这类问题的库,
如async/streamlingjs/jscex/eventproxy

模块与包
~~~~~~~~

模块与包
""""""""

模块的required与exports/modele.exports

**TODO** 包与package.json

**TODO** nodejs模块加载机制


npm使用
-------

本地与全局安装.

install/link/init/publish/unpublish

调试
----

1) node debug <script.js>
2) 远程调试: node --debug[=port] <script.js> / node --debug-brk[=port] <script.js>.默认5858端口

使用node-inspector调试(基于浏览器?). ``npm install -g node-inspector``

核心模块
--------

全局对象global
console/process
process描述当前node进程状态，是node与操作系统的简单接口

console
console.log()
console.error()
console.trace()输出调用栈

util常用函数

events事件驱动
EventEmitter.on注册事件
EventEmitter.emit触发事件
.once单次事件注册
removeListener移除指定的事件处理函数
removeAllListers移除所有事件处理函数

error是特殊时间，error触发时如果没有处理函数，则抛出异常.

fs文件系统
所有操作都有异步和同步两个版本

http模块
http.Server服务器对象
createServer
request/response对象

服务器事件:
1) request
2) connection
3) close

http客户端
http.request
http.get

Express框架与web开发

ejs模板语法简介
layout使用, render设置layout属性
模板中用partial()函数加载其他功能试图模块，类似yii的那个？

视图助手
静态
通过app.helpers()注册
动态
通过app.dynamicHelper()注册,必须为函数，函数只能有req/res两个参数

nodejs进阶
----------

模块加载机制
加载只加载一次，重复required不会多次执行模块代码

控制流

循环与异步之间的陷阱
使用foreach处理

回调函数在深层嵌套时代码可读行差，维护困难，代码耦合高
要想办法改善设计，考虑使用异步转同步库

应用部署
cluster模块多进程启动
nginx反向代理
日志开启
启动脚本

nodejs缺点与不适用
计算密集型
单用户多任务
逻辑复杂
unicode与国际化缺陷

nodejs编码规范
--------------

http://nodeguid.com/style.html

+ 两个空格缩进
+ 80字符限制
+ ;换行
+ 永远使用var定义变量，建议绝不使用全局变量
+ 变量/函数用陀峰(考虑_命名方式?)
+ 建议尽量使用单引号，避免json/xml的双引号问题
+ 尽量使用===来做比较
+ 避免复杂继承/多集成，尽量使用utils.inherits函数

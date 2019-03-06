golang入门
==========

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2014-04-21 15:17:04
:status: draft
:tags: golang
:category: programming

golang特点
----------

+ 编译迅速

+ 依赖分析容易,避免c风格的include库与代码分离问题

+ 编译型静态类型语言

+ 类型没有层级,轻量级面向对象

+ 垃圾回收

+ 并行和通信的基本支持

+ 多核支持

安装
----

源码编译
~~~~~~~~~~~

标准包安装apt-get
~~~~~~~~~~~~~~~~~

GVM多版本管理安装
~~~~~~~~~~~~~~~~~

环境配置??
----------

应用程序目录结构
~~~~~~~~~~~~~~~~

1. src 存放源码

2. pkg 编译后的库文件

3. bin 编译后的可执行文件

包管理
~~~~~~

src目录下,相应的包名(目录下),文件开头
package ''(main为可执行文件)

编译应用
~~~~~~~~

go install

编译demo
~~~~~~~~

**TODO**

go命令
------

build
~~~~~

1. 如果是普通包,不生成库文件,需要go install

2. 如果是main包, 在当前目录生成可执行文件,-o或go install安装倒其他目录

3. 默认编译目录下所有文件,指定文件名来只编译一个

4. 忽略目录下 _或. 开头的文件

5. 对不同系统只编译文件名后带有系统名的文件 golinux.go/gowindows.go/gofreebsd.go

clean
~~~~~

清除编译的文件,方便提交源码包

get
~~~

获取远程包,先下载源码包,然后执行go install.
支持github/BitBucket/google code/lanchpad.
需要有git/svn/mercurial等工具支持

fmt
~~~

go fmt -w file
用于格式话go文件,一般的编辑器自带保存格式化功能.

go install??
~~~~~~~~~~~~

第一步生成结果文件(可执行文件/库文件)
第二步把结果文件移到$GOPATH/bin, $GOPATH/pkg目录

go test
~~~~~~~

编译src目录下*_test.go,并运行
go help testflag

godoc
~~~~~

查看go语言文档(入门指引/reference等)

参数
""""

-src 查看源码
--htpp=:8080 打开web支持

go help
~~~~~~~

查看go命令帮助

其他
~~~~

1. go fix 老版本代码修复倒新版本
2. go versin 查看go版本
3. go env 查看go环境变量
4. go list 列出安装的package
5. go run 编译并运行go文件 

编辑环境配置
------------

vim 
~~~~

**TODO**

emacs
~~~~~

**TODO**

sublime text2
~~~~~~~~~~~~~

**TODO**


resource
~~~~~~~~~

https://dave.cheney.net/practical-go/presentations/qcon-china.html?utm_campaign=Master%20the%20World%20of%20Golang&utm_medium=email&utm_source=Revue%20newsletter

https://medium.com/@dgryski/idiomatic-go-resources-966535376dba

https://www.ardanlabs.com/blog/2018/08/scheduling-in-go-part2.html?utm_campaign=Master%20the%20World%20of%20Golang&utm_medium=email&utm_source=Revue%20newsletter

eclipse过程忽略，只记录vim/shell过程
====================================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-08 14:43:40
:tags: android, hello world


开始工程
--------

1) android list targets

2) android create project --target <target-id> --name MyFirstApp --path <path-to-workspace>/MyFirstApp --activity MainActivity --package com.example.myfirstapp


重点
~~~~

下载配置android-sdk,配置环境变量
""""""""""""""""""""""""""""""""

**TODO** 熟悉android的命令使用
""""""""""""""""""""""""""""""

1) list

2) create

**TODO** 主配置文件 AndroidManifest.xml
"""""""""""""""""""""""""""""""""""""""

1) 包名/版本号/版本名

2) app名/app图标

3) activity/service/intent配置

4) 最新版本号/目标版本号等

**TODO** ant/gradel编译系统
"""""""""""""""""""""""""""

classpath变量处理??

运行hello world
---------------

1) ant debug

2) adb install bin/MyFirstApp-debug.apk

重点
~~~~

**TODO** adb(android debug bridge) 用于安装调试android app
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

1) 如何查看logcat

android avd 配置andriod虚拟机
"""""""""""""""""""""""""""""""""

用处不大

用户界面
''''''''


1) 用户界面有三种写法, layout_xml是主流方式。便于界面和逻辑分离

   1) layout_xml

   2) java activity setView

   3) 混合

布局方式
~~~~~~~~

**TODO**

界面元素的布局属性
~~~~~~~~~~~~~~~~~~

**TODO**

主题配置问题??
~~~~~~~~~~~~~~~~~


绑定事件，another activity
--------------------------


如何绑定手机事件
~~~~~~~~~~~~~~~~

**TODO**

1) layout xml onClick

2) 代码绑定(内部类/方法)


ntent用于实现activity通信
~~~~~~~~~~~~~~~~~~~~~~~~~


activity生命周期
~~~~~~~~~~~~~~~~


android类库基本的结构和常用类方法等
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**TODO**

vim
~~~

**TODO**

1) auto-import

2) auto-complete

3) syntax checker(libs setttings)



centos常用配置总结
==================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2014-01-03 18:09:49
:status: draft
:tags: centos
:category: tools

网络配置问题
------------

默认无界面的centos安装后没有开启网络链接，需要配置/etc/sysconf/netword-script/eth0网络脚本,
设置开机启动,ip获取方式，网关都信息.

编辑/etc/resolv.conf配置dns域名服务器

/etc/init.d/network restart重启网络应用

如果是虚拟机中，可能需要设置网络链接方式为桥接模式

yum源配置问题
-------------

一般centos可以配置多种源

+ 网络源(/etc/yum.repos.d/CentOS-Base.repo)

+ 本地源(/etc/yum.repos.d/CentOS-Media.repo)

网络源一般配置国内的源可以加快安装速度,可以考虑163源

virbox vs vmware
----------------

virbox免费，
但是使用界面不如vmware,
功能上是否也偏弱
性能据说也会差一些

终端centos使用问题
------------------
**TODO**

远程使用
--------

终端下不能滚屏，不能使用鼠标，C-S-c,C-S-v也无法使用, 使用起来很麻烦.

可以使用ssh登录方式使用centos，可以解决滚屏，复制/粘帖，中文乱码问题

yum使用与apt-get颇为不同
------------------------
**TODO**

有待研究,不知道能否配置使用aptitude

编译安装中文输入法及使用
------------------------

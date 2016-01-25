docker入门
==========

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2015-06-04 14:49:44
:tags: docker, vagrant


docker不久，不过个人感觉docker还是很有用的，有时间要好好研究下。

docker vs Vagrant
-----------------

docker和vagrant感觉上很想，但是差别也很大.

虽然同样是做虚拟相关的东西.

1) vagrant相当与一个虚拟机的命令行管理工具，能快速配置基于vbox/vmware虚拟机环境.提供的是一个完整的虚拟机环境.

2) docker抽象程度更高，系统资源利用率更高，为进程提供一个容器。来减少对外部系统的依赖。也能方便大规模部署等.

除了这一本质上的区别， 两者还有很多的相似之处。

1) 相似的命令行操作。

2) 都支持hug上下载和上传img.

3) 都有类似img/instance之类的概念存在.

docker中的概念
--------------

docker hug
~~~~~~~~~~

类似git-hub，方便用户上传和下载img。

img
~~~

可以认为是docker容器的class对象，封装必要的进程环境，方便必要时快速启动和大规模部署服务.

contain 容器
~~~~~~~~~~~~

进程的执行容器，也是img的运行中实例。

network port
~~~~~~~~~~~~

docker一般将contain内容的端口映射到一个外部主机端口，这样才能通过网络访问容器内的网络服务.

docker命令
----------

docker ps
~~~~~~~~~

docker build
~~~~~~~~~~~~

docker run
~~~~~~~~~~

docker logs
~~~~~~~~~~~


docker最佳实践
--------------

1) 一个contain/img只做一件事，只封装一个进程需要的执行环境.

2) img中不应该封装不需要的库或环境.

3) 使用docker hug来保存在利用img

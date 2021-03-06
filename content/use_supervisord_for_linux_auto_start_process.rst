使用supvisord取代linux默认开机启动项
====================================
:author: hackrole
:email: daipeng123456@gmail.com
:date: 2015-06-05 15:42:28
:tags: python, supvisord
:category: tools


linux做为开发环境, 经常需要安装一些第三方服务。
如mongodb服务器，redis服务器, nginx服务器等.

这些服务器如果是通过apt安装，默认是会开机启动,
并且能够通过sudo /etc/init.d/<name> restart/stop/start来控制.
不然就要自己写启动脚本，相当麻烦，并且危险.
并且没法检测到经常意外挂掉，日志和通知也相对较弱.


所以这里考虑用supervisord取代系统的开机启动任务.开机启动supervisor.
由supervisor来启动后续进程。好处多多.

1) 配置文件简单，改起来容易。可控制行强.

2) 自动重启功能。

3) 良好的日志和通知功能。


需要注意的事项:

1) 如果应用其他地方也需要启动supervisord，如启动一个web服务器的supervisord进程.
   则系统中会有两个supervisor进程。需要注意不引发问题.

2) supervisord默认有自动重启，会导致通过kill杀掉的进程自动重启，需要注意。
   通过supervisorctl -c config stop <NAME>可以用来停止和启动，使用linux别名简化输入.

3) 考虑是否用可能有些进程不适合或不能用supervisor来操作.

4) 如何处理日志通知等也需要考虑.

5) 通过apt-get安装的应用需要先去掉系统中的启动项。

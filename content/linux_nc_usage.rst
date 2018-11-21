linux下nc命令使用
=================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2014-08-15 16:20:32
:status: draft
:tags: nc


nc/netcat 一个很强大的tcp/udp工具.

1) 可以手动发送udp/tcp包

2) 可以开启tcp/udp服务器，做测试等用处

3) 可以做端口扫描

常用选项
--------

1) -l 打开listen模式，用于开启一个listen server

2) -s/-p 设置链接的源ip和端口，用于请求伪造。不能和 -l 一起使用.

3) -U/-u/-p 使用Unix/udp/tcp协议

4) -X/-x/-P 代理设置相关

5) -w/-v 超时等

6) -z 端口扫描


使用例子
--------

<1> 创建一个服务器::

    nc -l 1717
    nc -l 1717 >> out.log

<2> 链接服务器,拼接请求::

    nc localhost 1717
    nc localhost 1717 < in.log
    echo -e -n "GET HTTP/1.1\r\n\r\n" | nc localhost 80
    nc localhost 25 <<EOF

<3> 端口扫描::

    nc -z -v localhost 20-30
    echo "QUIT" | nc localhost 20-30


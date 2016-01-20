linux下配置iptables
===================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2014-08-19 16:29:27
:status: draft
:tags: linux, iptables, security


iptable主要用于配置linux服务器防火墙规则。

主要概念
--------

<1> 记录表 table
iptable包含在4个记录表中

1) filter (default table)

2) NAT

3) Mangle (for special packet alteration)

4) Raw

<2> 策略链 chain
记录表，每个记录表包含多个策略链

1) filter table

   1) input chain

   2) output chain

   3) forward chain

2) NAT table

   1) prerouting chain

   2) postrouting chain

   3) output chain

3) Mangle table

   1) prerouting chain

   2) output chain

   3) forward chain

   4) input chain

   5) postrouting chain

4) raw table

   1) prerouting chain

   2) output chain

<3> 过滤规则 rule
每个策略链会有多个rules,来实际处理防火墙过滤规则.
每个rule包饭target和criteria.

1) criteria满足时，就会执行对应的target

2) 不满足时，继续检查下一条rule

target分为:

1) accept

2) drop

3) queue??

4) return??

5) reject

基本命令
--------

开启防火墙::

    # iptables规则存储在/etc/sys
    service iptables status
    service iptable start

清空规则::

    # 临时
    iptable -F
    iptable --flush
    # 永久
    iptable --flush
    service iptables save

查看rules::

    iptable -t table --list
    iptable --list

iptable输出中主要有以下内容:

1) num规则计数

2) target (accept/reject..)

3) prot协议(tcp/all/udp/icmp...)

4) opt特殊选项

5) source源地址

6) dest目的地址






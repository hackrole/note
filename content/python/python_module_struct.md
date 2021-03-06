Title: python标准模块struct笔记
Date: 2014-09-11
Category: programming
Tags: python
Author: hackrole
Email: hack.role@gmail.com


struct模块的作用为，完成字节串到python对象的转换.


# 基本的api接口

## python对象 -> 字节串

1) pack(fmt, v1, v2, v3...)

2) pack_info(fmt, buffer, offset, v1, v2...)
    将多个python对象按固定的格式转化为字节串
##  字节串 -> python对象

1) unpack(fmt, str)

2) unpack_from(fmt, buffer, offset=0)

## 其他

1) calcsize(fmt) 计算一个fmt需要多少字节

2) Struct(fmt), 包含pack/unpack等方法。


# 转换说明
转换中要重要的有以下四项：

## byte order
字节顺序有大端和小端两种。
不同机器可能使用不同的字节序，
网络字节序统一采用大端.

1) native 本地字节序(与机器和本地环境相关)

2) little-endian 小端

3) big-endian 大端

4) network 网络字节序（使用大端)


## size
同一个c type在不同机器上可能有不同的大小。

1) native 于机器和本地环境相关的大小

2) standard 于环境无关的标准大小

## TODO alignment
对齐方式

##  format char

| char | c type             | python type   | size |
|------|--------------------|---------------|------|
| x    | pad bytes          |               | 1    |
| c    | char               | string(len 1) | 1    |
| b    | signed char        | integer       | 1    |
| B    | unsigned char      | integer       | 1    |
| ?    | bool               | bool          | 1    |
| h    | short              | integer       | 2    |
| H    | unsigned short     | integer       | 2    |
| i    | int                | integer       | 4    |
| I    | unsigned int       | integer       | 4    |
| l    | long               | integer       | 4    |
| L    | unsigned long      | integer       | 4    |
| q    | long long          | integer       | 8    |
| Q    | unsigned long long | integer       | 8    |
| f    | float              | float         | 4    |
| d    | double             | float         | 8    |
| s    | char[]             | string        |      |
| p    | char[]             | string        |      |
| P    | void *             | integer       |      |

# 重要事项

## struct 前缀

| char | byte order   | size     | alignment |
|------|--------------|----------|-----------|
| @    | native       | native   | native    |
| =    | native       | standard | none      |
| <    | litte-endian | standard | none      |
| >    | big-endian   | standard | none      |
| !    | network      | standard | none      |

若格式化字符串第一个字符不是上面的一个，则未默认的@.

## TODO 弄懂字节序和alignment规则

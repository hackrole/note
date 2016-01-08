musca笔记
=========
:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-08 15:31:41
:tags: musca, linux


简介
----

musca 是一个平铺式的窗口管理工具(WM). 使用纯键盘操作.

安装
----

debian 7
~~~~~~~~

1) 下载dmenu源码，编译安装

2) 下载musca源码，编译安装

3) 创建/usr/share/sessions/musca.desktop文件

ubuntu高版本下
~~~~~~~~~~~~~~

基本同debian, 不过要修改配置文件把 *.c 放到 -l前面才能编译通过，
不过仍然有不少警告.

使用
----

基本键位
~~~~~~~~

| key                    | desc                  |
| W-t                    | open a terimal        |
| W-h                    | split h               |
| W-v                    | split v               |
| W-r                    | close split           |
| W-o                    | only split            |
| W-g                    | show/switch win-group |
| W-m                    | exec musca command    |
| W-x                    | open application      |
| W-up/down/left/right   | move on frame         |
| W-S-up/down/left/right | move frame to         |
| W-u                    | undo frame            |
| W-k                    | close widow           |

基本commands
~~~~~~~~~~~~

| cmd         | desc                         |
| add <name>  | add a window group and focus |
| drop <name> | drop a window group          |
| move <name> | move frame wo window group   |

vim插件Synatics配置
===================
:author: hackrole
:email: daipeng123456@gmail.com
:date: 2015-04-28 15:44:44
:tags: vim, syntics


synatics是一个通用的语法检查插件,通过调用外部命令完成语法检查,之后合并多个语法检查的结果,将结果显示在quick-issue上.

mode-map配置
------------

synatics有两种模式, active/passive
active模式下会自动运行语法检查
passive模式下需要手动运行语法检查 

:SynaticsCheck
:SynacticsCheck <checkers: (pyling flake8)>

使用
:SynaticsToggleMode切换模式,
g:synatics_mode_map来配置默认情况.

注意
~~~~

1) 设置g:synatics_check_on_open/g:synatics_check_on_wq开启或关闭自动语法检查

配置分类
--------

synatics配置分为两种, 全局配置(配置synatics行为)/插件配置(配置单一莫个文件类型或checker)

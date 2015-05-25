我的vim插件整理
===============

:date: 2014-05-12
:tags: vim
:authors: hackrole
:summary: 我的vim插件整理,简单记下自己使用中的vim插件列表.持续的整理中,有不少需求暂时也没知道比较满意的插件，一些插件还没完成配置起来。

通用
----

nerdtree
~~~~~~~~
方便的文件目录树插件，集成bookmarks/filter等功能，必备插件
:NERDTreeToggle

nerdcommenter
~~~~~~~~~~~~~

一个支持多种语言的代码注释插件，提供多种快捷注释。未仔细研究。
\c<space>,\cc

tagbar
~~~~~~

代码结构预览插件，可以支持代码结构的嵌套，自定义扩展等.taglist的替代产品
:TagbarToggle

auto-pairs
~~~~~~~~~~

自动补全{},(),[],"",''等的插件，可以toggle on/off.

CmdlineCompletes
~~~~~~~~~~~~~~~~

命令行补全插件，可以补全buffer里的内容。C-n/C-p

:TODO: 一直在找能在命令行能copy/paste的插件

vundle
~~~~~~

插件管理,之前还一直在用vam,不过后面还是决定切换到vundle.

总的来说vundle更方便，容错行也更好

riv
~~~

vim里写rst的插件

grep
~~~~

全局查找的插件，还不太会用

emmet
~~~~~

前身是zencode,写html/css必备的插件.

比较麻烦的是，生成的html代码格式有时不太尽任意，手动调整也不太方便.
考虑以后自己在这个基础上扩展下。

UltiSnips
~~~~~~~~~

代码模板插件，写代码必备，snipmate的替代产品。

TagmaTasks
~~~~~~~~~~

任务管理插件，不过只能支持文件，不能提供项目todolist支持。
暂时没找到比较好的替代

TaskList
~~~~~~~~

:TODO:

airline
~~~~~~~

状态行强化的插件，比powerline更轻量级。没有外部依赖。
powerline还是各种问题/各种依赖。无视之。

EasyMotion
~~~~~~~~~~

在vim里更快速的跳转到指定位置

\\w,\\f,...

lookupfile
~~~~~~~~~~

快速打开文件的插件，需要genutils插件支持，现在用的较少了。

gtrans
~~~~~~

翻译插件.
\gt
\gv

matchit
~~~~~~~

:TODO:

minibufexploreerpp
~~~~~~~~~~~~~~~~~~

vim的buff显示管理插件,有时会导致窗口排位错乱。

DrawIt
~~~~~~

vim绘制文本图的插件，还不太会用

Conque-Shell
~~~~~~~~~~~~

可以在vim里启动bash/ipython等，不过现在使用中还有不少问题。

:TODO:


编程相关
--------

c语言/a.vim
~~~~~~~~~~~

可以方便的在c源文件/头文件中切换.
c developer必备.

c语言/c.vim
~~~~~~~~~~~

vim下的cIDE.
1) 代码模板功能，这个UltiSnips更好用.
2) 查看文档，这个可以借助man
3) 编译/运行c代码，用处不大，自己写个makefile就可以了。

python/python-mode-klens
~~~~~~~~~~~~~~~~~~~~~~~~

真正的python IDE(我要打十个),以前还要陪pep8/pylint/rope等一系列插件，还总是各种问题。
现在这一个就能解决所有问题，pythoner必备。

值得注意的是这插件有个问题，就是输入.后卡住，配置里配置下就可以解决。
还有就是会在项目目录建个.ropeproject目录，这个要加到.gitignore里

ruby
~~~~

:TODO:

golang
~~~~~~

:TODO:

nodejs
~~~~~~

:TODO:

html/css/jinja
~~~~~~~~~~~~~~

css-color-preview 可以预览css里的颜色。
vim-css-color :TODO:
jinja 支持jinja的语法高亮，在html基础上扩展而来。

配置vim syntastic语法高亮插件
=============================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-02-02 14:55:23
:serials: vim-syntastic
:series_index: 1
:status: draft
:tags: vim


本文是对syntastic中文档的简单翻译.
项目地址: https://github.com/scrooloose/syntastic

在vim中安装插件后通过 :h syntastic查看原文档

简介
----

syntastic是vim下的一个代码语法检查插件, 实现原理是通过外部命令做语法检查，并把结果显示到vim中.
可是设置为保存文件的时候自动做语法检查.

syntastic 由两部分组成.

1) 语法检查插件. 配合外部命令完成特定文件特定命令的语法检查

2) 核心部分. 调度语法插件，并输出检查结果.

快速起步
~~~~~~~~

安装教程参见项目文档.

使用方式如下:

1) :SyntasticInfo 显示当前的状态(激活还是禁用)/可用的checkers.

2) :SyntasticCheck 手动调用语法检查.默认错误信息不会输出到 **quickfix**

3) :Errors 错误输出到 **quickfix**, 并拉起errors窗口.

4) :lclose关闭错误窗口, 但是不会清空错误. :SyntasticReset 清空错误。

5) :SyntasticToggleMode 在激活禁用模式间切换.

6) 使用使用 `:lnext` `:lprevious` 做错误间跳转，不需要跳到 **quickfix** 窗口

默认的配置并不好用， 可以参考下面的配置:

.. code-block:: vim

    # 每次自动调用 :SyntasticSetLocList, 将错误覆盖 **quickfix**
    let g:syntastic_always_populate_loc_list = 1
    # 自动拉起/关闭错误窗口, 不需要手动调用 :Errors
    let g:syntastic_auto_loc_list = 1
    # 打开文件的时候做检查
    let g:syntastic_check_on_open = 1
    # 每次保存的时候做检查
    let g:syntastic_check_on_wq = 1

支持的特性
----------

1) statusline flag. 可以通过配置定制vim状态栏来显示syntastic相关信息.

.. code-block:: vim

    set statusline+=%{SyntasticStatuslineFlag()}

2) error sign. 可以在vim行号左边显示一个错误标记，标记可配置.

.. image:: /static/syntastic-error-sign.jpg
   :alt: error-sign

.. code-block:: vim

    " 配置error-sign
    let g:syntastic_error_symbol = 'EE'
    let g:syntastic_style_error_symbol = 'E>'
    let g:syntastic_warning_symbol = 'WW'
    let g:syntastic_style_warning_symbol = 'W>'

3) 错误信息高亮(需要plugin check支持)

4) 合并错误， 可以配置多个语法检查插件，最终将多个检查结果合并输出.

.. code-block:: vim

   " 需要如下配置
   let g:syntastic_aggregate_errors = 1

5) 过滤错误. 可以选择性让插件忽略一部分错误提示. 
   参见: 'syntastic_quiet_messages' 'syntastic_ignore-files' 'syntastic_<filetype>_<checker>_quiet_messages'

相关命令
--------

:Errors:
    拉起 **quick_fix** 窗口显示错误信息.

:SyntasticToggleMode:
    切换当前插件状态. 激活/禁用

:SyntasticCheck:
    手动调用语法检查

:SyntasticInfo:
    列表当前状态和可用check

:SyntasticReset:
    清空错误信息

:SyntasticSetLoclist:
    手动将错误输出到quick-fix, 但是不会打开错误窗口.(基本用不到改命令)

对常用命令可以配置一个快捷键.
推荐同时配置 :Errors :lclose :lnext :lprev 命令快捷键.

全局配置
--------
:syntastic_check_on_open:  0/1, 打开文件时做语法检查, 默认 0

:syntastic_check_on_wq: 0/1 报错时做语法检查, 默认 1

:syntastic_aggregate_errors: 0/1 合并错误, 默认 0
                             如果0则顺序调用check, 如果莫个check报错, 则不在调用后续check.
                             如果1则调用所有check, 并合并结果.

:syntastic_id_checkers: 0/1 输出错误来源. 默认1

:syntastic_sort_aggregated_errors: 对输出做排序, 默认1

:syntastic_echo_current_error: 在命令行显示当前行的错误信息. 默认1

:syntastic_cursor_columns: 默认1, 设为0加速。

:syntastic_enable_sign: 做行号左边显示错误标记. 默认1

:syntastic_enable_balloons:  鼠标悬停时显示当前行错误信息. 默认1, 改为0

:syntastic_enable_highlighting:  开启错误信息语法高亮, 默认1

:syntastic_always_populate_loc_list: 不需要手动调用 `:SyntasticSetTocList`. 默认1

:syntastic_auto_jump: 默认0

:syntastic_auto_loc_list: 自动拉起关闭错误窗口.
                          0不自动. 1自动拉起关闭. 2 自动关闭，但不自动拉起. 3 自动拉起，但不自动关闭
                          默认2, 改为1

:syntastic_ignore_file: 添加不想被检查的文件.

:syntastic_filetype_map: 将非标准filetype映射到标准文件.

:syntastic_mode_map: 配置每个filetype和全局默认默认

:syntastic_quiet_messages:  设置要忽略的错误

checker配置
-----------

其他
----


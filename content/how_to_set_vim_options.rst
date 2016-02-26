如何设置vim options
====================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-08 14:24:52
:tags: vim,vim-options


vim的set有很多讲究,暂时没时间整理完备.

可以通过:options看到已分类的所有options选项,方便设置

options分类
-----------

vim里的options一般分为如下:

1) boolean型. 如 `set number` `set nonumber` `set expandtab`

2) number型. 如: `set tabstop=4` `set shiftwidth=4` `set softtabstop=4`

3) string型. 如: `set foldmethod=marker` `set ignorecase smartcase`

4) `,` 分割的列表型. 如: `set iskeyword+=-` `set backspace=indent,eol,start`

不过的类型在使用上会有所差别。如::

    `set number` 会设置boolean选项, `set tabstop` 会返回现在的配置值.

set常用用法
-----------

set用法比较多， 一些用法不太常用，简单总结如下. 

.. list-table:: set用法
    :class: table
    :name: set-usage

    * - commands
      - describe
      - example
    * - set <option>?
      - 获取当前option value
      - set number? set tabstop?
    * - set <option>!
      - 反转option value(boolean取反)
      - set number!
    * - set <option>&(vi)(vim)
      - 复位为(vi)(vim)默认值
      - set iskeyword&
    * - set <option>=<value> or set <options>:<value>
      - 设置string或num型值为对应<value>
      - set tabstop=4
    * - set <option>+=<value>
      - number +, string append-to-string, list append-to-list
      - set tabstop+=1 set iskeyword+=-
    * - set <option>^=<value>
      - number 相乘, string unshift-to-string, list unshift-to-list
      - no
    * - set <option>-=<value
      - number -, string pop sub-string, list remove-item
      - no


同时要注意set的作用域问题，避免全局影响.

.. list-table:: set作用域问题
    :class: table
    :name: set-scope

    * - commands
      - describe
    * - setglobal
      - 全局
    * - setlocal
      - 本地
    * - set
      - global and local

不同的options有时是全局唯一的，有的会只到当前窗口或缓存区生效.

elisp keymap相关
================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-08 14:58:24
:tags: elisp, emacs


elisp按键序列概念
-----------------

elisp按键在elisp中有两种表达方式:

1> 字符串 "\C-x1"

2> 列表vector [?\C-x ?1]

函数(kbd keseq-string)返回字符串对应的按键序列(字符串或列表形式)

功能键用 <>表示, <RET> <SPC> <F1>等

keymap基本概念
--------------

keymap是一个中lisp内的数据结构，用于绑定多个按键序列到对应的command上

按键序列可以分为两种

1> prefix key 前缀键,如 C-x

2> complete key 完整的按键,如 x, C-k, C-x C-q

定义一个complete key前，需要定义所有需要的prefix key.

一般都会有多个keymap处于激活状态，分类如下
------------------------------------------

1> global keymap (shared by all buffers)

2> local keymap (通常由major mode设置)

3> zero or many minor keymap(通常有minor mode提供)

local keymap会覆盖global keymap, minor keymap会覆盖local keymap和global-keymap

create keymap and keymap format
-------------------------------

keymap format
~~~~~~~~~~~~~

**TODO**

函数(keymapp symbal)用于判断指定symbal是否为keymap

create keymap
~~~~~~~~~~~~~

| function                             | desc                                               | others                                   |
| (make-sparse-keymap &optional prompt | create and return a new keymap with no entries     | the usually keymap you need              |
| (make-keymap &optional prompt)       | create and return a new keymap with char-tables    | use this if you want bind a lots of keys |
| (copy-keymap keymap)                 | return a copy of keymap, recursive copy sub keymap | recursive copy fails on function keymap  |

新建keymap的两个函数都可选的有一个prompt参数，用于设置menu使用，一般不设置

一般使用sparse来新建keymap做按键绑定，按键较多时可以考虑keymap

keymap结构里可以递归的包含其他keymaps

keymap继承
----------

keymap可以继承其他keymap(单继承，多继承有其他实现方式),继承的逻辑和一般的类继承类似

| function                          | desc                                                                                 | others |
| (keymap-parent keymap)            | return the keymap's parent keymap, nil if no                                         |        |
| (set-keymap-parent keymap parent) | set the keymap parent to parent, if nil, do nothing, recursive set the parent parent |        |

一般用sparse keymap指定parent,non-sparse也可以制定不过因为所有键都会被重写，一般没有意义.

多继承用make-composed-keymap,

| function                                     | desc                                                                     | others |
| (make-composed-keymap maps &optional parent) | return a new keymap, whose key is first find in (first maps then parent) |        |

例如::

    (set-keymap-parent map (make-composed-keymap button-buffer-map special-mode-map))

定义prefix key
--------------

**TODO**


定义按键前缀
------------

**TODO**

(define-prefix-comamnd symbal &optional mapvar prompt)


active keymaps
--------------

**TODO**

| function                | desc |
| current-global-map      |      |
| current-local-map       |      |
| current-monor-mode-maps |      |
| use-global-map          |      |
| use-local-map           |      |

key lookup
----------

**TODO**

change/remapping/translation/bind keymaps
-----------------------------------------

remap command
~~~~~~~~~~~~~

keymaps for translating sequences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

command for binding keys
~~~~~~~~~~~~~~~~~~~~~~~~

| function         | desc |
| global-set-key   |      |
| global-unset-key |      |
| local-set-key    |      |
| local-unset-key  |      |
| define-key       |      |

scanning keymaps
----------------

menu keymaps
------------

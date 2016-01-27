learn vimscript
===============

注释
----

.. code-block:: vim

   " this is a commnet

变量
----

变量作用域:

+ b:name      缓冲区的局部变量
+ w:name      窗口的局部变量
+ g:name      全局变量 (也用于函数中)
+ v:name     Vim 预定义的变量
+ &name    options值
+ @name    寄存器值
+ &l:name   local-options


:h registers.
:h interval-variables

表达式
------

:h expr4
:h ignorecase

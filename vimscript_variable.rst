vim变量县官
===========

author: hackrole
email: daipeng123456@gmail.com
date: 2016-01-08
tags: vim,vimscript

概述
----

vim里的变量通过let定义.

变量类型:
1) 基本变量. let a = 'hello'
2) 选项 let &number = 1. let &l:number=1
3) 寄存器 let @a='hello'


变量的作用域:
1) script. let s:a = 'hello'
2) global. let g:a = 'hello'
3) buffer. let b:a = 'hello'

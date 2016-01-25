vim中不应该使用的按键映射
=========================
:author: hackrole
:email: daipeng123456@gmail.com
:date: 2015-05-07 15:43:03
:tags: vim, key-binding


vim由于历史原因,按键映射存在一些问题, 这些问题直到7.4还未能被处理. 恐怕最迟要等vim8.0.
详细内容可以参见 vim-google-group: https://groups.google.com/forum/#!topic/vim_dev/Ym6D-kWIsyo

不应该使用的按键
----------------

+ Ctrl+数字 常常会无法识别,不应该使用

+ Ctrl+字母 无法区分大小写,需要注意

+ <C-i>和<tab>冲突, emacs中也有其问题
+ <C-m>和<tab>冲突, emacs中也有其问题

+ <C-\>

+ <C-;>

+ 系统内部按键

建议的vim按键
-------------

+ 功能键和组合功能键<f2-n>/<C/S/M-f2-n>

+ <A-字母键>

+ <leader>前置键位

+ <C-字母>留做系统键位

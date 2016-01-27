vimscript keymap
================

1) vim有多种模式, keymap在不同模式可以定义为不同内容 map/imap/vmap/cmap

2) map分为递归和非递归 map/noremap. 应该一直使用非递归形式.

3) 多使用<leader>/<localleader>映射.

4) map可以附带options:

   :<buffer>: only-current buffer

   :<silent>: not-echo. (use with :silent)

   :<speical>:

   :<expr>: 使用expr的结果作为键映射

   :<unique>: 不允许定义重复键

.. [1] see :h mapleader
.. [2] see :h maplocalleader
.. [3] see :h map.txt
.. [4] see :h omap-info. 操作符等待映射

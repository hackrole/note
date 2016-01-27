vimscript autocmd
=================

1) autocmd格式 :autocmd <event-name,...> <fileter-pattern> :<cmd-to-execute>

2) 使用augroup对autocmd分组，方便管理. 可以删除已有的autocmd.

.. code-block:: vim

   augroup test
       " clear autocmd
       autocmd!
       " define new auto cmd
       <autocmd>
   endaugroup


.. [1] see :h autocmd-event for all event.

.. [2] see :h autocmd-groups for cmd-group

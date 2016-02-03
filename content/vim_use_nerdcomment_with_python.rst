vim中使用nerdcomment来注释python代码tips
========================================
:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-02-03 11:06:47
:status: published
:tags: vim, python

intro
-----

nerdcomment是一个vim插件，提供多种文件类型的代码注释功能. 同时设置了写常用的快捷按键。
项目地址: https://github.com/scrooloose/nerdcommenter.git

常用的按键有:

.. csv-table:: nerdcommnet按键
    :header: keymap, 描述, key-mode
    :class: table
    :name: csv-table

    <leader>c<space>, 切换代码注释状态, v
    <leader>cc, 注释代码, v
    <leader>cl, 注释代码.但是保持左边对齐, v
    <leader>cb, 同上both-side.暂时没看出区别, v
    <leader>ca, 切换alt注释符号, n
    <leader>cA, 在行尾添加注释, n
    <leader>c$, 从当前cursor注释到行尾, n


配合python使用tips
------------------

第一个是要设置 `let g:NERDSpaceDelims = 1`.
然后， 注释的时候会在#后加入一个空格，这样代码做pep8的时候就不会报警告了. 如图.

设置前:

.. image:: /static/vim-nerdcomment/bad-delims.jpg
    :alt: bad-pep8

设置后:

.. image:: /static/vim-nerdcomment/good-delims.jpg
    :alt: good-pep8

其次是使用<leader>cl取代<leader>c<space>. 我一般也是用<leader>c<space>用了好久。
但是注释出来的效果不是很好。看了好久文档总算是找个了解决办法.效果如下.

<leader>c<space>

.. image:: /static/vim-nerdcomment/bad-align.jpg
    :alt: bad-pep8

<leader>cl

.. image:: /static/vim-nerdcomment/good-align.jpg
    :alt: good-pep8


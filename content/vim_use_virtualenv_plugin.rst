vim中使用virtualenv插件
=======================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-03-21 10:19:42
:status: draft
:tags: vim, virtualenv, python, pep8
:category: tools


.. code-block:: bash

    pip install virtualenvwrapper

    mkvirtualenv <env>
    workon <env>

    pip install pep8 pylint pyflakes

    # open vim and install virtualenv plugin
    gvim +PluginInstall 'jmcantrell/vim-virtualenv' +qa

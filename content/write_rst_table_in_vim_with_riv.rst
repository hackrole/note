vim中使用riv插件输出表格
========================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-02-02 16:29:59
:status: published
:tags: vim
:category: tools

使用
----

严格来说, 是使用rst里支持的directives来写表格.

想对于默认的表格写起来方便很多，而且不用烦心对齐的问题.

第一种方式: csv-table

.. code-block:: rst

   .. csv-table:: options整理
       :header: "键名", "描述", "默认值", "建议值"
       :class: table
       :name: csv-table

       quiet, "是否安静模式", 0, 1
       quiet, "是否安静模式", 0, 1
       quiet, "是否安静模式", 0, 1
       quiet, "是否安静模式", 0, 1
       quiet, "是否安静模式", 0, 1

第二种方式: list-table

.. code-block:: rst

    .. list-table:: Frozen Delights!
        :widths: 15 10 30
        :class: table
        :name: list-table
        :header-rows: 1

        * - Treat
          - Quantity
          - Description
        * - Albatross
          - 2.99
          - On a stick!
        * - Crunchy Frog
          - 1.49
          - If we took the bones out, it wouldn't be
            crunchy, now would it?
        * - Gannet Ripple
          - 1.99
          - On a stick!

想对于要这么写表格，方便太多了:

.. image:: /static/vim_riv_old_table.jpg
    :alt: rst old table

生成的表格截图如下:

.. image:: /static/vim_riv_table.jpg
    :alt: rst table

vim模板
-------

如果已经配置了vim **UltiSnips** 插件, 可以使用模板让写表格更方便.

.. code-block:: vim


    snippet tb.csv "make a csv table" !b
    .. csv-table:: $1
        :header: $2
        :class: ${3:table}
        :name: ${4:csv-table}

        $0
    endsnippet

    snippet tb.list "make a list table" !b
    .. list-table:: $1
        :class: ${2:table}
        :name: ${3:list-table}

        $0
    endsnippet

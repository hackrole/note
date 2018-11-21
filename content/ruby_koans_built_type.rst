ruby koans笔记:基本类型
=======================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-14 11:41:08
:series: ruby koans note
:series_index: 1
:tags: ruby
:category: programming

boolean
-------

ruby中除 nil/false 外其他都为true. **不同与python**.

.. code-block:: ruby

    []  # true
    ""  # true
    {}  # true
    nil  # false
    false  # false

string
------

ruby支持三种字符串字面量.

1) "" 和 ''定义. 其中""支持插值表达式.

2) here-document.

.. code-block:: ruby

    a = <<EOF
        hello world
    EOF

3) flex-quote.

.. code-block:: ruby

    a = %{flex world}
    b = %!flex world!
    c = %(flex world)

string可以支持array的分片操作.

string << 操作可以在 **原地操作string** !!.

ruby 1.8支持 char类型. 1.9不再支持.

.. code-block:: ruby

  # 1.8 and below
  97 == ?a  # true
  # 1.9 and above
  "a" == ?a  # true

splite和join等操作都是String对象的method.

symbal
------

原子, 类似lisp里的symbal实现. 在ruby使用比较频繁。多数可以作为string的替代.

**TODO**

to_s/to_sym 用于在string/symbal之间转换

array
-----

ruby的array支持两中分片操作.
1) array[2, 3]. 从index=2开发取三个元素.

2) array[1..2]. 使用Range取,但是和Range有些不同, 如: 5..-1

array通过push/pop, shift/unshift支持头尾的增减操作, **原地操作!**.

ruby支持并行赋值和自动解包, 可使用并行复制做change

.. code-block:: ruby

    a, b = b, a

ruby可以使用 \*完成更复杂的并行复制.

.. code-block:: ruby

    a, *b = [1, 2, 3]  # b = [2, 3]

自动解包时，不足或多余不会报错 **不同与python**

.. code-block:: ruby

    a, b = [1]  # b = nil
    a, b = [1, 2, 3]  # b = 2

hash
----

.. note::

  ruby的hash设计和python有所不同. 在默认值和raise

hash[:not_exists] 返回nil, 而不raise. 而hash.fetch[:not_exists]会raise.

hash.new(default), 参数为默认值. 并且是唯一. 配合[]等使用是有意外之事.

.. code-block:: ruby

    h = Hash.new([])
    h['a'] << 'hello'
    h['b'] << 'world'
    puts h['a'] # ['hello', 'world']
    puts h['b'] # ['hello', 'world']

hash.new可以跟一个block.这样可以每次重建默认值，避免上面的问题

.. code-block:: ruby

    h = Hash.new { |hash, key| hash[key] = [] }
    h['a'] << 'hello'
    h['b'] << 'world'
    puts h['a'] # ['hello']
    puts h['b'] # ['world']

constant常量
------------

ruby里的常量暂时还没完全理解. **TODO**

常量使用大写字母， 可以修改，但是会有警告. **python里不会有警告** 

.. code-block:: ruby

    LOG = 4
    LOG = 2

可以在类内部定义常量, 通过命名空间做引用.

.. code-block:: ruby

    LOG = 4

    class A
      LOG = 2

      LOG == 2
      ::LOG == 4
    end

    LOG == 4
    ::LOG == 4
    A::LOG == 2

class继承也会继承常量。

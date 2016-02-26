ruby koans笔记:流程控制
=======================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-14 14:16:28
:series: ruby koans note
:series_index: 2
:tags: ruby, koans

if/unless
---------

ruby支持if/unless(if not).

.. code-block:: ruby

  if true
    :true
  else
    :false
  end

  if true
    :true
  elseif :false
    :false
  end

  unless true
    :true
  end

ruby是面向表达式， if/unless也是表达式，会返回一个结果

.. code-block:: ruby

    a = if true
          :true
        else
          :false
        end

ruby 支持if倒缀语法

.. code-block:: ruby

    a = :true if true

ruby支持三元元算符, ?: **python中不支持**

while/for
---------

ruby只有for...in循环

.. code-block:: ruby

    for i in [1, 2, 3]
    end

ruby使用break/next 取代break/continue

method
------

ruby方法支持*args和named argument. 但是好像不支持**kw.
named argument应该是最近加入的支持.

ruby带*args和named arg的方法class方法返回Array, **很奇怪**

.. code-block:: ruby

    def a(*args):
    end
    a.class  # => Array
    def b(b=:name)
    end
    b.class  # => Array

ruby里有private/public的作用域限制。
并且方法默认为public.属性默认为private.

ruby里私有方法不能用self调用, **很奇怪** 

.. code-block:: ruby

    class A
      def a
      end
      private :a
      def b
        a  # this works ok
        self.a  # would raise
      end

ruby里的类和module都想是一个命名空间

.. code-block:: ruby

    class A
      class B
        LOG = 'log'
      end
    end
    ::A::B::LOG
    A::B

exceptions
----------

ruby里处理exception的关键字与大多数程序很不同

.. code-block:: ruby

    begin
      fail "Oops"
      raise RuntimeError, "Oops"
      raise RuntimeError("Oops")
    rescue RuntimeError => ex
      result = :exception
    ensure
      result = :ensure
    end

ruby里的异常结构

.. code-block:: shell

    RuntimeError -> StandardError -> Exceptin -> Object

block代码块
-----------
ruby有两种代码块写法，单行和多行

.. code-block:: ruby

   [].map {|dd| }
   [].map do |dd|
   end


函数内通过yield调用block, yield可以传值到block. yield返回block的返回值

.. code-block:: ruby

    def f()
      yield
      yield("world")
      a = yield("hello")

block没有创建新的作用域，所以会改变外部作用域

.. code-block:: ruby

    a = 10
    [].map {|b| a = 11} 
    a == 11

可以使用block_given?判断是否有block

.. code-block:: ruby

    def a()
      if block_given?
        :block
      else
        :no-block
      end

block可以通过使用lambda定义，并赋值给变量, 并可以使用两中方式调用

.. code-block:: ruby

    a = lambda {|n| n + 1}
    a.call(10)
    a[10]

block可以直接传入方法, 方法也可以显式定义block

.. code-block:: ruby

    def m(&block)
    end

    a = lambda {|n| n+1}
    m(&a)

lambda和proc的区别. 是否没区别. **TODO**
估计proc是lambda的简写形式

.. code-block:: ruby

    proc = -> {|n| n + 1}


sandwich代码
------------

感觉类似python的with, 但是用法感觉很不同

.. code-block:: ruby

    def a()
      f = open("tt")
    ensure
      f.close if f
    end

配合代码块来抽象代码

.. code-block:: ruby

    def a()
      f = open("tt")
      yield(f)
    ensure
      f.close if f
    end

    def b()
      a do |f|
        f.read
      end
    end

iterater迭代
------------

ruby中大多数的集合都支持这些迭代，从Enumatable module扩展来.

each 用于遍历.
map/collect 类似python map.
select/find_all 类似python filter.
find 返回第一个可用
inject 类似python reduce

ruby中很多迭代都是配合代码块使用. 包括File.open/File.read等.

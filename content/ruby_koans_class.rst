ruby koans:类相关
=================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-14 15:26:33
:series: ruby koans note
:series_index: 3
:tags: ruby
:category: programming


属性
----

ruby使用如下如下约定:

1) 实例变量 @

2) 类变量 @@

.. code-block:: ruby
   :linenos: inline

    class A
      def initialize(name, world)
        @name = name
        @@world = world
      end
    end


ruby属性默认不可访问, 通过定义get/set方法， 或attr_read/attr_access使其可访问.

.. code-block:: ruby

    class A
      def name
        @name
      end
      def set_name(name)
        @name = name
      end
      attr_reader :name
      attr_access :name
    end

通过一些特定方法可以访问本不可访问的属性

.. code-block:: ruby

    a.instance_variables  # [:name]
    a.instance_variables_get("@name")
    a.instance_variables_eval("@name")
    a.instance_variables_eval { @name }

to_s/inspect方法返回对象的描述信息,所有object都有这些方法.
inspect返回比to_s更详细的描述.
字符串插值用的是to_s方法

ruby类使用initilize方法做初始化，类python `__init__`

open-class打开类
----------------

也被叫做monkey-patch, 用不好会导致难以调试的bug. 应该慎用.

ruby可以在必要时修改已有类，增加方法或改变既有方法

.. code-block:: ruby

    class A
    end
    class A
      def name
      end
    end
    class String
      def name
      end
    end

甚至built-in class也可以.

继承
----

使用如下方式继承.

.. code-block:: ruby

    class A < Object
    end

子类的ancestors方法返回所有父类的列表.

子类通过使用super可以调用父类同名方法, 无法调用不同名的父类方法.

module与多继承
--------------

ruby使用Minix(module)实现多继承

.. code-block: ruby

    module A
      def name
        @name
      end
    end
    class A
      include A
    end

module不能使用new初始化.
module可以方法子类中的属性.
子类里可以重写module里的方法.

scope作用域
-----------

ruby作用域使用从内到外的查找顺序.
只用类和方法会新建作用域，block不会新建作用域.

使用::语法来访问不同的作用域.

.. code-block: ruby

  ::global

  Name::Class:CONS

类名等也都是个常量


class method方法
----------------

ruby类也是一个对象, **类python**

可以为对象定义方法.

.. code-block:: ruby

    a = Object.new
    def a.wag
      :wag
    end

ruby里类和实例不共享方法和属性，类也是个对象。相当与对象模板.

使用如下方式定义类方法.

.. code-block:: ruby

    class Dog
      def Dog.name
      end
      def self.name
      end
    end
    class Dog
      class << self
        def name
          self.name
        end
      end
    end

class也是一个表达式，返回最后一个表达式的结果.

消息
----

ruby所有的方法调用都是基于消息发送.

可以使用send方法显式发送消息, 通过这种方式能调用private方法和属性

.. code-block:: ruby

    a = Object.new
    a.send(:to_s)

ruby提供了send/__send__两个方法都可以发送消息.

使用respond_to?方法返回对象是否能接受莫消息.

.. code-block:: ruby

    a = Object.new
    a.respond_to?(:to_s)

send后面的参数会作为参数传给方法

method missing
--------------

ruby的method_missing方法用来做元编程.

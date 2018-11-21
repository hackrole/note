如果在pytest中使用pdb调试代码
=============================

:tags: py.test,python,TDD
:date: 2015/11/01
:author: hackrole
:summary: how to use pdb in py.test


写单元测试的过程其实也是调试代码的过程.
单元测试保持代码可运行(快速而方便的), 是的我们可以观察跟踪代码流程,写出更高质量的代码.

之前一直使用unitest2写单元测试,需要pdb的地方,可以直接

..code:: python
    import ipdb; ipdb.set_trace()

这一方式在py.test中无法使用, 因为py.test默认会截取所有的输出.
解决办法有多个.

1) 使用py.test --pdb这里只能在代码出错时进到pdb,实用性不强.

2) 使用py.test --capture=no 配合ipdb,没实际测过.

3) 使用pdbpp配合pytest.set_trace()使用.代码如下:

   ..code:: python
       import pytest; pytest.set_trace()

第三种方法是目前最好的方法,不过有个问题,就是只用使用pdb调试,没法用到ipdb中更多方便的特性.
通过安装pdbpp库可以解决,pdbpp是另一个提供很多类型ipdb功能的库,并且可以配合py.test使用.

numpy中使用不对称数组初始话np.array的结果
=========================================

:author: hackrole
:tags: numpy
:date: 2015/10/29
:category: programming


numpy.array一般使用对齐数组初始化.
初始化后, arr具有对应的shape, 可以使用多维数组的诸多特性.

.. warning::
   如果使用未对齐的数组或未完全对齐的数组初始化, arr只会对应的可以对齐的维度上,更低维度会作为list-object类型存储.


.. code: python
   import pytest
   import numpy as np

   data1 = [[1, 2], [2, 3]]
   arr1 = np.array(data1)
   assert arr1.shape == (2, 2)
   assert 'int' in arr1.dtype
   assert arr1[1] == [2, 3]
   assert arr1[1, 1] == 3

   data2 = [[1], [2, 3]]
   arr2 = np.array(data2)
   assert arr2.shape == (2,)
   assert arr2.dtype == 'object'
   assert arr2[1] == [2, 3]
   with pytest.raises(Exception):
       arr2[1, 1]

Title: sort algorithms note
Date: 2019-03-08 10:05
Catagory: algorithms
Tags: algorithms
Author: hackrole


# Sort Algorithms note

TODO 

## heap sort

1) in-place sort algorithms

2) O(nlgn)

## 过程要点

1) left/right/parent可以通过(2n, 2n+1, n/2)算出.

2) 一般数组索引从0开始，left/right/parent为(2n+1, 2n+2, (n-1)/2)

3) 建堆算法 O(n)

4) 堆有一个cap和一个len(当前长度)

### 步骤

```python
# max-heap 保持堆性质
def max_heap(h, i):
    l = left(i)
    r = right(i)
    if l <= heap_size(A) && A[l] > A[i]:
        lg = l
    if r <= heap_size(A) && A[r] > A[i]:
        lg = r
        
    if lg != i:
        A[i], A[lg] = A[lg], A[i]
        
    max_heap(h, lg)
    
# build-heap 建堆
def build_heap(h):
    hs = len(h)
    for i = hs/2; i >= 0; i--:
        build_heap(h, i)
    
# heap-sort 排序
def heap_sort(A):
    build_heap(A)
    for i = len(A); i>0; i--:
       A[0], A[i] = A[i], A[0]
       A.size -= 1
       max_heap(A, 1)
```

# questions

1) 左式堆/二项堆

2) 堆的插入算法

3) 不用递归实现(stack?)

## quick sort


1) in-place sort

2) O(nlgn)


### 要点


### 步骤

```python
# 基于元素分裂数组为两个
def partition(A, q, r):
    x = A[r]
    i = p - 1
    for j = p; i<r; i++:
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            
    A[i+1], A[r] = A[r], A[i+1]
    return i+1
    
# quicksort
def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
```

## others

一般的递归算法可以用一个stack配置迭代来实现。
原理为通过stack来保存要执行的状态。

一般线性递归可以通过添加一个状态参数，优化为可尾递归。
线性递归一般可以直接转化为迭代写法.
树形递归一般要通过stack来实现。

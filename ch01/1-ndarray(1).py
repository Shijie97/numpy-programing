# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# ndarray是一个多维数组对象类型
a = np.array([1, 2, 3])
print(type(a)) # <class 'numpy.ndarray'>
print(a) # [1 2 3]

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.dtype) # 元素类型int32
print(b.ndim) # 维度2
print(b.shape) # 返回一个元素(2， 3)，两行三列
print(b.size) # 返回总共多少个元素，即2 * 3 = 6
print(b.shape[0]) # 返回行数2
print(b.shape[1]) # 返回列数3

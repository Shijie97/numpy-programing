# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# 从其他类型转变为ndarray类型

# asarray
x = (1, 2, 3)
newX = np.asarray(x, 'int64')
print(newX) # [1 2 3]

# fromiter从迭代对象那里创建多维数组
lst = range(0, 10)
it = iter(lst)
a = np.fromiter(it, 'int64')
print(a) # [0 1 2 3 4 5 6 7 8 9]

# arange从数值范围创建数组，终止值不包含，左闭右开
print(np.arange(0, 10, 1, 'int32')) # [0 1 2 3 4 5 6 7 8 9]

# linspace，指定起点终点以及总个数，而不是步长
print(np.linspace(0, 10, 11, dtype = 'int32')) # [ 0  1  2  3  4  5  6  7  8  9 10]
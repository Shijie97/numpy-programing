# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import numpy.matlib

# NumPy 中包含了一个矩阵库 numpy.matlib，该模块中的函数返回的是一个矩阵，而不是 ndarray 对象。

# empty返回一个矩阵，值随机
# zeros,ones不多赘述
# eye返回对角矩阵，注意这个矩阵可以不是方阵，方阵的话用identity就好
# identity返回单位阵，这个阵一定是方阵
print(np.matlib.empty((3, 4)))
print(np.matlib.zeros((3, 4)))
print(np.matlib.ones((3, 4)))
print(np.matlib.eye(3))
print(np.matlib.identity(3))

# rand(N, M)返回一个N * M大小的矩阵，值0~1
print(np.matlib.rand(3, 3))

# 矩阵永远二维，而ndarray是多维数组，因此可以互相转化

# 矩阵转ndarray，用np.asarray
a = np.matlib.rand(3, 3)
print(np.asarray(a))

# ndarray转矩阵，用np.matrix
b = [[1, 2], [3, 4]]
print(np.matrix(b))
print(type(np.matrix(b))) # <class 'numpy.matrix'>
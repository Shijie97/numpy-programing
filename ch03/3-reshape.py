# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# 修改数组形状，reshape
a = np.arange(8)
b = a.reshape(4, 2)
print(b)

# flatten，返回的是一个副本，修改不会影响原来的值
print(b.flatten()) # [0 1 2 3 4 5 6 7]

# ravel，和flatten功效一样，只不过修改会影响原来的值
b.ravel()[0] = 1
print(b.ravel()) # [1 1 2 3 4 5 6 7]

# flat，用于压平之后迭代
for x in b.flat:
    print(x)

# 矩阵转置
print(b.transpose())

# shape
a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a.shape) # (2, 3)

# resize，功效等同于reshape，只不过reshape是创建副本且有返回值，resize会修改原来的值
a = np.arange(64)
a.resize(8, 8) # 用完之后改变
print(a)

print('-' * 20)

b = np.arange(64)
b.reshape(8, 8) # 用完之后不改变
print(b)
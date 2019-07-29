# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import numpy.matlib

# dot
# dot对于两个一位矩阵，实则求内积
# 内积还可以用专门的inner函数运算
a = [1, 2, 3]
b = [4, 5, 6]
print(np.dot(a, b)) # 32
print(np.inner(a, b)) # 32

# dot对于两个矩阵，实则求矩阵乘法
c = [[1, 2],
     [2, 3],
     [3, 4]]
print(np.dot(a, c)) # [14 20]

# np.linalg.det求方阵对应行列式的值
d = [[1, 2],
     [2, 3]]
print(np.linalg.det(d))

# np.linalg.inv求方阵的逆
print(np.linalg.inv(d))
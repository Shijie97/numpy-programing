# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# numpy的算术函数，加减乘除

# add
a = np.arange(9, dtype = np.float).reshape(3, 3)
b = np.array([10, 20, 30], dtype = np.float)
print(np.add(a, b)) # 加
print(np.subtract(a, b)) # 减
print(np.multiply(a, b)) # 乘
print(np.divide(a, b)) # 除
print(np.reciprocal(b)) # 取倒数
print(np.power(a, 2)) # 幂运算
print(np.mod(a, 6)) # 取余
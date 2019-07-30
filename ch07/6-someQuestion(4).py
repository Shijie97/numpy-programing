# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# a传进去，相当于，形参x和a都指向字典这片区域，所以会改变原有的值
def f(x):
    x[1] = 0


a = {2:1}
f(a)
print(a)

# 另外一个例子
def g(x):
    x[0][0] = 5

a = np.array([[1, 2],
              [3, 4]])
g(a)
print(a)

# [[5 2]
#  [3 4]]
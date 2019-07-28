# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# 如果两个矩阵形状相同，则各位点乘
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[1, 2],
              [3, 5]])
print(a * b)

# 如果不同，触发广播机制
c = np.array([10, 20])
print(a * c)

# tile函数，铺展开
print(np.tile(a, (1, 3))) # 纵向铺展*3
print(np.tile(a, (2, 3))) # 纵向铺展*3，横向*2

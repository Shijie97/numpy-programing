# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# 迭代数组用nditer
a = np.arange(6).reshape(3, 2)
for x in np.nditer(a, order = 'C'): # C为行序，F为列序
    print(x, end = ' ') # 0 1 2 3 4 5

# 若要修改元素的值，得设置op_flags
for x in np.nditer(a, op_flags = ['readwrite']):
    if x % 2 == 0:
        x = x ** 2
    print(x, end = ' ') # 0 1 4 3 16 5

# 广播迭代
b = np.array([1, 2])
for x, y in np.nditer([a, b]):
    print('x:', x, 'y:', y)
# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# 其他方法创造ndarray对象

# empty
a = np.empty((2, 3), 'int64') # 初始化一个两行三列的数组，类型为int64，值随机
print(a)

# zeros
a = np.zeros((2, 3), 'int64') # 同上，值全0
print(a)

# ones
a = np.ones((2, 3), 'int64') # 同上，值全1
print(a)
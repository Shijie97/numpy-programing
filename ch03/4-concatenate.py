# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
print(np.concatenate((a, b), axis = 0)) # 沿着第一维, 同理也可以有第二维

# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# nonzero返回数组中非0元素的索引
a = np.array([[30,40,0],
              [0,20,10],
              [50,0,60]])
print(np.nonzero(a)) # (array([0, 0, 1, 1, 2, 2], dtype=int64), array([0, 1, 1, 2, 0, 2], dtype=int64))
b = np.nonzero(a) # b包括b[0]和b[1]
# 为了观看方便，可以使用zip函数进行解压
newB = zip(b[0], b[1])
print(list(newB)) # [(0, 0), (0, 1), (1, 1), (1, 2), (2, 0), (2, 2)]
c = np.array([1, 2, 0, 6, 0])
print(np.nonzero(c)) # [array([0, 1, 3], dtype=int64)]


# where返回数组中满足给定条件的索引
print(np.where(c != 0)) # (array([0, 1, 3], dtype=int64),) 返回索引[0, 1, 3]
print(c[np.where(c != 0)]) # 根据索引来获取对应元素[1 2 6]

# extract根据条件抽取元素，用法为 np.extract(condition, 数组名)
condition = c != 0
print(condition) # [ True  True False  True False]
print(np.extract(condition, c)) # [1 2 6]
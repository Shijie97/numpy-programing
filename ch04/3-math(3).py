# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# 统计函数

# amin / amax，返回某一维上最小/大的那个数
# argmin / argmax，返回某一维上最小/大的那个数的索引
a = np.array([[3,7,5],
              [8,4,3],
              [2,4,9]])
print(np.amin(a, axis = 0)) # 依次输出每列的最小值 [2 4 3]
print(np.argmin(a, axis = 0)) # 依次输出每列的最小值 [2 4 3] 的索引 [2 1 1]

# 极差ptp
print(np.ptp(a)) # 不指定axis默认为flatten的，9 - 2 = 7
print(np.ptp(a, axis = 0)) # 每一列的极差 [6 3 6]

# 中位数median
print(np.median(a)) # 4
print(np.median(a, axis = 0)) # [3 4 5]

# 算术平均mean
print(np.mean(a))
print(np.mean(a, axis = 0))

# 加权平均average
weights = [0.6, 0.2, 0.2]
print(np.average(a, weights = weights, axis = 0)) # [3.8 5.8 5.4] 对每一列求加权平均

# 标准差std
print(np.std([1, 2, 3, 4]))

# 方差var
print(np.var([1, 2, 3, 4]))
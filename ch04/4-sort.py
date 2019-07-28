# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# np.random.randn返回随机值，服从标准高斯分布
a = np.round(np.random.randn(10) * 100)
print(a)

# np.sort
print(np.sort(a))
print(list(reversed(np.sort(a, kind = 'heapsort')))) # 倒序输出，且用的是堆排序

# np.argsort，返回排序后的元素原来的index值
print(np.argsort(a))

# 结构体排序
dt = np.dtype([('name', 'S10'), ('age', 'int8')])
a = np.array([('zsj', 22), ('ll', 25), ('zjl', 5)], dtype = dt)
print(a)
print(np.sort(a, order = 'age')) # 按年龄升序
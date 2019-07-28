# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# unique去重
a = np.array([1, 1, 1, 2, 5, 2, 9, -1])
u = np.unique(a)
print(u)

# set去重
print(list(set(a)))
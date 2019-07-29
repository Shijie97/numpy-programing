# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# ndarray.copy()是深拷贝
a = np.arange(10)
b = a.copy()
print(a is b) # False
b[0] = 100
print(a) # [0 1 2 3 4 5 6 7 8 9]
print(b) # [100   1   2   3   4   5   6   7   8   9]
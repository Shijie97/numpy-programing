# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
a = np.arange(9)

# 如果是个数，则代表要分成几份，如果是个数组，则代表切分点，切分点左闭右开
print(np.split(a, 3)) # [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]
print(np.split(a, [4, 7])) # [array([0, 1, 2, 3]), array([4, 5, 6]), array([7, 8])]
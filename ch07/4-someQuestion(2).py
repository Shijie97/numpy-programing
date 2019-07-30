# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
from collections import Counter

# collection.Counter的用法
a = [1, 2, 2, 5, 5, 5, 5, 7]
b = Counter(a)
print(b) # Counter({5: 4, 2: 2, 1: 1, 7: 1})
print(b[5]) # 4
# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

x = np.array([[1, 2, 3],
              [4, 5, 6]])
print(x.reshape(-1, 1))
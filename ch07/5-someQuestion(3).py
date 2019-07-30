# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 如何画出多张图形，并且是单独的，也不是subplot
x = np.arange(-5, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()

x = np.arange(0, 10, 0.1)
y = np.cos(x)
plt.plot(x, y)
plt.show()
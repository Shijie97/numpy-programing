# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

a = np.arange(9).reshape(3, 3)
print(a ** 2)

# matplotlib
# x = [[1, 5],
#      [2, 3]]
# plt.plot(x[0], x[1])
# plt.show()

dict = OrderedDict()
dict['a'] = 1
dict['b'] = 2
print(list(dict.keys())[0])

x = [1, 2, 3, 4, 5]
y = [7, 8, 9, 10, 100]
u = list(zip(x, y))
print(u)
for pos in range(len(x)):
    plt.plot(x, y)
plt.show()
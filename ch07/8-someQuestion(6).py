# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# hist指的是统计直方图，统计样本在各个区间的个数，然后以直方图的形式画出来
# 参数一：x，最好是一位数组
# 参数二：bins，bins如果是一个整数，则代表，要把x分为多少类，此时应该配合参数三使用
# 参数三：range，在bins为整数的前提下，range是一个元组(xmin, xmax)，指定x的上下界

# 上面讲的bins为整数，range(xmin, xmax)的用法是方法一
# 方法二，是指bins为一个np.arange(a, b, step)数列，指的是将x的范围指定为a ~ b，并且每step格为一类
# 方法二不需要指定range参数

# 方法一
x = np.random.randn(10000)
plt.hist(x, bins = 5, range = (-3, 3))
plt.show()

# 方法二
x = np.random.randn(10000)
plt.hist(x, bins = np.arange(-4, 4, 0.1))
plt.show()
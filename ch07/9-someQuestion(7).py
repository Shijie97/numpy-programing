# !user/bin/python
# -*- coding: UTF-8 -*-

# 想通过函数改变numpy数组的时候，这个函数一定要用np自带的函数

import numpy as np
import matplotlib.pyplot as plt

# f = lambda x : x if x > 0 else 0
a = np.random.randn(10, 10)
def ff(x):
    if x > 0:
        return x
    else:
        return 0

def fff(x):
    return np.exp(x)

print(fff(a))

def g():
    x = np.arange(0, 9, 0.01)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()

g()
# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# 单个数组的读写用save和load
a = np.array([1,2,3,4,5])
np.save('output.npy', a)
b = np.load('output.npy')
print(b) # [1 2 3 4 5]

# numpy.savez() 函数将多个数组保存到以 npz 为扩展名的文件中
# 不起名的话，默认为arr_0，arr_1...
b = np.arange(10)
np.savez('twoarr.npz', a, range_10 = b)
f = np.load('twoarr.npz')
print(f['arr_0']) # [1 2 3 4 5]
print(f['range_10']) # [0 1 2 3 4 5 6 7 8 9]


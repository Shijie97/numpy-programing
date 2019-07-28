# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
# 花式索引
x = np.arange(0, 32, 1).reshape(8, 4)
print(x)
print('*' * 20)
print(x[[4,2,1,7]]) # 打印第4，5，1，7行

# np.ix_类似于笛卡尔积的形式
print(x[np.ix_([1,5,7,2],[0,3,1,2])])# 打印1,5,7,2行，对于每一行，排列顺序为0,3,1,2

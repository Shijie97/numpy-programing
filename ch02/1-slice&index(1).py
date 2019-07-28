# !user/bin/python
# -*- coding: UTF-8 -*-
import numpy as np

a = np.arange(0, 10)
# 切片，索引从2开始，到8结束（不包括8），步长为2
print(a[2:8:2]) #[2 4 6]
print(a[2:-2]) # 2 ~ 7，因为-2代表8，但是又不能包括8
print(a[1:]) # 1 ~ 9

b = np.zeros((10, 8), 'int64')
print(b[2:8:2]) # 三行0，和一维一样的套路

# 用...选择某几行或者某几列
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [10, 11, 12]]
a = np.asarray(a)
print(a[..., 0]) # 打印第一列，不过是一位数组[ 1  4  7 10]
print(a[1:, ...]) # 打印第二道最后一行
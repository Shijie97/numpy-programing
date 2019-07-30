# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
from collections import Counter

# collection.Counter的用法
a = [1, 2, 2, 5, 5, 5, 5, 7]
b = Counter(a)
print(b) # Counter({5: 4, 2: 2, 1: 1, 7: 1})
print(b[5]) # 4


# np.sum的用法，不指定axis，默认矩阵所有元素相加
# axis = 0，计算每列和
# axis = 1，计算每行和
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([[1, 2, 3],
              [4, 5, 6]])
print(np.sum(a * b, axis = 0))

# 函数的赋值
def f(x, y):
    return x + y
a = f
print(a(1, 2))

# 一次获取ndarray的多个元素
# 注意只有ndarray可以，普通的list不行
a = np.array([1, 2, 3, 5, 4])
b = [0, 1, 1, 2]
print(a[b])

# -= +=的使用
a = 1
a += 5
print(a)

# 元组作为迭代器
dict = {}
a = ['a', 'b', 'c', 'd']
for x in a:
    dict[x] = x * 2
print(dict) # {'a': 'aa', 'b': 'bb', 'c': 'cc', 'd': 'dd'}
# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# A * B, np.dot(A, B)以及np.multiply(A, B)三者没区别（除了两个一维相乘的时候，dot是求内积之外）
# 当两个都是一维，没指定为二维的时候，默认对应元素相乘
# 当一个一维一个多维且允许广播的时候，则先广播，然后对应元素相乘
# 若A和B都规定为二维，且满足矩阵乘法要求，则进行矩阵乘法

A = np.array([1, 2, 3])
B = np.array([1, 2, 3])
print(A * B) # [1 4 9]，对应项相乘
print(np.dot(A, B)) # 14，求内积
print(np.dot(A.reshape(3, 1), A.reshape(1, 3))) # 如果是一维，不指定就默认是一维，现在指定了是二维的，就按矩阵乘法来算

# [[1 2 3]
#  [2 4 6]
#  [3 6 9]]

print(np.multiply(A, B)) # [1 4 9]，仍为对应项相乘
print('-' * 50)
print(A.reshape(3, 1) * A.reshape(1, 3))

# [[1 2 3]
#  [2 4 6]
#  [3 6 9]]
print(np.multiply(A.reshape(3, 1), A.reshape(1, 3)))

# [[1 2 3]
#  [2 4 6]
#  [3 6 9]]

print('*' * 50)
C = np.array([[1, 2, 3],
              [4, 5, 6]])
print(A * C) # 将A进行广播，然后对应项相乘

# [[ 1  4  9]
#  [ 4 10 18]]

# arange，range和xrange
# arange属于Numpy的一个函数，生成一列数
print(np.arange(10))

# range是python的函数，返回一个生成器
print(range(10)) # range(0, 10)


# 求数组中指定元素的个数，先转化为布尔数组，在sum求和
a = np.arange(10)
b = [a % 2 ==0]
print(b)
print(a % 2 == 0) # [ True False  True False  True False  True False  True False]
print(np.sum(a % 2 == 0)) # 5

print('-' * 50)
# 查看数组中符合规定的个数
c = np.array(['dog', 'dog', 'god', 'cat'])
d = list(map(lambda x: 1 if x == 'dog' else 0, c))
print(d)
print(np.sum(d)) # 2

# 对布尔值数组进行sum运算的时候，只数包含True的个数
a = np.array([1, 2, 3, 4])
b = np.array([1, 3, 3, 0])
print(a == b) # [ True False  True False]
c = a == b
print(c) # [ True False  True False]
print(np.sum(c)) # 2

# (2, 3) * (2, 3)
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a * b)

# 实则为对应项相乘
# [[ 1  4  9]
#  [16 25 36]]
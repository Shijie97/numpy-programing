# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# append，修改的是副本，有返回值，因此需要将副本保存到另外一个变量中
# append如果指定维度，则添加的值必须和原矩阵/列表结构完全一致
# append如果不指定维度，则默认是一维，和list的append用法一样
a = np.array([[1, 2]])
newA = np.append(a, [3, 4]) # ，不指定axis默认为一位数组，因此里面的[]自己会取消
print(newA)
newB = np.append(a, [[3, 4]], axis = 0) # 向第0维添加元素，这个和list的append不太一样，这里的形状必须和a保持一样，即两层方括号
print(newB)
newC = np.append(newB, [[5, 6], [7, 8]], axis = 1) # 横向append
print(newC)

# 同append，insert，修改的是副本，有返回值，因此需要将副本保存到另外一个变量中
# 如果不指定维度，则默认一维，自动展开
# 若指定维度，则index的插入值，不要求和append一样必须和原数组/矩阵结构一样，和list的append一样就好
newA = np.insert(a, 0, 3) # 在index为0的位置插入3这个数字
print(newA) # [3 1 2]
newB = np.insert(a, 0, [3, 4], axis = 0)
print(newB) # [[3, 4], [1, 2]]、

# delete，修改的是副本，有返回值，因此需要将副本保存到另外一个变量中
# 如果不指定维度，则默认一维，自动展开
# 也可以指定维度，代表删除某一行或者某几列
b = np.array([[1, 20], [3, 4]])
newA = np.delete(b, 0) # 删除index为0的那一个数
print(newA) # [1 3 4]
newB = np.delete(b, 0, axis = 0)
print(newB) # 删除第一行 # [[3 4]]

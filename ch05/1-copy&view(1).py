# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# 副本：深拷贝，即内容完全相同，地址不同
# 视图：浅拷贝，共享内存

# 浅拷贝：直接赋值
a = np.arange(10)
b = a
print(id(a) == id(b)) # True

# 浅拷贝：调用view函数 / 切片
# view函数或者切片，区别于直接赋值，因为地址会改变，但是内容仍指向原来的内容
b = a.view()
print(id(a) == id(b)) # False
print(a is b) # False
b[0] = 100
print(a) # [100   1   2   3   4   5   6   7   8   9]
print(b) # [100   1   2   3   4   5   6   7   8   9]

# 浅拷贝：切片
# 会更改原来的值，但是地址不同，等同于view
print('*' * 50)
a = np.arange(10)
b = a[:]
c = a[1:]
b[0] = 101
c[0] = 102
print(a) # [101 102   2   3   4   5   6   7   8   9]
print(b) # [101 102   2   3   4   5   6   7   8   9]
print(c) # [102   2   3   4   5   6   7   8   9]
print(id(a), id(b), id(c)) # 2355930764512 2355930764592 2355913162544

# 然而，在Python中，切片却是深拷贝
print('-' * 50)
words = ['cat', 'dogdog', 'mouse']
new_words = words[:]
new_words[0] = 'puppy'
print(words) # ['cat', 'dogdog', 'mouse']
print(new_words) # ['puppy', 'dogdog', 'mouse']
print(words is new_words) # False

# 再一次证明，Python中，切片是深拷贝
print('#' * 50)
a = [1, 2, 3, 4, 5]
b = a[:]
b[0] = 10
print(a) # [1, 2, 3, 4, 5]
print(b) # [10, 2, 3, 4, 5]
print(a is b) # False
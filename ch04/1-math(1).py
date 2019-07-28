# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# sin
a = np.array([30, 45, 60 ,90, 180])
print(np.sin(a * np.pi / 180))

# atan
print(np.degrees(np.arctan(1))) # 45.0，弧度制转为角度制

# round 四舍五入
a = np.array([1.0, 5.55, 123, 0.567, 25.532])
print(np.round(a))

# floor 向下取整
print(np.floor(a))

# ceil 向上取整
print(np.ceil(a))
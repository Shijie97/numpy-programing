# !user/bin/python
# -*- coding: UTF-8 -*-

from matplotlib import pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.title('sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y1, 'g--')
plt.plot(x, y2, '--')
plt.legend()
plt.show()

x =  [5,8,10]
y =  [12,16,6]
x2 =  [6,9,11]
y2 =  [6,15,7]
plt.bar(x, y, align =  'center')
plt.bar(x2, y2, color =  'g', align =  'center')
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()
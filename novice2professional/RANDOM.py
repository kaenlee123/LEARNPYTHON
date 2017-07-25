# coding=UTF-8

'''==============================================numpy.random'''
import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt
'''生成随机正太分布'''
sample = nr.normal(size=(3, 3))
print('3x3:', sample)

'''随机漫步'''
nsteps = 100
en = nr.randint(0, 2, size=nsteps)  # x-y(不包括y)的选取整数
enn = np.where(en > 0, 1, -1)
walks = np.cumsum(enn)
# 下面用图展示
plt.figure()
plt.plot(list(range(len(walks))), walks)
plt.title('walks')
plt.show()

'''0-1之间的随机值'''
print(nr.rand(3, 3))

'''标准正太分布'''
print(nr.randn(3, 3))

'''离散选择'''
print(nr.choice([1, 24, 2], size=3))

'''============================================random'''
from .random import *
from time import *
date1 = (2016, 1, 1, 12, 0, 0, -1, -1, -1)
date2 = (2016, 4, 3, 12, 0, 0, -1, -1, -1)
time1 = mktime(date1)
time2 = mktime(date2)   # 转化为新世纪纪元（秒）
'''连续均匀分布'''
timeRandom = uniform(time1, time2)
dateRandom = localtime(timeRandom)
print(asctime(dateRandom))
# out: Mon Feb 22 09:38:18 2016

'''模拟投骰子'''
print(randrange(6)+1)

'''打乱排序'''
print(shuffle(list(range(10))))  # none
x = list(range(10))
shuffle(x)
print(x)
# [8, 2, 4, 5, 3, 7, 0, 1, 6, 9]
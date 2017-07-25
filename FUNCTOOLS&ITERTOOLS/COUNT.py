# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/19 15:48
purpose:
"""

from itertools import count


iterCount = count(start=10, step=2)
x = [next(iterCount) for i in range(3)]
print(x)

def mycount(start=0, step=1):
    """
    生成一个从年开始的迭代器
    :param start: 起始
    :param step: 步长
    :return:
    """
    n = start
    while True:
        yield n
        n += step

myIterCount = mycount(10, 1)
print(next(myIterCount))
print(next(myIterCount))


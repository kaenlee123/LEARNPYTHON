# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/24 10:47
purpose:
"""

from itertools import product

x = range(3)
print(list(product(x, repeat=3)))
print(list(product(x, x, x)))
print(list(product(x, x, x, repeat=2)))


def MyProduct(*args, repeat=1):
    res = [[]]
    pools = [tuple(p) for p in args] * repeat
    for p in pools:
        res = [x + [y] for x in res for y in p] #动态的res指数形式增加
    for p in res:
        yield tuple(p)


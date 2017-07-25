# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/24 12:02
purpose:
"""

from itertools import starmap, product
xy = product(range(3), [2])
print(list(starmap(pow, xy)))

def startMap(func, iterable):
    for args in iterable:
        print(args)
        yield func(*args)

xy = product(range(3), [2])
print(list(startMap(pow, xy)))

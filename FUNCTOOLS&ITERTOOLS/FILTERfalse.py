# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/24 11:06
purpose:
"""

from itertools import filterfalse

x = range(10)
func = lambda x: x % 2
print(list(filterfalse(bool, x)))
print(list(filterfalse(func, x)))


def MyFilter(iterable, func=None):
    if func == None:
        func = bool
    for x in iterable:
        if func(x):
            yield x


func = lambda x: x % 2
print(list(MyFilter(x)))
print(list(MyFilter(x, func)))

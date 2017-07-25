# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/24 11:24
purpose:
"""

from itertools import islice
import sys

x = range(10)
print(list(islice(x, 2)))
print(list(islice(x, 2, 4)))
print(list(islice(x, 2, 6, 2)))


def MySlice(iterable, *args):
    s = slice(*args)
    # print(s)
    it = iter(range(s.start or 0, s.stop or sys.maxsize, s.step or 1))
    try:
        nexti = next(it)
    except StopIteration:
        return
    for i, element in enumerate(iterable):
        if i == nexti:
            yield element
            nexti = next(it)

print(list(MySlice(x, 3, 2)))
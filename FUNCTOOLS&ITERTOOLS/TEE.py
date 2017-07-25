# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/24 13:00
purpose:
"""

from itertools import tee
from collections import deque

x = range(3)
x1, x2 = tee(x, 2)
print(list(x1), list(x2))


def myTee(iterable, n):
    it = iter(iterable)
    deques = [deque() for i in range(n)]

    def gen(mydeque):
        while True:
            if not mydeque:  # when the local deque is empty
                try:
                    newval = next(it)  # fetch a new value and
                except StopIteration:
                    return
                for d in deques:  # load it to all the deques
                    d.append(newval)
            yield mydeque.popleft()

    return tuple(gen(d) for d in deques)

print([list(i) for i in myTee(x, 3)])

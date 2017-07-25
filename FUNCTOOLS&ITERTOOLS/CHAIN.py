# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/19 17:14
purpose:
"""

from itertools import chain

ch = chain([1, 2, 3], ["a", "b"], range(3))
print(list(ch))


def myChain(*x):
    for i in x:
        for j in i:
            yield j


mych = myChain([1, 2, 3], [2, 3, 2])
print(list(mych))


ch_ = chain.from_iterable([[1, 2, 3], ["a", "b"]])
print(list(ch_))

def myChainIters(iterable):
    for it in iterable:
        for j in it:
            yield j
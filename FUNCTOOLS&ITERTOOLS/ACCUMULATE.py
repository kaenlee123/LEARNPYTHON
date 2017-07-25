# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/20 20:21
purpose:
"""

from itertools import accumulate
import operator
import copy

x = [1, 2, 3, 4, 5]

print(list(accumulate(x, operator.mul)))

def myAccmulate(iterable, func):
    it = iter(iterable)
    try:
        acc = next(it)
    except StopIteration:
        return None
    yield acc
    for e in it:
        acc = func(acc, e)
        yield acc

print(list(myAccmulate(x, operator.mul)))



it = iter(x)

def myproduct(iterable):
    it = iter(iterable)
    temp = iter(iterable)
    while next(temp):
        for i in it:
            print(i)
            for j in it:
                #尾部会直接在这里跳出
                yield (i, j)
            it = copy.copy(temp)  # it的值和temp共享, 不copy 会在while next丢失一个字值
            break # 必须调到while 才能重新赋值it并进入下一层for
print(list(myproduct([1, 2, 3, 4])))

def myproduct(iterable):
    it = iter(iterable)
    temp = iter(iterable)
    while next(temp):
        for i in it:
            print(i)
            for j in it:
                for z in it:
                    #尾部会直接在这里跳出
                    yield (i, j, z)
            it = copy.copy(temp)  # it的值和temp共享, 不copy 会在while next丢失一个字值
            break # 必须调到while 才能重新赋值it并进入下一层for
print(list(myproduct([1, 2, 3, 4, 5])))
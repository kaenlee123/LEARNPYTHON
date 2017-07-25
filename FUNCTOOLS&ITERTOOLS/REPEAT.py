# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/19 17:00
purpose:
"""
from itertools import repeat

rp = repeat("abdc", 7)
x = [next(rp) for i in range(3)]
print(x)

def myRepeat(item, times=None):
    if not bool(times):
        while True:
            yield item
    else:
        for i in range(times):
            yield item

myrp= myRepeat("1212")

x = [next(myrp) for i in range(31)]
print(x)
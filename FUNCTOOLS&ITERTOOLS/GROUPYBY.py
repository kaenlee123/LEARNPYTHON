# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/19 17:47
purpose:
"""

from itertools import groupby

gb = groupby("aaaabbbaaa")  #连续的迭代对象相同则分为一类

for key, gr in gb:
    print(key, list(gr))

def keyFunc(x):
    if x == "a":
        return 1
    elif x == "b":
        return 2
    else:
        return 0
gb01 = groupby("aaaabbbaaa", keyFunc)
for key, v in gb01:
    print(key, list(v))


class MyGroupBy(object):
    # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
    # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
    def __init__(self, iterable, key=None):
        if key is None:
            key = lambda x: x
        self.keyfunc = key
        self.it = iter(iterable)
        self.tgtkey = self.currkey = self.currvalue = object()

    def __iter__(self):
        return self

    def next(self):
        while self.currkey == self.tgtkey:
            self.currvalue = next(self.it)  # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)
        self.tgtkey = self.currkey
        return (self.currkey, self._grouper(self.tgtkey))

    def _grouper(self, tgtkey):
        while self.currkey == tgtkey:
            yield self.currvalue
            self.currvalue = next(self.it)  # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)

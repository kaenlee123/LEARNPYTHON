# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/19 17:21
purpose:
"""

from itertools import compress

cp = compress(data=[1, 0, 1, 0, 1], selectors=[1, 0, 1, 0, 1])
[print(i) for i in cp]

def MyCompress(data, selectors):
    # for d, s in zip(data, selectors):
    #     if s:
    #         yield d

    return (d for d, s in zip(data, selectors) if s)

x = MyCompress(data=[1, 0, 1, 0, 1], selectors=[1, 0, 1, 0, 1])
print(x)
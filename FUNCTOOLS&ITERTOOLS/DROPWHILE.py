# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/19 17:29
purpose:
"""

from itertools import dropwhile

x9 = range(9)
x5 = dropwhile(lambda x: x < 5, x9) # 在条件为false之后的第一次, 返回迭代器中剩下来的项.
x5 = [i for i in x5]
print(x5)

def MyDropWhile(predicate, iterable):
    itered = iter(iterable)
    for i in itered:
        if not predicate(i):
            yield i
            break
    for i in itered:
        yield i

x5 = list(MyDropWhile(lambda x: x < 5, x9))
print(x5)
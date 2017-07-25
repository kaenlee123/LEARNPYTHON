# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/24 13:21
purpose:
"""

from itertools import zip_longest, repeat, chain

print(list(zip_longest(range(2), range(3), range(4), fillvalue="-")))


class ZipExhausted(Exception):
    pass


def ZIPLONG(*args, **kwds):
    # zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    fillvalue = kwds.get('fillvalue')
    counter = len(args) - 1
    print(counter)

    def sentinel():
        nonlocal counter
        if not counter:
            raise ZipExhausted
        counter -= 1
        print("def-counter", counter)
        yield fillvalue

    fillers = repeat(fillvalue) #
    for x in args:
        print("x", x)
    iterators = [chain(it, sentinel(), fillers) for it in args]
    print(iterators)
    try:
        flag = 0
        while iterators:
            flag += 1
            print("flag", flag)
            print(tuple(map(next, iterators)))
            # yield tuple(map(next, iterators))  # 此处才开始调用sentinel
    except ZipExhausted:
        print("count:", counter)
        pass


# print(list(ZIPLONG(range(2), range(3), range(4), fillvalue="-")))
ZIPLONG(range(2), range(6), range(4), fillvalue="-")
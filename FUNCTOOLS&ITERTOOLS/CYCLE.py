# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/19 15:58
purpose:
"""
from itertools import cycle

cycleIter = cycle("asd")
x = [next(cycleIter) for i in range(10)]
print(x)


def myCycle(iterableVara):
    save = []
    for element in iterableVara:
        print("for1", save)
        yield element
        save.append(element)
        print("for2", save)

    while save:
        print("while", save)
        for element in save:
            yield element


myCycleIter = myCycle("abc")
print(next(myCycleIter))  # for1([]) -> yiled(a) ->stop1
print(next(myCycleIter))  # stop1 -> save(a) -> for2([a]) ->for1([a]) -> yield(b) -> stop2
print(next(myCycleIter))  # stop2 -> save(b) -> for2([a, b]) ->for1([a, b]) -> yield(c) -> stop3
print(next(myCycleIter))  # stop3 -> save(c) -> for2([a, b, c]) ->while([a, b, c]) -> yield(a) -> stop4


def myCyle01(iterable):
    while True:
        for i in iterable:
            yield i
cy01 = myCyle01("123")
x = [next(cy01) for i in range(10)]
print(x)

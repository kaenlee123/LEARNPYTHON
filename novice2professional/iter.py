# coding=UTF-8
'''
#Created on 2016年7月10日@author: kaen
'''
'''=============================创建一个斐波那契数列迭代器'''
class fibs:
    def __init__(self):
        self.a=0
        self.b=1
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
    def __iter__(self):
        return self
for f in fibs():
    if f>10:
        print(f)
        break

'''=============================== 列表转化为迭代器'''
x = list(range(10))
xiter = iter(x)
print(next(xiter))

'''==============================创建一个迭代器得到序列'''
class testIter:
    value = 0
    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value
    def __iter__(self):
        return self
ti = testIter()
print(list(ti))
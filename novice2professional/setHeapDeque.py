# coding=UTF-8
'''
#Created on 2016年7月12日@author: kaen
'''
'''======================================集合set'''
a = set([1,1,2,3,3])
b = set([2,3,4,4])
print(a,b)
#out: set([1, 2, 3]) set([2, 3, 4])
print(a.union(b))
#out: set([1, 2, 3, 4])
print(a|b)
#out: set([1, 2, 3, 4])
c = a&b
a.intersection(b)
print(c)
#out: set([2, 3])
print(c.issubset(a), end=' ')
print(c.issuperset(a), end=' ')
print(c < a)

print(a-c,a.difference(c))
#set([1]) set([1])

print(a^b, a.symmetric_difference(b))
#set([1, 4]) set([1, 4])
print(a.copy is a)

'''==================================堆（heap）'''
from heapq import *
from .random import shuffle
data = list(range(10))
shuffle(data)#随机打乱
print(data)  
#[1, 3, 8, 0, 2, 6, 5, 7, 4, 9]
heap =[]
for i in data:
    heappush(heap, i)  #入堆操作
print(heap)
#[0, 1, 4, 2, 3, 9, 6, 8, 7, 5] 无需中含有有序
print('返回最小元素(移除)：', heappop(heap))

'''无返回值，修改成合法的堆'''
x = [2,3,5,3,5,3,5,9,5]
heapify(x)              
print(x)

'''返回最小，并用指定对象替代'''
heapreplace(x, 0)
print(x)

'''=======================================双端队列：double——ended queue
按照元素增加顺序移除
'''
from collections import deque
q = deque(list(range(5)))
q.append(5)
q.appendleft(6)
print(q)
#deque([6, 0, 1, 2, 3, 4, 5])
print(q.pop(),q.pop())          #5 4
print(q.popleft())             #6

print(q, end=' ') 
q.rotate()                    #左移：首位相连
print(q, end=' ')
q.rotate(-1)                  #右移
print(q)
#deque([0, 1, 2, 3]) deque([3, 0, 1, 2]) deque([0, 1, 2, 3])

q.extend(q)
print(q)
q.extendleft('ss')
print(q)
#deque([0, 1, 2, 3, 0, 1, 2, 3])
#deque(['s', 's', 0, 1, 2, 3, 0, 1, 2, 3])

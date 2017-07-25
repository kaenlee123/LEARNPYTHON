#!/usr/bin/env python
# coding:utf-8
"""
  Author:   --<>
  Purpose: 
  Created: 2016/11/8
  copyright: python 3.5.2
"""

x = set("abs")
y = set("absds")  # set具有唯一性且不具有顺序
print(x, y)

# union
print("并集", x.union(y), x | y)

# intersectuon
print("交集", x.intersection(y), x & y)


# difference
print(y.difference(x), y - x)

#
print("判断是不是子集", x.issubset(y))
print("判断是不是父集", y.issuperset(x))
print("两者的交集取反", set([1, 2, 3]).symmetric_difference(set([2, 3, 4])))

z = x.copy()
print(z)
x.update(set("100"))
print(x)

# add
newz = x
x.add(100)
print(newz)  # newz 被改变

#pop
newz.pop()
print(x)  # 也被删除
print(newz)  #

# remove
newz.remove("0")
print(newz)

# discard()
newz.discard("1")
print(newz)
newz.discard("1")  # 相比remove不存在不会抛出异常

# clear
print(newz.clear())
print(newz)

# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/20 10:12
purpose: 字符串 :http://www.runoob.com/python/python-strings.html
"""

import numpy as np

# find
title = '字符串 方法: 常用fdfdf'
print(title.find('常用'), title[8:])
print('找到第一个即停止', title.find(" "))
print(title.find(" ", 5, 10))  # 限定寻找的区间

# join
l = list('123')
print('join123:', "+".join(l))

# replace
print('i love you'.replace(' ', ' do not '))  # find then replace

#  split
print(title.split(" "))

# strip
s = '@1213@'
print('delete@:', s.strip("@"))

# maketrans translate
tab = "".maketrans({"a": "1", "b":"2", "c": "3"}) # {97: '1', 98: '2', 99: '3'}
tab1 = "".maketrans("abc", "123")
print("abcd".translate(tab), "abs".translate(tab1))

# reversed: 返回一个迭代器
rev = reversed(title)
print(rev, list(rev))

# count
print("121312121".count("12"))

# title: 首字符大写
print('asasa'.title())

# index # 类似于find
print('asas'.index("a", 1, 4))

# partition # find the first 并split 保留split符号
print("12324244".partition("2"))

#
print('AsdA'.capitalize())
print('AsdA'.title())
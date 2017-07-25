# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/19 16:46
purpose:
"""

def FAB():
    a = 0
    b = 1
    while True:
        yield b
        temp = b
        b = a +b
        a = temp

Fabnaci = FAB()

[print(next(Fabnaci)) for i in range(10)]
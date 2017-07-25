# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/20 11:47
purpose:
"""
x = 3
print(eval("3 * x"))
try:
    print(eval("pow(3, '3')"))
except Exception as e:
    print(e)
    print(eval("pow(3, 3)"))


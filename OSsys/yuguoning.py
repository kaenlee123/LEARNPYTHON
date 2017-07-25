# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/21 20:41
purpose:
"""
import re
import os

def Files(dir):
    files = os.listdir(dir)
    for f in files:
        print(f)

if __name__ == '__main__':
    Files(r"D:\PycharmProjects\LEARNPYTHON\OSsys")
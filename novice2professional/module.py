# coding=UTF-8
'''
#Created on 2016年7月12日@author: kaen《模块的知识》
'''
'''查看模块包含的的所有变量和函数'''
import pprint
pprint.pprint(dir(pprint))

'''
__all__:告诉解释器函数接口
from XX import *:仅仅能调用all里面包含的函数
'''
print(pprint.__all__)
#out: ['pprint', 'pformat', 'isreadable', 'isrecursive', 'saferepr', 'PrettyPrinter']

'''查看某个模块函数所具有的功能'''
print(help(pprint.pprint))

'''模块信息：文档'''
print(range.__doc__)
print(pprint.__doc__)

'''查看学习模块的源代码'''
print(pprint.__file__)
#out: C:\Python27\lib\pprint.pyc
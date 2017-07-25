# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/20 11:08
purpose:
"""
import numpy as np

# 字符串的格式化 format

# % 除去这种转换用%%
format = 'firtname: %s' + ' ' * 4 + 'lastname: %s'
value = ('li', 'chao')
print(format % value)

# 格式化浮点数:f
import numpy

format = 'pi的值（精确的5位）： %.5f'
print(format % np.pi)

# 如同unix的shell格式化方法: $

from string import Template

s = Template('$x glorious $x')
s.substitute(x='slurm')
print(s)
# 如果替换掉的部分是字符串一部分:${}
s = Template('$$ are ${x}ful')  # $$ = $
s.substitute(y='you', x='beauti')

s = Template('$x are $ful')
d = {}
d['x'] = 'you'
d['ful'] = 'beautiful'
s.substitute(d)  # '字典参数

# 符号，对齐和0的填充'''
print('pi: %10.3f' % np.pi)  # 字段宽度10
# out:pi:      3.142
print('pi: %010.3f' % np.pi)  # 0填充
# out:pi: 000003.142
print('pi: %-10.3f' % np.pi)  # 左对齐
# out：pi: 3.142

# 正数前面加上空格:数字对齐'''
print('xx:% 5d' % 10)
print('yy:%5d' % -10)
# xx:   10
# yy:  -10
# 不管正负都标出正负号'''
print('xx:%+5d' % 10)
print('yy:%+5d' % -10)
# xx:  +10
# yy:  -10

# *向右看齐,s宽度：
a3 = 'a' * 3
a6 = 'a' * 6
print('%*s' % (10, a3), '@', '%*s' % (10, a6), end='\n')


print("{1}121212{0}".format("one", "zero"))
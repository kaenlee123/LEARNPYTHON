# coding=UTF-8
'''
#Created on 2016年6月29日@author: kaen
'''
'''
##################################################  + *
'''
#序列乘法
x = [0] * 10
print(x)
#包含字符乘法的特殊输出
hello = input('输出内容：')
width = len(hello) +20
left_margin = int(input('输入离左边界距离：'))
height = int(input('盒子高度(奇数):'))
print(' '*left_margin +'+'+ '-'*width +'+')
for i in range((height-1)/2):
    print(' '*left_margin +'|'+ ' '*width +'|')
print(' '*left_margin +'|'+ ' '*10 + hello +' '*10 +'|')
for i in range((height-1)/2):
    print(' '*left_margin +'|'+ ' '*width +'|')
print(' '*left_margin +'+'+ '-'*width +'+')
'''
输出内容：hello lichoa !
输入离左边界距离：20
盒子高度(奇数):3
                    +----------------------------------+
                    |                                  |
                    |          hello lichoa !          |
                    |                                  |
                    +----------------------------------+

'''
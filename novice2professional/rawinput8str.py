# coding=UTF-8
'''
#Created on 2016年6月29日@author: kaen
'''
'''###############################input和raw_input'''
#input 会假设输入时合法的：字符窜
i = 1
while(i):
    try:
        name = eval(input('what is your name ?'))
        i = 0
    except:
        print('确认输入形式：\"xx\"')
        
print('Hello '+name+' !')

#raw_input: 会把所有数据以原始数据输入，然后将其放入字符串
num = input('enter a number:')
print(type(num))                                 #<type 'str'>
'''##############################################字符串'''
#很长str输出问题
print('''这是一个很长
字符串''')
#out:这是一个很长
#    字符串

#通过转义符把换行去除
print('''这是一个很长\
字符串''')
#out:这是一个很长字符串
'''
##############################################原始字符串
'''
#对于原始字符串：转义符（\）不会起作用
print('hello \nlichao')                          #\n换行符
print(r'hello \nlichao')                         #out：hello \nlichao
'''
##############################################unicode
普通字符以8位ASCII保存，unicode以16，这样就能显示很多字符
'''
print('糹丩乄 亇閁')
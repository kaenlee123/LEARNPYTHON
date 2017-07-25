# coding=UTF-8
'''
#Created on 2016年7月12日@author: kaen
'''
'''===================================文件模式
r: 读模式
w: 写入模式
a： 追加模式
+（可组合）： 读/写模式
b（可组合）: 二进制模式，处理声音剪辑，图片，就需要，’rb‘，用来读取一个二进制文件
'''
'''==================================缓冲
第3个参数为缓冲参数 0/False;无缓存直接对硬盘数据进行读写，比较慢
1/true; 缓存，使用flush/close才会对硬盘数据更新，程序运行较快
'''
f = open('firstfile.txt', 'w')
f.write('hello file\n')
f.write('hello file')
f.close()          # 完成一个文件的调用使用

f = open('firstfile.txt', 'r')   # 默认模式‘r’
print(f.read(4))         # 指定读取字符截数
print(f.read())          # 接下来读取剩下的

'''================================不按循序读取:(默认按循序从0（不断在变）开始)'''
f = open('firstfile.txt', 'w')
f.write('0123456789')
f.seek(5)                           # 位置跳到了第6个字符
f.write('hello')
f.close()

f = open('firstfile.txt', 'r')
print(f.read())
# out： 01234hello
print(f.read(2))      # 已经读取过了， 此句没有输出
f.close()

f = open('firstfile.txt', 'r')
print(f.read(2))        # 此处已经改变了0 的位置
# o ut: 01
print(f.read(2))        # 所以此处返回的是接着上面来   
# out: 23
print(f.tell())
# out: 4                 #返回相对于原始文件0所处的字符段位置
f.close()

'''==================================读写'''
winequality = open(r'E:\eclip\machineL\svm\winequality.txt')
'''读取当前行:当前0到一个\n'''
print(winequality.readline())
# out： ixed acidity;"volatile acidity";"citric acid";"residual sugar";"chlorides";"free sulfur dioxide";"total sulfur dioxide";"density";"pH";"sulphates";"alcohol";"quality"
'''读取所有行:列表形式保存'''
x = winequality.readlines()
print(type(x))

'''========================================内容迭代处理
按字节：
while 1：
   f.read(1)
   if not read(1):
      break
按行：改成readline（）

for i in f。read():
for line in f.readlines():

import fileinput
for line in fileinput.input(filename)

for line in list(open(xxx)):
'''



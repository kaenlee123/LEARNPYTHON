#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<>
  Purpose: 
  Created: 2016/11/14
  copyright: python 3.5.2
"""
from operator import itemgetter, attrgetter
#------------------------------sorted
a = [5, 2, 3, 1, 4]
sorted(a)  #有返回值，
print(a)
a = [5, 2, 3, 1, 4]
a.sort()   #没有返回值，直接在原基础上更改
print(a)
#-----------------------------对付更加复杂的
sorted({1: 'D', 2: 'B', 4: 'E', 5: 'A', 3: 'B'})

#------------------------------添加参数key
print((sorted("This is a test string from Andrew".split(), key=str.lower)))  #不区分大小写
student_tuples = [('jhon', 'A', 15),
                  ('jane', 'B', 12),
                  ('dave', 'B', 10)]
print((sorted(student_tuples, key=lambda student: student[2])))

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))
student_objects = [Student('john', 'A', 15),
                   Student('jane', 'B', 12),
                   Student('dave', 'B', 10),]
print((sorted(student_objects, key=lambda student: student.age)))


'''上面的key参数的使用非常广泛，因此python提供了一些方便的函数来使得 访问方法更加容易和快速。
operator模块有itemgetter，attrgetter，从 2.6开始还增加了methodcaller方法。使用这些方法，上面的操作将变得更 加简洁和快速：
'''
print('=====>>>.....')
print((sorted(student_tuples, key=itemgetter(2))))
print('=====>>>....')
print((sorted(student_objects, key=attrgetter('age'))))

'''operator模块还允许多级的排序，例如，先以grade，然后再以age来排 序：'''
print('=====>>>.....')
print((sorted(student_tuples, key=itemgetter(1, 2))))
print('=====>>>....')
print((sorted(student_objects, key=attrgetter('grade', 'age'))))

'''升序和降序
list.sort()和sorted()都接受一个参数reverse（True or False）来表示升序 或降序排序。例如对上面的student降序排序如下：
'''
'''排序被保证为稳定的。意思是说多个元素如果有相同的 key，则排序前后他们的先后顺序不变'''


'''更复杂地你可以构建多个步骤来进行更复杂的排序，例如对student数据先 以grade降序排列，然后再以age升序排列。
'''
print('=====>>>....')
s = sorted(student_objects, key=attrgetter('age'))     #降
print((sorted(s, key=attrgetter('grade'), reverse=True)))   #升

'''special example'''

x = [1, 3, 1, 2, 5, 2]
y = set(x)
print(y)  #out:{1, 2, 3, 5}
#不改变顺序输出
print((sorted(y, key=x.index))) #out:[1, 3, 2, 5]
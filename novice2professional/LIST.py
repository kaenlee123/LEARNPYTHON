# coding=UTF-8



# del
name = ['a', 'b', 'c']
del name[1]
print(name)

# list(iterable)
x = list('lichoa')

# 分片赋值
print(x)
x[1:-1] = []
print(x)

# 'append'''
x.append((1, 3))

# 'count():'''
x = list("121212")
print(x.count("1"))

# extend():新list扩展原有list
y = [1, 1, 1, 'new list']
x = ['old']
print(x + y)
print(x.extend(y))  # out: None没有返回值

# index:值对应index
print(x.index('old'))

# insert(object): return none
number = [1, 2, 3, 5, 6]
number.insert(3, 'four')
print("insert", number)

number = [1, 2, 3, 5, 6]
number.insert(3, ['four', 'four'])
print("inser a list", number)

# insert by index
number = [1, 2, 3, 5, 6]
number[3:3] = ['four', 'four']
print("inser flatten iterabel", number)

# pop(index):删除一个list中一个元素
p = [1, 2, 3]
print(p.pop(1), p)

# remove(value):从list中移除匹配到的值, find the firts and delete no return
x = [11, '32', 11, 3]
x.remove(11)
print("removed x", x)

# reverse():反转list # return none
number = [1, 2, 3, 5, 6]
print(reversed(number), number.reverse())

# sort():升序: return none
print(number.sort())

# coding=UTF-8
'''
#Created on 2016年7月11日@author: kaen  <生成器>
'''
nested = [[1,2],[3,4],5]
nested1 = [[1,2],[3,4],[5]]
'''===============================对比函数和生成器'''
def func(x):
    for sublist in x:
        for element in sublist:
            return element
print(func(nested))
#out ： 1    return终结了循环

def flatten(x):
    for sublist in x:
        for element in sublist:
            yield element
print(flatten(nested))
#out: <generator object flatten at 0x000000000314D288>
try:
    for i in flatten(nested):  #每调用一次就会终止在那次，并记下，下次就从终止的地方开始
        print(i, end=' ')
    print('\n')
except TypeError as e:
    print(e)
    for i in flatten(nested1):
        print(i, end=' ')
    print('\n')
#out:
#1 2 3 4 'int' object is not iterable
#1 2 3 4 5

'''===========================================递归生成器
每增加一层嵌套就加一个for，在不知道嵌套多少层时我们用递归。
上面已经知道对nested（树形结构列表）调用生成器时，出现typeError，如果转化成字符型就不会有错误
现在不装转化字符新如何输出'''
def newFlatten(x):
    try:
        for sublist in x:
            for element in sublist:
                yield element
    except:
        yield x
for i in newFlatten(nested):
    print(i, end=' ')
print('\n')
#out: 1 2 3 4 [[1, 2], [3, 4], 5]

nested = [[1,'sss'],[3,4],5]
def endedFlatten(x):
    try: #不要迭代类似字符串对象
        try:
            x + ' '  #如果x不是字符串就会出错
        except:
            pass      #如果不是字符串执行此句
        else:
            raise TypeError('字符串型') #如果是字符串就执行此句，抛出typeError错误
        for sublist in x:
            for element in endedFlatten(sublist):
                print('111111111',element)
                yield element
    except TypeError as e:
        print(e)
        print('222222222',x)
        yield x
print(list(endedFlatten(nested)))  
#out: [1, 'sss', 3, 4, 5]

'''========================================模拟生成器'''
def yyy(x):
    result = []
    try: #不要迭代类似字符串对象
        try:
            x + ' '  #如果x不是字符串就会出错
        except:
            pass      #如果不是字符串执行此句
        else:
            raise TypeError #如果是字符串就执行此句，抛出typeError错误
        for sublist in x:
            for element in yyy(sublist):
                print('1111')
                result.append(element)
    except:
        print('2222')
        result.append(x)
    return result
print('result:',yyy(nested))
# coding=UTF-8
'''
#Created on 2016年7月3日@author: kaen《字典》
'''

# pair tuple
items = [('name', 'gumby'), ('age', '42')]
d = dict(items)
print(d)

# 赋值创建
d = dict(name='gumby', age=42)
print(d)

# 更新
d = {}
d['name'] = 'gumby';
d['age'] = 42
print(d)

# 字典格式化'''
phone_book = {'andy': '12313', 'devao': '32324', 'jinady': '43423'}
print('andy\'s cell number: %(andy)s' % phone_book)

# 字典方法'''

# clear:无返回值
print(d.clear(), d)  # None {}

# fromkeys:使用指定的键建立字典
print({}.fromkeys(['name', 'age']))  # 默认：none

print({}.fromkeys(['name', 'age'], ['jily', '22']))  # 第二个参数改变默人填充

# get:访问字典，当遇到没有的键不会出错
print(phone_book.get('lichao'))

# has_key:查询键的存在性
print('liochoa' in phone_book)

# items:以list形式返回'''
print(phone_book.items())

# keys/values:以list返回相应值'''
print(enumerate(phone_book.keys()), list(enumerate(phone_book)))  # 以keys作为可迭代对象

# pop:删除给定键值，并返删除值
print(phone_book.pop('andy'))

# popitem:随机删除
print(phone_book.popitem())

# setdefault:根据键查询与get一样，不过查询不存在键，会创建且更新字典; 默认值none:并返回
print(phone_book.setdefault('andy'), phone_book)

print(phone_book, phone_book.setdefault('lichao', 'NA'))  # 第二个参数修改默认


# update:用一个字典更新另一个字典，已有就覆盖，没有回添加进去'''
x = {'lichao': '12313', 'ganh8u': '32432'}
phone_book.update(x)
print(phone_book)
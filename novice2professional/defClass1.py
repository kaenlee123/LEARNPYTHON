# coding=utf-8

'''=============================================Person类创建'''
import __main__
class Person:
    def __init__(self, name, job = 'NA', pay = '0'):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]   
    def raisePay(self, rate = 0.1, wyear=1):
        self.pay = str(int(self.pay) * pow(1+rate, wyear))
    def __str__(self):
        return '%12s  %6s  %6s' % (self.name, self.job, self.pay)
    
'''
执行和调用是不同的
if __name__ == __main__:用于判断代码是执行
利用以上信息我们可写测试
'''
if __name__ != __main__:
    Bob = Person('Bob Smith')         ##bob = Person()   #没有给默认参数时。参数为空会出错
    Sue = Person('Sue Jones', 'dev','1000')
    print('姓氏:', Bob.name.split()[-1])
    Sue.pay = str(1.1 * int(Sue.pay))
    print(Sue.pay)
    print(Sue.lastName())
    print(Sue)

'''制表输出'''
def strucPrint (instance):
    print('|' + '='*12 + '+' + '='*6 +'+' +'='*6 +'|')
    print('|' + 'name' +' '*(12-len('name')) + '|' + 'job'+' '*(6-len('job')) + '|' + 'pay'+' '*(6-len('pay'))+'|')
    for self in instance:
        print('|'+'-'*26 +'|')
        print('|' + self.name +' '*(12-len(self.name)) + '|' + self.job+' '*(6-len(self.job)) + '|' + self.pay+' '*(6-len(self.pay))+'|')
    print('|' + '='*12 + '+' + '='*6 +'+' +'='*6 +'|')
strucPrint([Bob, Sue])

'''====================================================子类'''
'''坏方法：如果涨工资的方式变了，比如基年变了，那就得改2地方：，麻烦'''
#class Manager(Person):
#    def raisePay(self, rate = 0.2, wyear=1):
#        self.pay = str(int(self.pay) * pow(1 + rate, wyear))
        
'''好方法'''
class Manager(Person):
    def __init__(self,name):
        Person.__init__(self, name, 'mgr', '5000')                   #重新定义构造函数
    def raisePay(self):
        Person.raisePay(self, rate=0.2)
Tom = Manager('Tom D.H')
print(Tom)



        
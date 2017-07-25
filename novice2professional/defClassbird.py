# coding=UTF-8
'''
#Created on 2016年7月10日@author: kaen
'''
'''=====================================调用绑定类'''
class bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry == True:
            print('ahahhaha!')
            self.hungry = False
        else:
            print('i have ate!')
b = bird()
print(b.eat())
print(b.eat())

class song_bird(bird):
    def __init__(self):
        self.sound = 'gagagaga!'
sb =song_bird()
try:
    print(sb.eat())
except AttributeError as e:
    print(e)
#out: song_bird instance has no attribute 'hungry'

class song_bird1(bird):
    def __init__(self):
        bird.__init__(self)
        self.sound = 'gaggaga'
sb1 = song_bird1()
print(sb1.eat())
#out: ahahhaha!

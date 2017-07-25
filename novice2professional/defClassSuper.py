# coding=UTF-8
'''
#Created on 2016年7月10日@author: kaen
'''
__metaclass__=type  #super函数只在新类中有用
class bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry == True:
            print('ahahhaha!')
            self.hungry = False
        else:
            print('i have ate!')
            
class song_bird(bird):
    def __init__(self):
        super(song_bird, self).__init__()
        self.sound = 'gaggaga'
sb = song_bird()
print(sb.eat())
#out: ahahhaha!
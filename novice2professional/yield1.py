# coding=UTF-8
'''
#Created on 2016年7月4日@author: kaen
'''
'''状态表示
state[0] = 3   :表示第一皇后在第1行的第4列
用元组表示状态
'''
'''寻找冲突'''
def conflict(state, nextX):   #nextX代表下一个皇后的水平位置
    nextY = len(state)        #nextY代表垂直位置
    for i in range(nextY):
        #如果前面一个皇后和下一个：水平一线（每行安排一个皇后：水平不一线），或者垂直一线，或者一条对角线上，就会冲突
        #下面只需要检查剩下2 者是否冲突
        #如果水平位置差值绝对值为0：在垂直一线上
        #nextY - i：行间距；如果水皮位置绝对值之差等于换后位置行间距说明在一条对角线上
        if abs(state[i] - nextX) in (0, nextY - i):
            return True          #存在冲突
    return False

'''基本情况：位置'''
def queens(num, state):         #num:皇后的总数   
    if len(state) == num -1:
        #还有最后一个皇后没放置
        for pos in range(num):
            if not conflict(state, pos):
                #没有冲突就返回水平位置值
                yield pos 
'''假设在4x4的方格上4个皇后，前3个水平位置为（0,3,1）求第4个的位置可能'''
print(list(queens(4, (0,3,1))))  #无解
print(list(queens(4, (1,3,0))))  #[2]

'''传递前面皇后位置给后面皇后'''
def queens_new(num, state = ()):
    for pos in range(num): 
        #依次选取每个皇后水平位置的坐标              
        if not conflict(state, pos):
            #和前面没有错误就往下走
            if len(state) == num-1 :
                #如果此处满足的是最后一个皇后，就生成所有最后满足的水平位置
                yield (pos,)
            else:
                #不是最后一个：把满足的位置添加进state里面，再次调用，也就是嵌套，不过参数要变
                for result in queens_new(num, state+(pos,)):
                    #生成
                    yield (pos,)+result
print(len(list(queens_new(8))))
        
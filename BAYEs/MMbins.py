# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/19 20:05
purpose:MM豆
"""

from itertools import permutations
import pandas as pd

bag01 = {'brown': 0.3, 'yellow': 0.2, 'red': 0.2, 'green': 0.1, 'orange': 0.1, 'tan': 0.1}
bag02 = {'blue': 0.24, 'green': 0.2, 'orange': 0.16, 'yellow': 0.14, 'red': 0.13, 'brown': 0.13}
pakages = {"bag01": bag01, "bag02": bag02, "bag03": bag02}
df = pd.DataFrame(pakages)
df.fillna(value=0, inplace=True)
print(df)


def Prob(colorBean, pakageName):
    """
    计算colorBean豆子来自pakageName的后验概率
    :param colorBean:
    :param pakageName:
    :return:
    """
    global pakages
    probColorBean = 0
    n = len(pakages)
    for pak in pakages:
        probColorBean += pakages[pak][colorBean]
    probColorBean /= n
    probColorBeanFromPakageName = 1 / n * pakages[pakageName][colorBean] / probColorBean
    return probColorBeanFromPakageName


def ProbMany(colorList, colorBean, pakageName):
    """
    从每个袋子取出一个豆子组成colorList（包不包含目标色），计算colorBean来自pakageName的概率
    :param colorList: 取出其他豆子的颜色
    :return:
    """
    global df
    m, n = df.shape
    print(m, n)
    # colorBean来自pakageName的概率：先验概率，事件已经发生
    PH = 1 / n
    # 计算似然度
    # #在前面的基础上计算剩下豆子发生情况的排列组合
    it = permutations(colorList)
    bags = list(df.columns)
    bags.remove(pakageName)
    data = []
    for indexs in it:
        temp = 1
        for i, b in zip(indexs, bags):
            temp *= df.at[i, b]
        data.append(temp)
    probColorList = sum(data)
    #colorBean和colorLISt的组合概率
    probColorList * df.at[colorBean, pakageName]
    # 计算P(H)P(X|H)


if __name__ == '__main__':
    print(("the probility of the yellow from prob0:", Prob('yellow', "bag01")))
    ProbMany(["green", "blue"], "yellow", "bag01")

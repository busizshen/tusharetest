#coding=utf-8
import numpy as np
import pandas as pd
import os
import tushare as ts
import buildModel.modelTest1 as md1
'''
选取一个因子，写一个模型
出现过 5日均线值 在20日均线值之下的，并且前后一天分别是下降趋势 和 上升趋势
'''
# 创建一个字典
dict = []

#取得因子下前十的股票
def getTopTenShare():
    loopGetCsv()
    print(dict)
    print('------------------------请购买以下股票-----------------------')
    for i in range(0,10):
        print(dict[i])

# 循环文件夹下所有的文件
def loopGetCsv():
    for root,dirs,files in os.walk('D:/pythonData/history'):
        for file in files:
            filename = '%s/%s' % (root, file)
            code = file[0:6]
            calcStandardDeviation(code,filename)

#找出是否记录中是否有ma5 小于 ma20的时候
def calcGeneWl2(dfs,code):
    # 循环遍历data 然后找出是否有ma5 小于 ma20的时候
    for indexs in dfs.index:
        ma5 = dfs.loc[indexs].values[0]
        ma20 = dfs.loc[indexs].values[1]
        #先找出ma5<ma20
        if ma5 < ma20 and indexs > 0:
            yestodayMa5 = dfs.loc[indexs-1].values[0]
            tomorrowMa5 = dfs.loc[indexs+1].values[0]
            yestodayMa5Rate = yestodayMa5/ma5
            tomorrowMa5 = tomorrowMa5/ma5
            if (yestodayMa5Rate > 1) and (tomorrowMa5 > 1):
                return code

    return 0



def calcStandardDeviation(code,filename):
    df = pd.read_csv(filename)
    #筛选是不是次新股
    shape0 = df.shape[0]
    if shape0 > 100:
        return
    # 按照索引来进行排序
    df = df.sort_index(ascending=True)
    df = df[['ma5','ma20']]

    # 计算
    code = calcGeneWl2(df,code)
    print("code=",code)
    if code != 0:
        # 向字典中加数据
        dict.append(code)


if __name__ == '__main__':
    getTopTenShare()

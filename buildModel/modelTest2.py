#coding=utf-8
import numpy as np
import pandas as pd
import os
import tushare as ts
import buildModel.modelTest1 as md1
'''
选取一个因子，写一个模型
1.首先选取近10日股价走势，如果股价一直增长，且幅度很大就选取（可以采用增长的加速度来衡量）
2.当短期的日均线从上到下交叉到中长期日均线，说明股价上涨，抖动幅度可以用作一个因子
'''
# 创建一个字典
dict = {}

#取得因子下前十的股票
def getTopTenShare():
    dict = loopGetCsv()
    print('------------------------请购买以下股票-----------------------')
    for i in range(0,10):
        print(dict[i])

# 循环文件夹下所有的文件
def loopGetCsv():
    for root,dirs,files in os.walk('D:/pythonData/history'):
        for file in files:
            filename = '%s/%s' % (root, file)
            code = file[7:13]
            calcStandardDeviation(code,filename)
    dict1 = sorted(dict.items(), key=lambda item: item[1])
    return dict1


# 选取文件中的指标
def readAllCsvToGetData(code,filename):
    df = pd.read_csv(filename,index_col='date')
    # 按照索引来进行排序  可以指定ascending=False进行降序排列
    df = df.sort_index(ascending=False)
    # 选取收盘价格 和 金额变动两个指标
    df = df[['close','price_change']]
    # shape 方法说明这个矩阵有几行 几列 亦是它的元组
    print('code:',code)
    acceleration = calcCPFluctuate(df)
    # 向字典中加数据
    dict[code] = acceleration


# 确定分析因子
def calcCPFluctuate(df):
    shape0 = df.shape[0]
    if shape0 < 10 :
        acceleration = 0
    else:
        acceleration = (df['close'][0]-df['close'][10])/df['close'][0]
    return acceleration

def calcGeneWl2(df):
    # 先计算10短上涨基率的倒数
    shape0 = df.shape[0]
    if shape0 < 10:
        acceleration = 0
    else:
        acceleration = df['close'][0]/(df['close'][0] - df['close'][10])

    # 再计算标准差
    col = df.iloc[:,0]
    arrs = col.values
    acceleration1 = np.std(arrs,ddof=1)

    #np.array(df.close).tolist()

    # 计算两数的积  积越小说明越好
    acceleration2 = acceleration * acceleration1
    return acceleration2



# 计算标准差（用来分析股票这一段时间区间内的离散程度）
def calcStandardDeviation(code,filename):
    df = pd.read_csv(filename,index_col='date')
    # 按照索引来进行排序
    df = df.sort_index(ascending=False)
    df = df[['close']]

    print(code)
    # 用所有的收盘价格计算标准差 与 10短上涨基率的倒数  乘积越小，说明上涨越快 越稳定
    gene = calcGeneWl2(df)
    if gene <= 0:
        gene = 9999
    # 向字典中加数据
    dict[code] = gene


if __name__ == '__main__':
    getTopTenShare()

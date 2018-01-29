#coding=utf-8
import tushare as ts #用来提取数据的包
import pandas as pd #进行分析数据的包
import datetime
import os
import numpy as np

dir = "D:/pythonData"

'''
这个demo用于取出股票数据，用于后续做数据模型使用
'''

# 循环用股票代码去取历史数据
def main():
    try:
        codeList = getCode()
        for index,code in enumerate(codeList):
            print(code,index)
            captureData(code)
    except Exception as err:
        print(err)


# 获取股票代码
def getCode():
    try:
        print('开始获取股票代码!!!')
        #获取今日数据
        pp = ts.get_today_all()
        #获取所有的股票代码
        codeList = np.array(pp.code).tolist()
        return codeList
    except Exception as err:
        print(err)

# 用于抓取股票的历史数据,并且存储到文件中
def captureData(code):
    try:
        dir1 = '%s/history'%(dir)
        nowTime = datetime.datetime.now().strftime("%Y%m%d")
        fileName = '%s/%s-%s.csv'%(dir1, code , nowTime)
        pp = ts.get_hist_data(str(code))

        if not os.path.exists(dir1):
            os.makedirs(dir1)
        pp.to_csv(fileName,encoding='utf-8')
    except Exception as err:
        print(err,code)


if __name__ == '__main__':
    main()

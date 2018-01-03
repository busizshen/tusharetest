import datetime

import os
import tushare as ts
import pandas as pd

import numpy as np
import tangguo.gongshi as gongshi
dir = "./data"
# 成长
def getCZNL(nian,ji):
    otherStyleTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    pp = ts.get_growth_data(nian, ji)
    fileName='%s/growth/%s-%s.csv'%(dir,str(nian)+str(ji),otherStyleTime)
    if not os.path.exists('%s/growth'%(dir)):
        os.makedirs('%s/growth'%(dir))
    pp.to_csv(fileName,encoding='utf-8')
# 今日数据
def getTodayAll():
    otherStyleTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    fileName='%s/todayAll/%s.csv'%(dir,otherStyleTime)
    pp = ts.get_today_all()
    if not os.path.exists('%s/todayAll'%(dir)):
        os.makedirs('%s/todayAll'%(dir))
    pp.to_csv(fileName,encoding='utf-8')
    return pp

def getSimpleTick(num):
    try:
        dir1='%s/simple'%(dir)
        otherStyleTime = datetime.datetime.now().strftime("%Y%m%d")
        fileName='%s/%s-%s.csv'%( dir1, num, otherStyleTime)
        pp = ts.get_hist_data(str(num))

        if not os.path.exists(dir1):
            os.makedirs(dir1)
        pp.to_csv(fileName,encoding='utf-8')
    except Exception as err:
        print(err,num)

def getSimpleDetilTick(num):
    dir1 = '%s/simple/%s'%(dir,num)
    # df = ts.get_tick_data('600848', date='2014-01-09')  #历史分笔接口
    otherStyleTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    fileName = '%s/%s.csv' % ( dir1, otherStyleTime)
    # pp = ts.get_hist_data(num)
    pp = ts.get_realtime_quotes(num) # 实时分笔接口
    pp = pp[::-1]
    if not os.path.exists(dir1):
        os.makedirs(dir1)
    pp.to_csv(fileName, encoding='utf-8')

#     大盘指数
def getindex():
    # df = ts.get_tick_data('600848', date='2014-01-09')  #历史分笔接口
    dir1 = '%s/index/'%(dir)

    otherStyleTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    fileName = '%s/%s.csv' % (dir, dir1, otherStyleTime)
    # pp = ts.get_hist_data(num)
    pp = ts.get_index()
    if not os.path.exists(dir1):
        os.makedirs(dir1)
    pp.to_csv(fileName, encoding='utf-8')
# getCZNL(2017,3)
# getTodayAll()
# getSimpleTick('600887')
# getSimpleDetilTick('600887')
# getSimpleDetilTick()

def genTick(num,df):
    # df = df[::-1]
    df=df.head(250)
    C= np.array(df.close).tolist()
    M= np.array(df.high).tolist()
    N= np.array(df.low).tolist()
    a = gongshi.gongshi(C, M, N)
    b=a.var8()


    if float(b)>=2.5:
        print("----------------",b,num)
        with open('test.txt', 'a') as fp:
            fp.write("----------------",b,num)
    row = [b, str(num)]
    return row

# if __name__ == '__main__':
#     fileName=r"data\todayAll\20180103103838.csv"
#     df = pd.read_csv(fileName)
#     codeList=np.array(df.code).tolist()
#     for index,code in enumerate(codeList):
#         print(code,index)
#         getSimpleTick(code)


def getAmt(ss):
    df = ts.get_realtime_quotes(ss)
    otherStyleTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    print(df[['name', 'price']])
    df.to_csv("test1%s.cvs"%(otherStyleTime),encoding='utf-8')


if __name__ == '__main__':
    fileName = r"data\todayAll\20180103103838.csv"
    otherStyleTime = datetime.datetime.now().strftime("%Y%m%d")

    df = pd.read_csv(fileName)
    codeList=np.array(df.code).tolist()
    aa =[]
    for index,code in enumerate(codeList):
        try:
            fileName = r"data\simple\%s-%s.csv"%(code,otherStyleTime)
            # print(fileName)
            df = pd.read_csv(fileName)
            row =genTick(code, df)
            aa.append(row)
        except Exception as e :
            print(index,code,"error",e)

    data = pd.DataFrame(aa)


    data=data.sort_values(0,ascending=False)
    data.columns = ['a','b']

    data.to_csv("test1.cvs",encoding='utf-8')
    data=data.head(20)
    getAmt(np.array(data.b).tolist())
    print(data.head(20))
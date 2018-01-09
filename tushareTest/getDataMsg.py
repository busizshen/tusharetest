import datetime
import os

import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tushare as ts
from matplotlib import style
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression

import tangguo.gongshi as gongshi

dir = "./data"


def dfvolume(fileName):
    df = pd.read_csv(fileName,index_col='date')
    df = df[::-1]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title(fileName)
    ax.set_xlabel("x value")
    ax.set_ylabel("y value")
    # date,open,high,close,low,volume,price_change,p_change,ma5,ma10,ma20,v_ma5,v_ma10,v_ma20,turnover
    # df['volume'].plot()
    df['close'] = df['close']
    df['close'].plot( color='r')
    # df['volume'].plot()
    style.use('ggplot')

    ax = fig.add_subplot(121)
    # ax.set_title("成交量")
    # date,open,high,close,low,volume,price_change,p_change,ma5,ma10,ma20,v_ma5,v_ma10,v_ma20,turnover
    # df['volume'].plot()
    # df['close'] = df['close'] ** 4
    # df['close'].plot()
    df['volume'].plot( color='m')
    style.use('ggplot')
    # ax.plot(df['close'], df.index, 'o')
    plt.show()

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

def jiaolongmairu(num,df):
    # df = df[::-1]
    df=df.head(250)
    C= np.array(df.close).tolist()
    M= np.array(df.high).tolist()
    N= np.array(df.low).tolist()
    a = gongshi.gongshi(C, M, N)
    b=a.jiaolongmairu()

    if float(b)>=2.5:
        print("----------------",b,num)
        with open('test.txt', 'a') as fp:
            fp.write("----------------",b,num)
    row = [b, str(num)]
    return row

def todayAll():
    df = getTodayAll()
    codeList=np.array(df.code).tolist()
    for index,code in enumerate(codeList):
        print(code,index)
        getSimpleTick(code)


def getAmt(ss,name):
    df = ts.get_realtime_quotes(ss)
    df["change"]= df.price.astype(float)/df.pre_close.astype(float)
    otherStyleTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    print(df[['name', 'price']])
    df.to_csv("getAmt%s%s.cvs"%(otherStyleTime,name),encoding='utf-8')
    print(df.info)
    return df

def ver8(fileName):
    otherStyleTime = datetime.datetime.now().strftime("%Y%m%d")
    otherStyleTime1 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    df = pd.read_csv(fileName)
    codeList = np.array(df.code).tolist()
    aa = []
    for index, code in enumerate(codeList):
        if len(str(code)) == 3:
            code = "000%s" % (code)
        if len(str(code)) == 4:
            code = "00%s" % (code)
        if len(str(code)) == 2:
            code = "0000%s" % (code)
        try:
            fileName = r"data\simple\%s-%s.csv" % (code, otherStyleTime)
            # print(fileName)
            df = pd.read_csv(fileName)
            print(df.shape)
            # if df.shape[0]<250:
            #     continue
            row = genTick(code, df)
            aa.append(row)
        except Exception as e:
            print(index, code, "error", e)
            with open('test.txt', 'a') as fp:
                fp.write("%s%s%s---------%s" % (index, code, "error", otherStyleTime1))

    data = pd.DataFrame(aa)

    data = data.sort_values(0, ascending=False)
    data.columns = ['a', 'b']
    data.to_csv("ver8%s.cvs"%(otherStyleTime1), encoding='utf-8')
    data = data.head(20)
    getAmt(np.array(data.b).tolist(),"ver8")
    print(data.head(20))

def jiaolongmairuList(fileName):
    otherStyleTime = datetime.datetime.now().strftime("%Y%m%d")
    otherStyleTime1 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    df = pd.read_csv(fileName)
    codeList = np.array(df.code).tolist()
    aa = []
    for index, code in enumerate(codeList):
        if len(str(code)) == 3:
            code = "000%s" % (code)
        if len(str(code)) == 4:
            code = "00%s" % (code)
        if len(str(code)) == 2:
            code = "0000%s" % (code)
        try:
            fileName = r"data\simple\%s-%s.csv" % (code, otherStyleTime)
            # print(fileName)
            df = pd.read_csv(fileName)
            print(df.shape)
            # if df.shape[0]<250:
            #     continue
            row = jiaolongmairu(code, df)
            aa.append(row)
        except Exception as e:
            print(index, code, "error", e)
            with open('test.txt', 'a') as fp:
                fp.write("%s%s%s---------%s" % (index, code, "error", otherStyleTime1))

    data = pd.DataFrame(aa)
    data = data.sort_values(0, ascending=False)
    data.columns = ['a', 'b']
    data.to_csv("jialongmairu%s.cvs"%(otherStyleTime1), encoding='utf-8')
    data = data.head(20)
    getAmt(np.array(data.b).tolist(),"jiaolong")
    print(data.head(20))

def currentP(fileName):
    df = pd.read_csv(fileName)
    codeList=np.array(df.code).tolist()
    aa =[]
    for index,code in enumerate(codeList):
        if len(str(code))==3:
            code="000%s"%(code)
        if len(str(code))==4:
            code="00%s"%(code)
        if len(str(code))==2:
            code="0000%s"%(code)
        aa.append(str(code))
    dd = getAmt(aa,"currentprice1")
    df["price1"]=dd.price
    # print(df["price1"])
    # print(dd["price"].astype(float))
    df["amt"]= df["price1"].astype(float)-df["price"].astype(float)
    df["rate"]= (df["price1"].astype(float)/df["price"].astype(float)-1)*100
    # print(df.info())
    print(df[['name','code','price','price1','amt','rate']])
    print(df[['rate']].head(10).fillna(0).apply(sum)/10.0)


def draw(fileName,otherStyleTime):
    df = pd.read_csv(fileName)
    codeList = np.array(df.code).tolist()
    aa = []
    for index, code in enumerate(codeList):
        if len(str(code)) == 3:
            code = "000%s" % (code)
        if len(str(code)) == 4:
            code = "00%s" % (code)
        if len(str(code)) == 2:
            code = "0000%s" % (code)
        aa.append(str(code))
        dir1 = '%s/simple' % (dir)
        fileName = '%s/%s-%s.csv' % (dir1, code, otherStyleTime)
        dfvolume(fileName)


if __name__ == '__main__':
    # todayAll()
    # fileName = r"data\todayAll\20180108151219.csv"
    # ver8(fileName)
    # jiaolongmairuList(fileName)
    fileName = r"getAmt20180108160129ver8.cvs"
    currentP(fileName)
    draw(fileName,'20180108')


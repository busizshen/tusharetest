import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY, date2num
import datetime


dir= r"D:\PycharmProjects\data"
def dataCleanIng(fileName,code,name):
    goog = pd.read_csv(fileName)
    # print(goog.head())
    goog=goog[::-1]
    goog["ma5"] = np.round(goog["close"].rolling(window=5, center=False).mean(), 2)
    goog["ma20"] = np.round(goog["close"].rolling(window=50, center=False).mean(), 2)
    goog.fillna(0)
    goog["code"]=code
    goog["name"] = name
    goog['ma5-20'] = goog['ma5'] - goog['ma20']
    goog['diff'] = np.sign(goog['ma5-20'])
    goog['signal'] = np.sign(goog['diff'] - goog['diff'].shift(1))
    goog=goog[::-1]
    return goog.head(1)


def allstockCode(fileName,otherStyleTime):

    df = pd.read_csv(fileName)
    codeList = np.array(df.code).tolist()
    aa = []
    p = pd.DataFrame()
    name = np.array(df.name).tolist()
    for index, code in enumerate(codeList):
        if len(str(code)) == 3:
            code = "000%s" % (code)
        if len(str(code)) == 4:
            code = "00%s" % (code)
        if len(str(code)) == 2:
            code = "0000%s" % (code)
        try:
            fileName = r"%s\simple\%s-%s.csv" % (dir,code, otherStyleTime)

            print(p.shape[0])
            if p.shape[0] == 0:
                p = dataCleanIng(fileName,code, name[index])
            else:
                p = np.row_stack((p, dataCleanIng(fileName,code, name[index])))
            p = pd.DataFrame(p)
            # dataCleanIng(fileName)

        except Exception as e:
            print(index, code, "error", e)
    p.to_excel("test.xls")
def allstock():
    fileName = r"%s\simple\000001-20180205.csv"%(dir)
    p = pd.DataFrame()
    print(p.shape[0])
    if p.shape[0] == 0:
        p = dataCleanIng(fileName)
    else:
        p.append(dataCleanIng(fileName))
    print(p)

if __name__ == '__main__':
    fileName=r"%s\todayAll\20180207164933.csv"%(dir)
    # otherStyleTime = datetime.datetime.now().strftime("%Y%m%d")
    otherStyleTime ="20180205"
    allstockCode(fileName,otherStyleTime)


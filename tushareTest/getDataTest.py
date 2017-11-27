import datetime
import tushare as ts

def getData(num):
    otherStyleTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    pp = ts.get_hist_data(num)
    pp.to_csv('./data/%s-%s.csv'%(num,otherStyleTime),encoding='utf-8')

getData('002049')

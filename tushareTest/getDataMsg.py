import datetime

import os
import tushare as ts
# 成长
def getCZNL(nian,ji):
    otherStyleTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    pp = ts.get_growth_data(nian, ji)
    if not os.path.exists('./data/growth'):
        os.makedirs('./data/growth')
    pp.to_csv('./data/growth/%s-%s.csv'%(str(nian)+str(ji),otherStyleTime),encoding='utf-8')
# 今日数据
def getTodayAll():
    otherStyleTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    pp = ts.get_today_all()
    if not os.path.exists('./data/todayAll'):
        os.makedirs('./data/todayAll')
    pp.to_csv('./data/todayAll/%s.csv'%(otherStyleTime),encoding='utf-8')

def getSimpleTick(num):
    dir='./data/simple'
    otherStyleTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    pp = ts.get_hist_data(num)
    if not os.path.exists(dir):
        os.makedirs(dir)
    pp.to_csv('%s/%s-%s.csv'%(dir,num,otherStyleTime),encoding='utf-8')

def getSimpleDetilTick(num):
    dir = './data/simple/%s'%(num)
    # df = ts.get_tick_data('600848', date='2014-01-09')  #历史分笔接口
    otherStyleTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # pp = ts.get_hist_data(num)
    pp = ts.get_realtime_quotes(num) # 实时分笔接口
    if not os.path.exists(dir):
        os.makedirs(dir)
    pp.to_csv('%s/%s-%s.csv' % (dir, num, otherStyleTime), encoding='utf-8')

#     大盘指数
def getSimpleDetilTick():
    # df = ts.get_tick_data('600848', date='2014-01-09')  #历史分笔接口
    dir = './data/index/'
    otherStyleTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # pp = ts.get_hist_data(num)
    pp = ts.get_index()
    if not os.path.exists(dir):
        os.makedirs(dir)
    pp.to_csv('%s/%s.csv' % (dir, otherStyleTime), encoding='utf-8')
# getCZNL(2017,3)
# getTodayAll()
# getSimpleTick('600887')
# getSimpleDetilTick('600887')
getSimpleDetilTick()
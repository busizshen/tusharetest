import tushare as ts
import pandas as pd 
import datetime
import sys,codecs
def getAllTickToday():
    date1=ts.get_today_all()
    otherStyleTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    print(otherStyleTime)
    fileName='allTick%s.csv'%otherStyleTime
    date1.to_csv(fileName,encoding='utf-8')
    print(fileName)

    # fileObj = codecs.open("1.xml",'w',"utf-8")
    # fileObj.write("test\n")
    with  codecs.open("filename.txt",'a',"utf-8") as fileObj:
        fileObj.write("%s\n"%fileName)
    return fileName
# ,code,name,changepercent,trade,open,high,low,settlement,volume,turnoverratio,amount,per,pb,mktcap,nmc
fileName="allTick20171019182610.csv"
lines = pd.read_csv(fileName)
# print(lines['code'])
# print(lines['code'].ix[0])
print(lines.ix[0])


# ts.get_hist_data('600848')
# date：日期
# open：开盘价
# high：最高价
# close：收盘价
# low：最低价
# volume：成交量
# price_change：价格变动
# p_change：涨跌幅
# ma5：5日均价
# ma10：10日均价
# ma20:20日均价
# v_ma5:5日均量
# v_ma10:10日均量
# v_ma20:20日均量
# turnover:换手率[注：指数无此项]



# date1=datetime.timedelta(days = -100)
# print((datetime.datetime.now() - datetime.timedelta(days = 100)).strftime("%Y-%m-%d"))

# pd=ts.get_concept_classified()

# hs300=ts.get_hs300s()
# hs300.to_csv('hs300.csv',encoding='utf-8')
# print(hs300)
# zz50=ts.get_sz50s()
# hs300.to_csv('zz50.csv',encoding='utf-8')

# lines = pd.read_csv('hs300.csv',index_col=0)
# print(lines)

# 002230
# pp = ts.get_hist_data('600848')
# pp.to_csv('600848.csv',encoding='utf-8')

# pp = ts.get_hist_data('002230')
# pp.to_csv('002230.csv',encoding='utf-8')

# lines = pd.read_csv('002230.csv')
# print(lines)
# print(lines.shape[0])
# lines.sort_index(axis=1, ascending=False) 

# index=[]
# for i in range(0,700):
#     # print(i)
#     index.append(i)
# index.reverse()
# print(index)
# lines1=lines.reindex(index)

# print(lines[2:3] )

# import datetime

# (datetime.datetime.now() - datetime.timedelta(days = 100)).strftime("%Y-%m-%d")
# string转datetime

#             str = '2012-11-19'

#             date_time = datetime.datetime.strptime(str,'%Y-%m-%d')

#             date_time

# datetime.datetime(2012,11,19,0,0)
# datetime转string

#             date_time.strftime('%Y-%m-%d')

# '2012-11-19'
# datetime转时间戳

#             time_time = time.mktime(date_time.timetuple())

#             time_time

# 1353254400.0
# 时间戳转string

#             time.strftime('%Y-%m-%d',time.localtime(time_time))

# '2012-11-19'
# date转datetime

#             date = datetime.date.today()

#             date

#             datetime.date(2012,11,19)

#             datetime.datetime.strptime(str(date),'%Y-%m-%d') #将date转换为str，在由str转换为datetime

#             datetime.datetime(2012,11,19,0,0)


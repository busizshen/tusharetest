import datetime
import tushare as ts

def getCZNL(nian,ji):
    otherStyleTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    pp = ts.get_growth_data(nian, ji)
    pp.to_csv('./data/growth/%s-%s.csv'%(str(nian)+str(ji),otherStyleTime),encoding='utf-8')

getCZNL(2017,3)
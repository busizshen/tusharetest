import tushare as ts
import pandas as pd
# from pymysql.constants.FIELD_TYPE import VARCHAR
from sqlalchemy import create_engine, NVARCHAR, Float, Integer,VARCHAR
import pymysql,sys
import numpy as np
import datetime
# ,code,name,changepercent,trade,open,high,low,settlement,volume,turnoverratio,amount,per,pb,mktcap,nmc
# df = ts.get_today_all()
class tuShareDataTool:
    def __init__(self):
        if "MySQLdb" not in sys.modules:
            print("initMysqlDb")
            pymysql.install_as_MySQLdb()
        else:
            print("don't initMysqlDb")
        self.engine=create_engine('mysql://root:123456@127.0.0.1/stock_data?charset=utf8')

    def allStockNumToMysql(self):
        # fileName=r"D:\PycharmProjects\tusharetest\tushareTest\data\todayAll\20180202175033.csv"
        # df = pd.read_csv(fileName)
        df = ts.get_today_all()
        df=df[["code","name"]]
        df['code'] = df['code'].apply(lambda x: str(x))
        tableName="t_all_stock_num"
        # df = ts.get_hist_data('000875')
        engine = self.engine
        df.to_sql(tableName, engine, if_exists='replace', dtype={'date': VARCHAR(20) ,'code': VARCHAR(10)})

    def pdfToMysql(self, df, tableName):
        engine =self.engine
        df.to_sql(tableName, engine, if_exists='replace',dtype={'date': VARCHAR(20)})
        return engine

    def mapping_df_types(self,df):
        dtypedict = {}
        for i, j in zip(df.columns, df.dtypes):
            print(i,j)
            if "object" in str(j):
                dtypedict.update({i: NVARCHAR(length=50)})
            if "float" in str(j):
                dtypedict.update({i: Float(precision=2, asdecimal=True)})
            if "int" in str(j):
                dtypedict.update({i: Integer()})
        return dtypedict


    # df1 = pd.read_sql('tick_data', engine, index_col='date', parse_dates=['date'])
    def allStockDataToMysql(self):
        tableName="t_all_stock_num"
        df = pd.read_sql(tableName, self.engine)
        codeList = np.array(df.code).tolist()
        for index, code in enumerate(codeList):
            print(code, index)
            self.getSimpleTick(code)

    def getSimpleTick(self,num):
        df = ts.get_hist_data(str(num))
        # df = df.convert_objects(convert_numeric=True)
        df["code"] = num
        engine = self.pdfToMysql(df, 't_one_stock_history_%s' % (str(num)))
        # try:
        #     df = ts.get_hist_data(str(num))
        #     # df = df.convert_objects(convert_numeric=True)
        #     df["code"]=num
        #     print(df)
        #     engine = self.pdfToMysql(df, 't_one_stock_history_%s'%(str(num)))
        # except Exception as err:
        #     print(err, num)



if __name__ == '__main__':
    data=tuShareDataTool()
    # data.allStockNumToMysql()
    data.allStockDataToMysql()
    # data.getSimpleTick("603998")

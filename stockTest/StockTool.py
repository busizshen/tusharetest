import codecs
import datetime
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tushare as ts
from matplotlib import style
from tushareTest.kerasTest import test1
import tangguo.gongshi as gongshi
import time
dir = "D:\PycharmProjects\data"
class StockTool:

    def getDir(self):
        print(dir)
        with codecs.open("log.txt", 'w', "utf-8") as fileObj:
            fileObj.write("123456\n")
    def genCode(self,code):
        if len(str(code)) == 1:
            code = "00000%s" % (code)
        if len(str(code)) == 3:
            code = "000%s" % (code)
        if len(str(code)) == 4:
            code = "00%s" % (code)
        if len(str(code)) == 2:
            code = "0000%s" % (code)
        return code

    def dfvolume(self,fileName):
        df = pd.read_csv(fileName,index_col='date')
        df = df[::-1]

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_title(fileName)
        ax.set_xlabel("x value")
        ax.set_ylabel("y value")
        # date,open,high,close,low,volume,price_change,p_change,ma5,ma10,ma20,v_ma5,v_ma10,v_ma20,turnover
        # df['volume'].plot()
        # df['close'] = df['close']
        # df['close'].plot( color='r')
        df['volume'].plot( color='m')
        # style.use('ggplot')

        ax = fig.add_subplot(121)
        ax.set_title("成交量")
        # date,open,high,close,low,volume,price_change,p_change,ma5,ma10,ma20,v_ma5,v_ma10,v_ma20,turnover
        # df['volume'].plot()
        ax.set_xlabel("riqi")
        df['close'] = df['close'] ** 4
        df['close'].plot( color='r')
        # df['volume'].plot( color='m')
        # style.use('ggplot')
        # ax.plot(df['close'], df.index, 'o')
        plt.show()

    # 成长
    def getCZNL(self,nian,ji):
        otherStyleTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        pp = ts.get_growth_data(nian, ji)
        fileName='%s/growth/%s-%s.csv'%(dir,str(nian)+str(ji),otherStyleTime)
        if not os.path.exists('%s/growth'%(dir)):
            os.makedirs('%s/growth'%(dir))
        pp.to_csv(fileName,encoding='utf-8')
    # 今日数据
    def getTodayAll(self):
        otherStyleTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        fileName='%s/todayAll/%s.csv'%(dir,otherStyleTime)
        print(fileName)
        pp = ts.get_today_all()
        if not os.path.exists('%s/todayAll'%(dir)):
            os.makedirs('%s/todayAll'%(dir))
        pp.to_csv(fileName,encoding='utf-8')
        with codecs.open("log.txt", 'w', "utf-8") as fileObj:
            fileObj.write("%s\n"%(fileName))
        return pp

    def getSimpleTick(self,num: object) -> object:
        try:
            dir1='%s/simple'%(dir)
            otherStyleTime = datetime.datetime.now().strftime("%Y%m%d")
            fileName='%s/%s-%s.csv'%( dir1, num, otherStyleTime)
            pp = ts.get_hist_data(str(num))

            if not os.path.exists(dir1):
                os.makedirs(dir1)
            pp.to_csv(fileName,encoding='utf-8')
            return pp
        except Exception as err:
            print(err,num)

    def getSimpleDetilTick(self,num):
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
    def getindex(self):
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

    def genTick(self,num,df):
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

    def jiaolongmairu(self,num,df):
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

    def todayAll(self):
        df = self.getTodayAll()
        codeList=np.array(df.code).tolist()
        cixin=[]
        for index,code in enumerate(codeList):
            print(code,index)
            dd= self.getSimpleTick(code)

        #     if dd.shape[0] > 20 and dd.shape[0] < 50:
        #         cixin.append([code])
        #
        # cixin = pd.DataFrame(cixin)
        # cixin.to_excel("cixin.xls")

    def todayAllWithExcel(self):
        df = self.getTodayAll()
        codeList=np.array(df.code).tolist()
        cixin=[]
        for index,code in enumerate(codeList):
            print(code,index)
            dd= self.getSimpleTick(code)

            if dd.shape[0] > 20 and dd.shape[0] < 50:
                cixin.append([code])

        cixin = pd.DataFrame(cixin)
        cixin.to_excel("cixin.xls")


    def getAmt(self,ss,name):
        df = ts.get_realtime_quotes(ss)
        df["change"]= df.price.astype(float)/df.pre_close.astype(float)
        otherStyleTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        print(df[['name', 'price']])
        df.to_csv("getAmt%s%s.cvs"%(otherStyleTime,name),encoding='utf-8')
        print(df.info)
        return df

    def ver8(self,fileName):
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
                fileName = r"%s\simple\%s-%s.csv" % (dir,code, otherStyleTime)
                # print(fileName)
                df = pd.read_csv(fileName)
                print(df.shape)
                # if df.shape[0]<250:
                #     continue
                row = self.genTick(code, df)
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
        self.getAmt(np.array(data.b).tolist(),"ver8")
        print(data.head(20))
        return data


    def jiaolongmairuList(self,fileName,otherStyleTime):
        # otherStyleTime = datetime.datetime.now().strftime("%Y%m%d")
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
                fileName = r"%s\simple\%s-%s.csv" % (dir,code, otherStyleTime)
                # print(fileName)
                df = pd.read_csv(fileName)
                print(df.shape)
                # if df.shape[0]<250:
                #     continue
                row = self.jiaolongmairu(code, df)
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
        self.getAmt(np.array(data.b).tolist(),"jiaolong")
        print(data.head(20))

    def currentP(self,fileName):
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
        dd = self.getAmt(aa,"currentprice1")
        df["price1"]=dd.price
        # print(df["price1"])
        # print(dd["price"].astype(float))
        df["amt"]= df["price1"].astype(float)-df["price"].astype(float)
        df["rate"]= (df["price1"].astype(float)/df["price"].astype(float)-1)*100
        df["rate1"]= (df["price1"].astype(float)/df["pre_close"].astype(float)-1)*100

        # print(df.info())
        print(df[['name','code','price','price1','amt','rate','rate1']])
        print(df[['rate']].head(5).fillna(0).apply(sum)/5.0)

    def bankCurrentP(self):
        aa =['601398','601288','601939','601988']
        dd = self.getAmt(aa,"bankcurrentprice1")
        print(dd)


    def draw(self,fileName,otherStyleTime):
        df = pd.read_csv(fileName)
        codeList = np.array(df.code).tolist()
        aa = []
        for index, code in enumerate(codeList):
            code = self.genCode(code)
            aa.append(str(code))
            dir1 = '%s/simple' % (dir)
            fileName = '%s/%s-%s.csv' % (dir1, code, otherStyleTime)
            self.dfvolume(fileName)

    def doservice(self,num,df,servicename):
        # df = df[::-1]
        df=df.head(250)
        C= np.array(df.close).tolist()
        M= np.array(df.high).tolist()
        N= np.array(df.low).tolist()
        a = gongshi.gongshi(C, M, N)
        b=getattr(a, servicename)()
        print(b)
        if float(b)>=2.5:
            print("----------------",b,num)
            with open('test.txt', 'a') as fp:
                fp.write("----------------",b,num)
        row = [b, str(num)]
        return row

    def ver8M250(self,fileName ):
        serviceNmae='ver8M250'
        otherStyleTime = datetime.datetime.now().strftime("%Y%m%d")
        # otherStyleTime = "20180128"
        otherStyleTime1 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        df = pd.read_csv(fileName)
        codeList = np.array(df.code).tolist()
        aa = []
        for index, code in enumerate(codeList):
            code = self.genCode(code)
            try:
                fileName = r"%s\simple\%s-%s.csv" % (dir,code, otherStyleTime)
                # print(fileName)
                df = pd.read_csv(fileName)
                # test = test1(df)
                # test.trade()
                print(df.shape)
                if df.shape[0]<250:
                    continue
                # row = doservice(code, df,'var4')
                # row = doservice(code, df, 'jiaolongchugong')
                row = self.doservice(code, df, 'var8')
                aa.append(row)
            except Exception as e:
                print(index, code, "error", e)


        data = pd.DataFrame(aa)

        data = data.sort_values(0, ascending=False)
        data.columns = ['a', 'b']
        data.to_csv("var8M250%s.cvs"%(otherStyleTime1), encoding='utf-8')
        data = data.head(20)
        self.getAmt(np.array(data.b).tolist(),serviceNmae)
        print(data.head(20))
        return data





    def teststd(self,fileName ):
        serviceNmae='ver8M250'
        # otherStyleTime = datetime.datetime.now().strftime("%Y%m%d")
        otherStyleTime = "20180129"
        otherStyleTime1 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        df = pd.read_csv(fileName)
        codeList = np.array(df.code).tolist()
        aa = []
        for index, code in enumerate(codeList):
            code = self.genCode(code)
            try:
                fileName = r"%s\simple\%s-%s.csv" % (dir,code, otherStyleTime)
                # print(fileName)
                df = pd.read_csv(fileName)
                # test = test1(df)
                # test.trade()
                print(df.shape)
                if df.shape[0]<250:
                    continue
                aa.append(df["close"]/df['close'].min())
            except Exception as e:
                print(index, code, "error", e)


        data = pd.DataFrame(aa)
        data = data.sort_values(0, ascending=False)
        data.to_csv("test%s.cvs"%(otherStyleTime1), encoding='utf-8')
        return data

    def test20(self,fileName ):
        otherStyleTime = datetime.datetime.now().strftime("%Y%m%d")
        df = pd.read_csv(fileName)
        codeList = np.array(df.code).tolist()

        name = np.array(df.name).tolist()
        for index, code in enumerate(codeList):
            code = self.genCode(code)
            fileName = r"%s\simple\%s-%s.csv" % (dir,code, otherStyleTime)
            # print(fileName)
            df = pd.read_csv(fileName)

            if df.shape[0] < 250:
                continue
            print(name[index],code)
            # test = test1(df,code,name[index])
            # test.trade()
            # test.test()
            from tushareTest.drawKLine import draw
            draw(fileName, code, name[index])

    def drawAll(self,fileName ,otherStyleTime):
        df = pd.read_csv(fileName)
        codeList = np.array(df.code).tolist()
        aa = []
        name = np.array(df.name).tolist()
        for index, code in enumerate(codeList):
            code = self.genCode(code)
            try:
                fileName = r"%s\simple\%s-%s.csv" % (dir,code, otherStyleTime)
                # print(fileName)
                from tushareTest.drawKLine import draw
                draw(fileName, code, name[index])
            except Exception as e:
                print(index, code, "error", e)

    def tradeAll(self,fileName,otherStyleTime):
        df = pd.read_csv(fileName)
        codeList = np.array(df.code).tolist()
        aa = []
        name = np.array(df.name).tolist()
        for index, code in enumerate(codeList):
            code = self.genCode(code)
            aa.append(str(code))
            dir1 = '%s/simple' % (dir)
            fileName = '%s/%s-%s.csv' % (dir1, code, otherStyleTime)
            self.tradeOne(fileName, code, name[index])
            from tushareTest.drawKLine import draw
            draw(fileName, code, name[index])

    def tradeOne(self,fileName,code,name ):
        df = pd.read_csv(fileName)
        test = test1(df,code,name)
        test.trade()
        test.test()


    # df = ts.get_tick_data('600848',date='2014-01-09')

    def get_tick_data_his(self,code ,date ):

        time.sleep(5)
        # df = ts.get_tick_data(code, date=date)
        dir1='%s/simple/code/%s'%(dir ,code)
        otherStyleTime = datetime.datetime.now().strftime("%Y%m%d")


        fileName='%s/%s-%s.csv'%(dir1,code,date)
        if not os.path.exists(dir1):
            os.makedirs(dir1)
        if os.path.exists(fileName):
            pass
        pp = ts.get_tick_data(code, date=date)
        pp.to_csv(fileName,encoding='utf-8')


    def ssfb(self,code,fileName): #实时分比
        df = pd.read_csv(fileName)
        dates = df.date.values
        for date in dates:
            self.get_tick_data_his(code, date)



if __name__ == '__main__':
    stockTool = StockTool()
    # stockTool.getDir()
    stockTool.todayAll()
    # df = getTodayAll()
    # df.to_excel("today.xls")
    # code= "601398"
    # otherStyleTime = datetime.datetime.now().strftime("%Y%m%d")
    # df = ts.get_today_ticks(code)
    # df.to_excel("%s-%s.xls"%(code,otherStyleTime),encoding="utf-8")
    # stockTool.todayAll()
    # pass

    # fileName = r"%s\todayAll\20180326165425.csv"%(dir)
    # data1= teststd(fileName)
    # test20(fileName)
    # data2 =ver8(fileName)
    # data3= pd.merge(data1, data2, on=["b"])
    # print(data3)
    # data3.to_csv("%s3.cvs", encoding='utf-8')
    # jiaolongmairuList(fileName,'20180119')
    # fileName = r"getAmt20180327152757ver8.cvs"
    # otherStyleTime = datetime.datetime.now().strftime("%Y%m%d")

    # otherStyleTime = "20180205"
    # currentP(fileName)
    # drawAll(fileName,otherStyleTime)
    # bankCurrentP()
    # fileName = r"getAmt20180126132842ver8M250.cvs"
    # test20(fileName)

    # fileName = r"D:\PycharmProjects\data\simple\600069-20180326.csv"
    # code='600069'
    # # print(fileName)
    # ssfb(code,fileName)
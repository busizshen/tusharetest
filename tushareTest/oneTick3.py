import datetime

import numpy as np
import pandas as pd
import tushare as ts
from matplotlib import style
from sklearn import cross_validation
from sklearn.linear_model import LinearRegression


def getData(num):
    otherStyleTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    pp = ts.get_hist_data(num)
    pp.to_csv('%s-%s.csv'%(num,otherStyleTime),encoding='utf-8')
def number_to_flag(number):
    if number > 0:
        return 1
    elif number == 0:
        return 0
    else:
        return -1

def do_something(x):
    x= lambda x: 1 if x > 0 else (-1 if x < 0 else 0)
    print(x)
    return x
def trainData(fileName):
    df = pd.read_csv(fileName,index_col='date')

    df=df.sort_index()
    df = df[['open', 'high', 'close', 'low', 'volume', 'price_change' ,'p_change', 'ma5', 'ma10', 'ma20' ,'v_ma5', 'v_ma10', 'v_ma20', 'turnover']]
    print(df.shape[0],df.shape[1])
    index =df.shape[0]
    y = df[['price_change']].ix[1:df.shape[0]]
    # y[['price_change'] ]= y[['price_change'] ].map(lambda x: do_something(x), y[['price_change']])
    y['price_change'] = df['price_change'].map(number_to_flag)
    df1 = np.array(df.drop(['price_change','p_change'], 1)[0:df.shape[0]-1])
    print(df.head(5))
    print(y.head(5))
    print(df1[0:5])


    X_train, X_test, y_train ,y_test = cross_validation.train_test_split(df1,y,test_size=0.3)

    clf = LinearRegression()
    clf.fit(X_train,y_train)
    accuracy = clf.score(X_test,y_test)

    print(accuracy,"---------score------")



    style.use('ggplot')


# getData('600887')
trainData('600887-20171023134838.csv')


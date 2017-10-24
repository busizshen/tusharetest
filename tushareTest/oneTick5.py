import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from sklearn import svm
import tushare as ts
import pandas as pd
import numpy as np
import datetime
from pandas_datareader import data as web
import math
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression,LassoLarsIC
from sklearn.externals import joblib
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
def getData(num):
    otherStyleTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    pp = ts.get_hist_data(num)
    pp.to_csv('%s-%s.csv'%(num,otherStyleTime),encoding='utf-8')

def do_something(x):
    x= lambda x: 1 if x > 0 else (-1 if x < 0 else 0)
    print(x)
    return x
def trainData(fileName):
    df = pd.read_csv(fileName,index_col='date')

    df=df.sort_index()
    df = df[['open', 'high', 'close', 'low', 'volume', 'price_change' ,'p_change', 'ma5', 'ma10', 'ma20' ,'v_ma5', 'v_ma10', 'v_ma20', 'turnover']]

    df = df[['open', 'high', 'low', 'close', 'volume']]
    df['HL_PCT'] = (df['high'] - df['low']) / df['close'] * 100.0
    df['PCT_change'] = (df['close'] - df['open']) / df['open'] * 100.0
    df = df[['close', 'HL_PCT', 'PCT_change', 'volume']]
    # print(df.head())
    forecast_col = 'close'
    df.fillna(value=-99999, inplace=True)
    # forecast_out = int(math.ceil(0.01 * len(df)))
    forecast_out = 1
    # ??forecast_out???
    df['label'] = df[forecast_col].shift(-forecast_out)

    print(df.shape)
    print(df)
    X = np.array(df.drop(['label'], 1))

    X = preprocessing.scale(X)

    X_lately = X[-forecast_out:]
    X = X[:-forecast_out]
    df.dropna(inplace=True)
    print(X)
    print(X_lately)
    y = np.array(df['label'])
    # print(y)
    print(X.shape)
    print(y.shape)
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

    clf = LassoLarsIC(max_iter=100)
    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test)
    joblib.dump(clf, "%s.m"%fileName)
    print(accuracy,"---------score------")

    forecast_set = clf.predict(X_lately)

    print(forecast_out)
    style.use('ggplot')
    df['Forecast'] = np.nan
    last_date = df.iloc[-1].name

    date_time = datetime.datetime.strptime(last_date,'%Y-%m-%d')
    last_unix = date_time.timestamp()
    one_day = 86400
    next_unix = last_unix + one_day
    print(forecast_set)
    for i in forecast_set:
        next_date = datetime.datetime.fromtimestamp(next_unix)
        next_unix += 86400
        df.loc[next_date] = [np.nan for _ in range(len(df.columns) - 1)] + [i]
    print(df.tail(forecast_out))

    df['close'].plot()
    df['Forecast'].plot()
    plt.show()

def realData(fileName):
    df = pd.read_csv(fileName,index_col='date')

    # df=df.sort_index()
    df = df[['open', 'high', 'close', 'low', 'volume', 'price_change' ,'p_change', 'ma5', 'ma10', 'ma20' ,'v_ma5', 'v_ma10', 'v_ma20', 'turnover']]

    df = df[['open', 'high', 'low', 'close', 'volume']]
    df['HL_PCT'] = (df['high'] - df['low']) / df['close'] * 100.0
    df['PCT_change'] = (df['close'] - df['open']) / df['open'] * 100.0
    df = df[['close', 'HL_PCT', 'PCT_change', 'volume']]
    # print(df.head())
    forecast_col = 'close'
    df.fillna(value=-99999, inplace=True)
    # forecast_out = int(math.ceil(0.01 * len(df)))
    forecast_out = 1
    # ??forecast_out???
    df['label'] = df[forecast_col].shift(-forecast_out)

    print(df.shape)
    print(df)
    X = np.array(df.drop(['label'], 1))

    X = preprocessing.scale(X)

    X_lately = X[0:1]
    X = X[:-forecast_out]
    df.dropna(inplace=True)
    return X_lately

# getData('002183')
trainData('002183-20171024131142.csv')

# clf.fit(X_train, y_train)
# accuracy = clf.score(X_test, y_test)
# print(accuracy,"---------score------")

clf = joblib.load("002183-20171024131142.csv.m")
X_lately=realData("002183-20171024131142.csv");
forecast_set = clf.predict(X_lately)
print(forecast_set)
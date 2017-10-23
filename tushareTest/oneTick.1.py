import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from sklearn import svm

import pandas as pd
import numpy as np
import datetime
# import pandas.io.data as web
from pandas_datareader import data as web
import math
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

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

df = pd.read_csv('002230.csv')
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
ff=df['date']

print(ff.size)

df = df[['open',  'high',  'low',  'close', 'volume','date']]
df['HL_PCT'] = (df['high'] - df['low']) / df['close'] * 100.0
df['PCT_change'] = (df['close'] - df['open']) / df['open'] * 100.0
df = df[['close', 'HL_PCT', 'PCT_change', 'volume','date']]
# df['date'] = df['date'] #datetime.datetime.strptime(df['date'], "%Y-%m-%d")
df['date'] =  pd.to_datetime(df['date'], format='%Y-%m-%d')
df['date'] = pd.to_numeric(df['date'])

#print(df.head())
print(df[2:3]  )
forecast_col = 'close'
df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)

print(df.shape)
print(df.tail())
X = np.array(df.drop(['label'], 1))


X = preprocessing.scale(X)

X_lately = X[-forecast_out:]
X = X[:-forecast_out]
df.dropna(inplace=True)
print(X)
print(X_lately)
y = np.array(df['label'])
#print(y)
print(X.shape)
print(y.shape)

X_train, X_test, y_train ,y_test = cross_validation.train_test_split(X,y,test_size=0.2)

clf = LinearRegression()
clf.fit(X_train,y_train)
accuracy = clf.score(X_test,y_test)

print(accuracy)

forecast_set = clf.predict(X_lately)

print(forecast_set,accuracy,forecast_out)

style.use('ggplot')

df['Forecast']=np.nan

# last_date = df.iloc[-1]
# # print('-------',last_date)

# last_unix = last_date.date
# print(last_date,last_unix)
# one_day = 86400
# next_unix = last_unix + one_day
# print("---------",next_unix)
index=-1
for i in forecast_set :
    print(df.iloc[index].date)
    next_date = datetime.datetime.fromtimestamp(df.iloc[index].date)
    index=index-1
    # next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]


print(df.tail())

df['Close'].plot()
df['Forecast'].plot()
plt.show()

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


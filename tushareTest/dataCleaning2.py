import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY, date2num





def pandas_candlestick_ohlc(stock_data, otherseries=None):
    # 设置绘图参数，主要是坐标轴
    mondays = WeekdayLocator(MONDAY)
    alldays = DayLocator()
    dayFormatter = DateFormatter('%d')

    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    if stock_data.index[-1] - stock_data.index[0] < pd.Timedelta('730 days'):
        weekFormatter = DateFormatter('%b %d')
        ax.xaxis.set_major_locator(mondays)
        ax.xaxis.set_minor_locator(alldays)
    else:
        weekFormatter = DateFormatter('%b %d, %Y')
    ax.xaxis.set_major_formatter(weekFormatter)
    ax.grid(True)

    # 创建K线图
    stock_array = np.array(stock_data.reset_index()[['date', 'open', 'high', 'low', 'close']])
    stock_array[:, 0] = date2num(stock_array[:, 0])
    candlestick_ohlc(ax, stock_array, colorup="red", colordown="green", width=0.4)

    # 可同时绘制其他折线图
    if otherseries is not None:
        for each in otherseries:
            plt.plot(stock_data[each], label=each)
        plt.legend()

    ax.xaxis_date()
    ax.autoscale_view()
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

    plt.show()

# plt.rcParams['figure.figsize'] = (10, 6)  # 设置绘图尺寸
#
# # 读取数据
stock = pd.read_csv(r'D:\PycharmProjects\data\simple\000001-20180205.csv',usecols=range(15), parse_dates=[0], index_col=0)
stock = stock[::-1]  # 逆序排列
# pandas_candlestick_ohlc(stock)
# # print(stock.head())
#
# # print(stock.info())
# print(stock.columns)
# stock["close"].plot(grid=True)

# stock['return'] = stock['close'] / stock.close.iloc[0]
# stock['return'].plot(grid=True)

# stock['p_change'].plot(grid=True).axhline(y=0, color='black', lw=2)

# close_price = stock['close']
# log_change = np.log(close_price) - np.log(close_price.shift(1))
# log_change.plot(grid=True).axhline(y=0, color='black', lw=2)

# small = stock[['close', 'price_change', 'ma20','volume', 'v_ma20', 'turnover']]
# _ = pd.scatter_matrix(small)
# small = stock[['close', 'price_change', 'ma20','volume', 'v_ma20']]
# cov = np.corrcoef(small.T)

# img = plt.matshow(cov,cmap=plt.cm.winter)
# plt.colorbar(img, ticks=[-1,0,1])

# stock[['close','volume']].plot(secondary_y='volume', grid=True)
# ################雅虎数据########################
import datetime
import pandas_datareader.data as web

# 设置股票数据的时间跨度
start = datetime.datetime(2016, 10, 1)
end = datetime.date.today()

# 从yahoo中获取google的股价数据。
# goog = web.DataReader("GOOG", "yahoo", start, end)
goog = pd.read_csv(r'D:\PycharmProjects\data\simple\601398-20180205.csv',usecols=range(15), parse_dates=[0], index_col=0)

goog["ma5"] = np.round(goog["close"].rolling(window=5, center=False).mean(), 2)
goog["ma20"] = np.round(goog["close"].rolling(window=20, center=False).mean(), 2)
# goog = goog['2017-01-01':]

# pandas_candlestick_ohlc(goog, ['ma5', 'ma20'])


goog['ma5-20'] = goog['ma5'] - goog['ma20']
goog['diff'] = np.sign(goog['ma5-20'])
goog['diff'].plot(ylim=(-2,2)).axhline(y=0, color='black', lw=2)
goog['signal'] = np.sign(goog['diff'] - goog['diff'].shift(1))
goog['signal'].plot(ylim=(-2,2))
# ################雅虎数据########################


trade = pd.concat([
    pd.DataFrame({"price": goog.loc[goog["signal"] == -1, "close"],
                  "operation": "Buy"}),
    pd.DataFrame({"price": goog.loc[goog["signal"] == 1, "close"],
                  "operation": "Sell"})
])
trade1=pd.DataFrame({"price": goog.loc[goog["signal"] == -1, "close"],
                  "operation": "Buy"})
trade2=pd.DataFrame({"price": goog.loc[goog["signal"] == 1, "close"],
                  "operation": "Sell"})
# trade3=df = pd.merge(trade1, trade2, how='left', on='user_id')
trade3 = pd.concat([trade1,trade2] , axis=1 )
trade3=trade3.fillna(0)
trade.sort_index(inplace=True)
print(trade3)
trade3.to_excel("test.xls")
# plt.show()

# goog['20d-50d'] =goog['20d'] -apple['50d']
# apple.tail()




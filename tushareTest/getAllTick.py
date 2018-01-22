from pandas import DataFrame, Series
import pandas as pd;
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates as mdates
from matplotlib import ticker as mticker
from matplotlib.finance import candlestick_ohlc
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY, YEARLY
from matplotlib.dates import MonthLocator, MONTHLY
import datetime as dt
import pylab
import talib

daylinefilespath = 'G:\\dayline\\'
stock_b_code = '000001'  # 平安银行
MA1 = 10
MA2 = 50
startdate = dt.date(2016, 6, 29)
enddate = dt.date(2018, 1, 22)

def readstkData(rootpath, stockcode, sday, eday):
    returndata = pd.DataFrame()
    for yearnum in range(0, int((eday - sday).days / 365.25) + 1):
        theyear = sday + dt.timedelta(days=yearnum * 365)
        # build file name
        filename = rootpath + theyear.strftime('%Y') + '\\' + str(stockcode).zfill(6) + '.csv'
        try:
            rawdata = pd.read_csv(filename, parse_dates=True, index_col=0, encoding='gbk')
        except IOError:
            raise Exception('IoError when reading dayline data file: ' + filename)
        returndata = pd.concat([rawdata, returndata])
    # Wash data
    returndata = returndata.sort_index()
    returndata.index.name = 'DateTime'
    returndata.drop('amount', axis=1, inplace=True)
    returndata.columns = ['Open', 'High', 'Close', 'Low', 'Volume']
    returndata = returndata[returndata.index < eday.strftime('%Y-%m-%d')]
    return returndata


def moving_average(l, N):
    sum = 0
    result = list(0 for x in l)

    for i in range(0, N):
        sum = sum + l[i]
        result[i] = sum / (i + 1)

    for i in range(N, len(l)):
        sum = sum - l[i - N] + l[i]
        result[i] = sum / N

    return result

def main():
    # days = readstkData(daylinefilespath, stock_b_code, startdate, enddate)
    days = pd.read_csv(r"D:\PycharmProjects\tusharetest\tushareTest\data\simple\000001-20180122.csv")
    # drop the date index from the dateframe & make a copy
    daysreshape = days.reset_index()
    # convert the datetime64 column in the dataframe to 'float days'
    daysreshape['date'] = pd.to_datetime(daysreshape['date'], format='%Y-%m-%d')
    daysreshape['date'] = mdates.date2num(daysreshape['date'].astype(dt.date))
    # daysreshape['date'] = pd.to_numeric(daysreshape['date'])
    # clean day data for candle view
    daysreshape.drop('volume', axis=1, inplace=True)
    # date,open,high,close,low,volume,price_change,p_change,ma5,ma10,ma20,v_ma5,v_ma10,v_ma20,turnover
    daysreshape = daysreshape.reindex(columns=['date', 'open', 'high', 'low', 'close'])

    Av1 = moving_average(daysreshape.close.values, MA1)
    Av2 = moving_average(daysreshape.close.values, MA2)
    SP = len(daysreshape.date.values[MA2 - 1:])
    fig = plt.figure(facecolor='#07000d', figsize=(15, 10))

    ax1 = plt.subplot2grid((6, 4), (1, 0), rowspan=4, colspan=4, axisbg='#07000d')
    candlestick_ohlc(ax1, daysreshape.values[-SP:], width=.6, colorup='#ff1717', colordown='#53c156')
    Label1 = str(MA1) + ' SMA'
    Label2 = str(MA2) + ' SMA'

    ax1.plot(daysreshape.date.values[-SP:], Av1[-SP:], '#e1edf9', label=Label1, linewidth=1.5)
    ax1.plot(daysreshape.date.values[-SP:], Av2[-SP:], '#4ee6fd', label=Label2, linewidth=1.5)
    ax1.grid(True, color='w')
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.yaxis.label.set_color("w")
    ax1.spines['bottom'].set_color("#5998ff")
    ax1.spines['top'].set_color("#5998ff")
    ax1.spines['left'].set_color("#5998ff")
    ax1.spines['right'].set_color("#5998ff")
    ax1.tick_params(axis='y', colors='w')
    plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='upper'))
    ax1.tick_params(axis='x', colors='w')
    plt.ylabel('Stock price and Volume')




    # plot an RSI indicator on top
    maLeg = plt.legend(loc=9, ncol=2, prop={'size': 7},
                       fancybox=True, borderaxespad=0.)
    maLeg.get_frame().set_alpha(0.4)
    textEd = pylab.gca().get_legend().get_texts()
    pylab.setp(textEd[0:5], color='w')

    ax0 = plt.subplot2grid((6, 4), (0, 0), sharex=ax1, rowspan=1, colspan=4, axisbg='#07000d')
    rsi = talib.RSI(daysreshape.close.values)
    # print(rsi,"rsi")
    rsiCol = '#c1f9f7'
    posCol = '#386d13'
    negCol = '#8f2020'

    ax0.plot(daysreshape.date.values[-SP:], rsi[-SP:], rsiCol, linewidth=1.5)
    ax0.axhline(70, color=negCol)
    ax0.axhline(30, color=posCol)
    ax0.fill_between(daysreshape.date.values[-SP:], rsi[-SP:], 70, where=(rsi[-SP:] >= 70), facecolor=negCol,
                     edgecolor=negCol, alpha=0.5)
    ax0.fill_between(daysreshape.date.values[-SP:], rsi[-SP:], 30, where=(rsi[-SP:] <= 30), facecolor=posCol,
                     edgecolor=posCol, alpha=0.5)
    ax0.set_yticks([30, 70])
    ax0.yaxis.label.set_color("w")
    ax0.spines['bottom'].set_color("#5998ff")
    ax0.spines['top'].set_color("#5998ff")
    ax0.spines['left'].set_color("#5998ff")
    ax0.spines['right'].set_color("#5998ff")
    ax0.tick_params(axis='y', colors='w')
    ax0.tick_params(axis='x', colors='w')
    plt.ylabel('RSI')

    volumeMin = 0
    ax1v = ax1.twinx()
    ax1v.fill_between(daysreshape.date.values[-SP:], volumeMin, days.volume.values[-SP:], facecolor='#00ffe8',
                      alpha=.4)
    ax1v.axes.yaxis.set_ticklabels([])
    ax1v.grid(False)
    ###Edit this to 3, so it's a bit larger
    ax1v.set_ylim(0, 3 * days.volume.values.max())
    ax1v.spines['bottom'].set_color("#5998ff")
    ax1v.spines['top'].set_color("#5998ff")
    ax1v.spines['left'].set_color("#5998ff")
    ax1v.spines['right'].set_color("#5998ff")
    ax1v.tick_params(axis='x', colors='w')
    ax1v.tick_params(axis='y', colors='w')

    # MACD

    # plot an MACD indicator on bottom
    ax2 = plt.subplot2grid((6, 4), (5, 0), sharex=ax1, rowspan=1, colspan=4, axisbg='#07000d')
    fillcolor = '#00ffe8'
    nslow = 26
    nfast = 12
    nema = 9
    emaslow, emafast, macd = talib.MACD(daysreshape.close.values)
    ema9 = talib.EMA(macd)
    ax2.plot(daysreshape.date.values[-SP:], macd[-SP:], color='#4ee6fd', lw=2)
    ax2.plot(daysreshape.date.values[-SP:], ema9[-SP:], color='#e1edf9', lw=1)
    ax2.fill_between(daysreshape.date.values[-SP:], macd[-SP:] - ema9[-SP:], 0, alpha=0.5, facecolor=fillcolor,
                     edgecolor=fillcolor)
    plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='upper'))


    ax2.spines['bottom'].set_color("#5998ff")
    ax2.spines['top'].set_color("#5998ff")
    ax2.spines['left'].set_color("#5998ff")
    ax2.spines['right'].set_color("#5998ff")
    ax2.tick_params(axis='x', colors='w')
    ax2.tick_params(axis='y', colors='w')
    plt.ylabel('MACD', color='w')
    ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins=5, prune='upper'))
    for label in ax2.xaxis.get_ticklabels():
        label.set_rotation(45)


    # ----------

    plt.suptitle(stock_b_code, color='w')
    plt.setp(ax0.get_xticklabels(), visible=False)
    plt.setp(ax1.get_xticklabels(), visible=False)
    # Mark big event
    # TODO: Make a real case here
    ax1.annotate('BreakNews!', (daysreshape.date.values[155], Av1[155]),
                 xytext=(0.8, 0.9), textcoords='axes fraction',
                 arrowprops=dict(facecolor='white', shrink=0.05),
                 fontsize=10, color='w',
                 horizontalalignment='right', verticalalignment='bottom')

    plt.subplots_adjust(left=.09, bottom=.14, right=.94, top=.95, wspace=.20, hspace=0)
    plt.show()

if __name__ == "__main__":
    main()
#coding=utf-8
from scipy.stats import rankdata
import scipy as sp
import numpy as np
import pandas as pd
import tushare as ts


class testAlpha:
    def __init__(self):
        pp = ts.get_today_all()
        ppd = pp[['open',  'high',  'low',  'close', 'volume','price_change','turnover']]
        #初始化 开盘价 最高价 最低价 收盘价 总交易量 价格变动 换手率#
        self.open_price = ppd.loc['open', :, :].dropna(axis=1, how='any')
        self.close = ppd.loc['close', :, :].dropna(axis=1, how='any')
        self.low = ppd.loc['low', :, :].dropna(axis=1, how='any')
        self.high = ppd.loc['high', :, :].dropna(axis=1, how='any')
        self.price_change = ppd.loc['price_change', :, :].dropna(axis=1, how='any')
        self.volume = ppd.loc['volume', :, :].dropna(axis=1, how='any')
        self.turnover = ppd.loc['turnover', :, :].dropna(axis=1, how='any')




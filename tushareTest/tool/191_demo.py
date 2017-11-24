# from gtja191 import *
import gtja191
import datetime
import importlib

importlib.reload(gtja191)


# 最多持仓10只股票
# 初始资金100w
# 每周一调仓

def initialize(account):
    account.security = get_index_stocks('000300.SH')
    run_weekly(trade, date_rule=1, reference_security='000001.SZ')


def trade(account, data):
    date = get_last_datetime().strftime("%Y%m%d")

    # 调用国泰君安191因子库
    gtja = gtja191.gtja_191(date, '000300.SH')
    # 选用第191号因子
    alpha = gtja.alpha_191()

    # 按照因子值排序
    sorted_alpha = alpha.sort_values(ascending=True, na_position='last')

    # 进行买卖
    position_stocks = list(account.positions.keys())  # 获取仓前持仓
    for s in position_stocks:  # 卖出上一周持仓
        order_target_percent(s, 0)
    for s in sorted_alpha.iloc[:10].index:  # 取因子值前10调仓买入
        order_target_percent(s, 0.1)

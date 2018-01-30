import tushare as ts
import numpy as np
import matplotlib.pyplot as plt

e = ts.get_today_all()
size = 20  # 把区间分成20份
array = []

ll = e[u'high']  # 最高价
hh = e[u'low']  # 最低价
cc = e[u'changepercent']  # 涨跌幅
for i in range(0, len(e)):
    if ll[i] != hh[i]:  # 最高价与最低价相同说明停牌
        if cc[i] > 10:  # 涨幅大于10%的股票归为10%
            array.append(10)
        elif cc[i] < -10:  # 跌幅大于-10%的股票归为-10%
            array.append(-10)
        else:
            array.append(cc[i])

print
"Total:", len(array)
array = np.sort(array)  # 排序

bin_arr = []
bin_arr.append(-10)  # 加入区间的左侧值
count = 0  # 区域计数
for i in range(0, len(array)):
    count += 1
    if count > len(array) / size:
        print
        array[i]
        count = 0
        bin_arr.append(array[i])
bin_arr.append(10)  # 加入区间右侧值

hist, bins = np.histogram(array, bins=bin_arr)  # 按bin_arr给定的区域计算直方图
width = np.diff(bins)
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.show()
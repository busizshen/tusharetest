# -*- coding:utf-8 -*-
import numpy as np
import sys, codecs

i = 0
m = 25
m1 = 25
dd = -1
rate = 0.15
rate1 = 0.1
# import sys,codecs
fileName="s1.txt"
fileObj = codecs.open(fileName, 'w', "utf-8")
fileObj.write("test\n")

fileObj = codecs.open(fileName, 'a', "utf-8")
for i in range(1, 48):
    day = (m * rate / 22) * 10000
    day1 = (m1 * rate1 / 22) * 10000
    week = (m * rate / 4) * 10000
    week1 = (m1 * rate1 / 4) * 10000
    month = m * rate
    month1 = m1 * rate
    ddd = (dd * (i / 12 + 1))
    m = m * rate + m + ddd
    m1 = m1 * rate1 + m1 + ddd

    m = float('%.2f' % m)
    day = float('%.2f' % day)

    m1 = float('%.2f' % m1)
    day1 = float('%.2f' % day1)
    ff = np.fv(rate, i, dd, dd)
    # print(str(m)+"   "+str(i)+"  "+str(ff)+"  "+str(dd))
    line = ' %s目标 \t\t金额%s ~ %s\t\t递增%s\t\t约%s ~ %s \n' % (
    str(i), str(m), str(m1), str(round(ddd, 2)), str(day), str(day1))
    print(line)

    fileObj.write(line)
    line = ' %s目标 \t\t金额%s ~ %s\t\t递增%s\t\t约%s ~ %s \n' % (
    str(i), str(m), str(m1), str(round(ddd, 2)), str(week), str(week1))
    print(line)

    fileObj.write(line)
    line = ' %s目标 \t\t金额%s ~ %s\t\t递增%s\t\t约%s ~ %s \n\n\n' % (
    str(i), str(m), str(m1), str(round(ddd, 2)), str(month), str(month1))
    print(line)

    fileObj.write(line)

    # fileObj = open("1.xml",'a',"utf-8")
    # print(line)
    # fileObj.write(line)
# fileObj.close
# year =sys.argv[0]
# print(year)


print(ff)
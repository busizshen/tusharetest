# -*- coding:utf-8 -*-
import numpy as np
import sys, codecs

i = 0
m = 20
m1 = 20
dd = -0.05
rate = 0.0075
rate1 = 0.005
# import sys,codecs
fileName="s1.txt"
fileObj = codecs.open(fileName, 'w', "utf-8")
fileObj.write("test\n")

fileObj = codecs.open(fileName, 'a', "utf-8")
for i in range(1, 1600):

    month = m * rate
    month1 = m1 * rate
    ddd = dd
    m = m * rate + m + ddd
    m1 = m1 * rate1 + m1 + ddd

    m = float('%.2f' % m)

    m1 = float('%.2f' % m1)
    ff = np.fv(rate, i, dd, dd)
    # print(str(m)+"   "+str(i)+"  "+str(ff)+"  "+str(dd))
    line = '<tr><td> <div id="div%s"></div> <input type="radio" id="one%s" value="%s" v-model="picked"></td>  <td>LV%s</td> <td>%s ~ %s</td><td>增加%s</td><td>约%s ~ %s</td></tr>  \n' % (
        str(i), str(i),str(i),str(i), str(m), str(m1), str(round(ddd, 2)), str(round(month, 2)), str(round(month1, 2)))
    # line = """
    # <input type="radio" id="one" value="%s" v-model="picked">
    # <label for="one%s">%s</label>
    # <br>
    # """%(str(i),str(i),str(line1))
    print(line)
    fileObj.write(line)

    # fileObj = open("1.xml",'a',"utf-8")
    # print(line)
    # fileObj.write(line)
# fileObj.close
# year =sys.argv[0]
# print(year)


print(ff)
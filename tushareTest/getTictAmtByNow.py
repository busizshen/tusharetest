# coding=utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time
import os
import smtplib
import email.mime.multipart
import email.mime.text
import tushare as ts
import csv, codecs

ss = ['002049', '002302','603260','000425','002230','002721']
dd = ['0', '19.5', '4.12']
sm = ['0', '1900', '10000']


def getAmt():
    df = ts.get_realtime_quotes(ss)
    print(df[['name','price']] )
    # csvfile = 'csvtest.csv'
    # msg = ''
    # df.to_csv(csvfile, encoding='utf-8')
    # with open(csvfile, "r", encoding='utf-8') as csvfile:
    #     # 读取csv文件，返回的是迭代类型
    #     read = csv.reader(csvfile)
    #     index = 0
    #     for i in read:
    #         tt = ''
    #         try:
    #             # print(i)
    #             print(str((float(dd[index]) * float(sm[index]) - float(i[4]) * float(sm[index]))))
    #             smsg = '%s从%s~%s 持有%s 盈亏%s  %s' % (i[1], dd[index], i[4], str(float(i[4]) * float(sm[index])), str(
    #                 float(i[4]) * float(sm[index]) - float(dd[index]) * float(sm[index])), datetime.now())
    #             print(smsg)
    #             msg = msg + '\n' + smsg
    #             # msg=msg+'\n'+  i
    #             index = index + 1
    #
    #             # tt=tt+smsg
    #             # fileObj = codecs.open("1.xml",'a',"utf-8")
    #             # fileObj = codecs.open("1.xml",'w',"utf-8")
    #             # print(line)
    #             # fileObj.write(smsg+'\r\n\r\n')
    #         except:
    #             print(11)
    #             index = index + 1
    #
    #             # print(msg)
    #             # setMail(msg)


def setMail(ss):
    msg = email.mime.multipart.MIMEMultipart()
    fromE = 'xxxxx@xxx.com'
    toE = 'xxxxx@xxx.com'
    msg['from'] = fromE
    msg['to'] = toE
    msg['subject'] = 'test'
    content = ss
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    smtp = smtplib
    smtp = smtplib.SMTP()
    smtp.connect('smtp.exmail.qq.com', '25')
    smtp.login(fromE, 'xxxxx')
    smtp.sendmail(fromE, toE, str(msg))
    smtp.quit()


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    getAmt()
    # sched = BlockingScheduler()
    # sched.add_job(getAmt, 'interval', seconds=5)
    # sched.start()

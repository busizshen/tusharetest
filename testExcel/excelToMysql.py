# -*- coding:utf-8 -*-
import xlrd
import pymysql

# Open the workbook and define the worksheet
book = xlrd.open_workbook(r"D:\文档\金禄贷\城市公司账户信息表.xlsx")
# sheet = book.sheet_by_name("Sheet1")
sheet = book.sheet_by_index(0)
# 建立一个MySQL连接+
# database = pymysql.connect(host="192..79", user="admin", passwd="+", db="banklake")

# 获得游标对象, 用于逐行遍历数据库数据
# cursor = database.cursor()

# # 创建插入SQL语句
# query = """INSERT INTO temp_open_bank_card (ru_id, re_id, user_id, re_amt, re_use_start_dts, re_use_end_dts, credit_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
query = r"""INSERT INTO temp_open_bank_card VALUES ('%s','%s', '%s', '%s', '%s'); """
# # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题
for r in range(1, sheet.nrows):

    temp0 = sheet.cell(r, 0).value
    temp1 = sheet.cell(r, 1).value
    temp2 = sheet.cell(r, 2).value
    temp3 = sheet.cell(r, 3).value
    temp4 = sheet.cell(r, 4).value

    values = (temp0,temp1,temp2,temp3,temp4)
    # print(values)
    print(query%values)
    with  open("test.txt",'a',encoding="utf-8") as fileObj:
        fileObj.write(query%values+'\r')
#       # 执行sql语句
#     cursor.execute(query, values)

# # 关闭游标
# cursor.close()

# # 提交
# database.commit()

# # 关闭数据库连接
# database.close()

# 打印结果
# print ""
# print "Done! "
# print ""
columns = str(sheet.ncols)
rows = str(sheet.nrows)



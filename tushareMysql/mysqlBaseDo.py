import pymysql
import time

#获取参数
class datainfo:
    host=""
    username = ""
    password = ""
    db = ""
    print()

    #测试数据库连接
    def testconnect(self):

        #打开数据库链接

        db = pymysql.connect(self.host,self.username,self.password,self.database)

        #使用cursor() 方法创建一个游标对象 cursor

        cursor = db.cursor()

        #使用execute()方法执行SQL查询

        cursor.execute("select version()")

        #使用fetchone ()获取单条数据

        data = cursor.fetchone()

        print(data)

        db.close()
    def dosth(self):
        with pymysql.connect(self.host,self.username,self.password,self.database) as db:
            self.testconnect(self)
            # b = getattr(a, servicename)()  #执行对象的某个方法
            
    #插入数据库
    def InsertDate(self):
        #打开数据库链接

        db = pymysql.connect(self.host,self.username,self.password,self.database,charset='utf8')

        #使用cursor() 方法创建一个游标对象 cursor

        cursor = db.cursor()

        create_time = time.strftime('%Y-%m-%d %H:%M:%S')
        update_time = time.strftime('%Y-%m-%d %H:%M:%S')
        start_time = time.strftime('%Y-%m-%d %H:%M:%S')
        end_time = time.strftime('%Y-%m-%d %H:%M:%S')
        remark = "测试插入信息"
        print("开始")
        #Sql 插入语句
        sql = "insert into demo(start_time,end_time,creat_time,update_time,remark) " \
              "VALUES ('%s','%s','%s','%s','%s')"\
              %(start_time,end_time,create_time,update_time,remark)
        try:
            #执行sql
            print("执行插入")
            tt = cursor.execute(sql)
            print(tt)
            db.commit()
        except UnicodeEncodeError as e :
            #发生错误时回滚
            print(e)
            db.rollback()
        db.close()


    #查询操作
    def selectData(self,db):

        cursor = db.cursor()

        sql = "select * from demo where id >='%d'" %(1)
        try:
            #执行sql
            print("执行查询")
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                id = row[0]
                start_time = row[1]
                end_time = row[2]
                create_time = row[3]
                update_time = row[4]
                remark = row[5]
                #打印结果
                print("id = %d,start_time=%s,end_time=%s,create_time=%s,update_time=%s,remark=%s" %(id,start_time,end_time,create_time,update_time,remark))

            db.commit()
        except UnicodeEncodeError as e :
            #发生错误时回滚
            print(e)


    #更新操作
    def update_data(self,db):
        cursor = db.cursor()
        update_time = time.strftime('%Y-%m-%d %H:%M:%S')
        sql = "update demo set update_time ='%s' where id >='%d' " %(update_time,1)
        try:
            #执行sql
            print("执行更新")
            cursor.execute(sql)

            db.commit()
        except UnicodeEncodeError as e :
            #发生错误时回滚
            print(e)
            db.rollback()

    #删除操作
    def delete_Date(self,db):

        # 使用cursor() 方法创建一个游标对象 cursor

        cursor = db.cursor()

        sql = "delete from demo where id <'%d' " %(1)
        try:
            #执行sql
            print("执行删除")
            cursor.execute(sql)

            db.commit()
        except UnicodeEncodeError as e :
            #发生错误时回滚
            print(e)
            db.rollback()



if __name__ == '__main__':
    testconnect()
    InsertDate()
    selectData()
    update_data()
    delete_Date()
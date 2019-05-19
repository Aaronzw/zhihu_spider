#-*- coding: utf-8 -*-
import pymysql
import time
import random
class Connetction:
    # db = pymysql.connect("139.199.205.104", "user", "pass", "wenda")
    db = pymysql.connect("127.0.0.1", "root", "root", "wenda")
    # def insertQuestion(self,question_title,question_content="",userId="1"):
    #     cursor = self.db.cursor()
    #     insert_sql = "insert into question(title, content,user_id, created_date, comment_count, status) values(%s, %s, %s, %s, %s, %s)"
    #     # 参数列表
    #     title=question_title
    #     content=question_content
    #     use_id=userId
    #     created_date= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #     comment_count='0'
    #     status='0'
    #     values = (title, content, use_id,created_date, comment_count, status)
    #     try:
    #     # 执行SQL语句
    #         cursor.execute(insert_sql,values)
    #         # 获取所有记录列表
    #         self.db.commit()
    #     except:
    #         print("Error: unable to fetch data")
    #         # 关闭数据库连接
    #         self.db.close()

    #插入数据返回id
    def insertQuestion(self,question_title,question_content="",user_id=1):
        cursor = self.db.cursor()
        insert_sql = "insert into question(title, content,user_id, created_date, comment_count, status) values(%s, %s, %s, %s, %s, %s)"
        # 参数列表
        title=question_title
        content=question_content
        # user_id=user_id
        created_date= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        comment_count='0'
        status='0'
        values = (title, content, user_id,created_date, comment_count, status)
        try:
        # 执行SQL语句
            self.db.ping(reconnect=True)
            cursor.execute(insert_sql,values)
            # 获取所有记录列表
            self.db.commit()
            row_id=cursor.lastrowid
            return row_id
        except:
            print(insert_sql)
            print(values)
            print("Error: unable to fetch data question")
            # 关闭数据库连接
            self.db.close()

    def insertComment(self,comment,userId,entityId,entityType=1,status=0):
        cursor = self.db.cursor()
        insert_sql = "insert into comment(user_id,content,created_date,entity_id,entity_type,status) values(%s, %s, %s, %s, %s, %s)"
        # 参数列表
        content = comment
        user_id = userId
        created_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        entityId = entityId
        entityType= entityType
        status = '0'
        values = (user_id, content, created_date, entityId,entityType, status)
        try:
            # 执行SQL语句
            self.db.ping(reconnect=True)
            cursor.execute(insert_sql, values)
            # 获取所有记录列表
            self.db.commit()
            row_id = cursor.lastrowid
            return row_id
        except:
            print(insert_sql)
            print(values)
            print("Error: unable to fetch data")
            # 关闭数据库连接
            self.db.close()

# C=Connetction()
# C.insertComment("HAHHA","1","1")

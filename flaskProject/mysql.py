# """ 配置数据库 """
# HOST='127.0.0.1'
# PORT='3306'
# USERNAME='root'
# PASSWORD='root'
# DATABASE='data'
import os
import time

# select * from character

import pandas as pd
import pymysql
import datetime


# 用面向对象的方式编写，更加熟悉面向对象代码风格
class Mysql_csv(object):
    # 定义一个init方法，用于读取数据库
    def __init__(self):
        # 读取数据库和建立游标对象
        self.connect = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root", database="data",
                                       charset="utf8")
        self.cursor = self.connect.cursor()

    # 定义一个del类，用于运行完所有程序的时候关闭数据库和游标对象
    def __del__(self):
        self.connect.close()
        self.cursor.close()

    def write_mysql(self):
        # 在数据表中写入数据
        t = time.localtime()

        # zhihu_csv_name = 'C:/Users/徐越/Downloads/flaskProject-master/Zhihu(2022,10,15).csv'
        # weibo_csv_name = 'C:/Users/徐越/Downloads/flaskProject-master/Weibo(2022,10,15).csv'
        # tieba_csv_name = 'C:/Users/徐越/Downloads/flaskProject-master/Tieba(2022,10,15).csv'
        # bilibili_csv_name = 'C:/Users/徐越/Downloads/flaskProject-master/Bilibili(2022,10,15).csv'
        path = os.getcwd()
        path = path.replace("\\", "/")
        zhihu_csv_name = path + "/data/Zhihu" + "({},{},{})".format(t.tm_year, t.tm_mon, t.tm_mday) + ".csv"
        weibo_csv_name = path + "/data/Weibo" + "({},{},{})".format(t.tm_year, t.tm_mon, t.tm_mday) + ".csv"
        tieba_csv_name = path + "/data/Tieba" + "({},{},{})".format(t.tm_year, t.tm_mon, t.tm_mday) + ".csv"
        bilibili_csv_name = path + "/data/Bilibili" + "({},{},{})".format(t.tm_year, t.tm_mon, t.tm_mday) + ".csv"
        print(zhihu_csv_name)
        data1 = pd.read_csv(zhihu_csv_name, encoding="utf-8")
        data_1 = list(data1.values)
        data2 = pd.read_csv(weibo_csv_name, encoding="utf-8")
        data_2 = list(data2.values)
        data3 = pd.read_csv(tieba_csv_name, encoding="utf-8")
        data_3 = list(data3.values)
        data4 = pd.read_csv(bilibili_csv_name, encoding="utf-8")
        data_4 = list(data4.values)
        for i in data_1:  # 提取数据到元组
            data = tuple(i)
            today = datetime.date.today()
            formatted_today = today.strftime('%y%m%d')  # 添加当前时间
            # print(formatted_today)
            time_tuple = (formatted_today,)
            data_ = data + time_tuple
            # print(data_)
            sql = """insert into zhihu values{}""".format(data_)
            self.cursor.execute(sql)
            self.commit()
        print("\n知乎数据植入完成")
        for i in data_2:  # 提取数据到元组
            data = tuple(i)
            today = datetime.date.today()
            formatted_today = today.strftime('%y%m%d')  # 添加当前时间
            # print(formatted_today)
            time_tuple = (formatted_today,)
            data_ = data + time_tuple
            # print(data_)
            sql = """insert into weibo values{}""".format(data_)
            self.cursor.execute(sql)
            self.commit()
        print("\n微博数据植入完成")
        for i in data_3:  # 提取数据到元组
            data = tuple(i)
            today = datetime.date.today()
            formatted_today = today.strftime('%y%m%d')  # 添加当前时间
            # print(formatted_today)
            time_tuple = (formatted_today,)
            data_ = data + time_tuple
            # print(data_)
            sql = """insert into tieba values{}""".format(data_)
            self.cursor.execute(sql)
            self.commit()
        print("\n贴吧数据植入完成")
        for i in data_4:  # 提取数据到元组
            data = tuple(i)
            today = datetime.date.today()
            formatted_today = today.strftime('%y%m%d')  # 添加当前时间
            # print(formatted_today)
            time_tuple = (formatted_today,)
            data_ = data + time_tuple
            # print(data_)
            sql = """insert into bilibili values{}""".format(data_)
            self.cursor.execute(sql)
            self.commit()
        print("\nB站数据植入完成")

    def commit(self):
        # 定义一个确认事务运行
        self.connect.commit()

    def create(self):
        # 若已有数据表，则删除
        # query = "drop table if exists zhihu;"
        # self.cursor.execute(query)
        # 创建数据表，用刚才提取的列索引作为字段
        # ！！！sql4注释掉的内容为添加like字段之前的sql语句
        sql1 = "create table if not exists tieba(id INT not null,`rank` INT not null,title varchar(255) not null,link varchar(255) not null,image_url varchar(255) not null,`describe` varchar(255) not null,heat varchar(50) not null,`date` varchar(50) not null,primary key(`rank`,`date`))default charset=utf8;"
        sql2 = "create table if not exists zhihu(id INT not null,`rank` INT not null,title varchar(255) not null,link varchar(255) not null,image_url varchar(255) not null,`describe` varchar(255) not null,heat varchar(50) not null,`date` varchar(50) not null,primary key(`rank`,`date`))default charset=utf8;"
        sql3 = "create table if not exists weibo(id INT not null,`rank` INT not null,title varchar(255) not null,link varchar(255) not null,`date` varchar(50) not null,primary key(id,`date`))default charset=utf8;"
        # sql4 = "create table if not exists bilibili(id INT not null,`rank` INT not null,title varchar(255) not null,link varchar(255) not null,image_url varchar(255) not null,`describe` varchar(255) not null,author varchar(255) not null,view varchar(10) not null,reply varchar(10) not null,favorite varchar(10) not null,coin varchar(10) not null,share varchar(10) not null,`date` varchar(50) not null,primary key(`rank`,`date`))default charset=utf8;"
        sql4 = "create table if not exists bilibili(id INT not null,`rank` INT not null,title varchar(255) not null,link varchar(255) not null,image_url varchar(255) not null,`describe` varchar(255) not null,author varchar(255) not null,view varchar(10) not null,like varchar(10) not null,reply varchar(10) not null,favorite varchar(10) not null,coin varchar(10) not null,share varchar(10) not null,`date` varchar(50) not null,primary key(`rank`,`date`))default charset=utf8;"
        self.cursor.execute(sql1)
        self.cursor.execute(sql2)
        self.cursor.execute(sql3)
        self.cursor.execute(sql4)
        self.commit()

    # 运行程序
    def run(self):
        self.create()
        self.write_mysql()


def main():
    sql = Mysql_csv()
    sql.run()


if __name__ == '__main__':
    main()

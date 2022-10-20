from flask import Flask  # 需自行下载Flask包，并导入这几个内容
from flask import jsonify
from flask import request
from flask_cors import CORS
from common.mysql_operate import db  # 从common包中导入mysql_operate，使用其db
import datetime
import os

app = Flask(__name__)
# 配置全局跨域
# cors = CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app, supports_credentials=True)
app.config['JSON_AS_ASCII'] = False  # 打印中文


@app.route("/")  # 自定义路径
def index():
    os.system('python mysql.py')
    return '今日数据植入完成!'


@app.route("/tieba")  # 自定义query路径
def get_tieba_users():
    """获取贴吧爬取信息"""
    today = datetime.date.today()
    formatted_today = today.strftime('%y%m%d')
    date = str(request.args.get('date', default=formatted_today))  # url为页面端输入的值
    rank = str(request.args.get('rank', default=-1))  # url为页面端输入的值
    if rank == '-1':
        sql = "SELECT * FROM tieba WHERE `date` =" + date  # sql语句，可自行对应自己数据相应的表进行操作
        data = db.select_db(sql)  # 用mysql_operate文件中的db的select_db方法进行查询
        if data:
            print("获取选定用户信息 == >> {}".format(data))  # 在pycharm下打印信息
            return jsonify(data)  # 在页面输出返回信息的json格式
        else:
            return '不存在当天的热搜'
    else:
        sql = "SELECT * FROM tieba WHERE (`rank`={0} and `date`={1})".format(rank, date)
        data = db.select_db(sql)  # 用mysql_operate文件中的db的select_db方法进行查询
        if data:
            print("获取选定用户信息 == >> {}".format(data))  # 在pycharm下打印信息
            return jsonify(data)  # 在页面输出返回信息的json格式
        else:
            return '不存在此热搜排名'


@app.route("/weibo")  # 自定义query路径
def get_weibo_users():
    """获取微博爬取信息"""
    today = datetime.date.today()
    formatted_today = today.strftime('%y%m%d')
    date = str(request.args.get('date', default=formatted_today))  # url为页面端输入的值
    rank = str(request.args.get('rank', default=-1))  # url为页面端输入的值
    if rank == '-1':
        sql = "SELECT * FROM weibo WHERE `date` =" + date  # sql语句，可自行对应自己数据相应的表进行操作
        data = db.select_db(sql)  # 用mysql_operate文件中的db的select_db方法进行查询
        if data:
            print("获取选定用户信息 == >> {}".format(data))  # 在pycharm下打印信息
            return jsonify(data)  # 在页面输出返回信息的json格式
        else:
            return '不存在当天的热搜'
    else:
        sql = "SELECT * FROM weibo WHERE (`rank`={0} and `date`={1})".format(rank, date)
        data = db.select_db(sql)  # 用mysql_operate文件中的db的select_db方法进行查询
        if data:
            print("获取选定用户信息 == >> {}".format(data))  # 在pycharm下打印信息
            return jsonify(data)  # 在页面输出返回信息的json格式
        else:
            return '不存在此热搜排名'


@app.route("/zhihu")  # 自定义query路径
def get_zhihu_users():
    """获取知乎爬取信息"""
    today = datetime.date.today()
    formatted_today = today.strftime('%y%m%d')
    date = str(request.args.get('date', default=formatted_today))  # url为页面端输入的值
    rank = str(request.args.get('rank', default=-1))  # url为页面端输入的值
    if rank == '-1':
        sql = "SELECT * FROM zhihu WHERE `date` =" + date  # sql语句，可自行对应自己数据相应的表进行操作
        data = db.select_db(sql)  # 用mysql_operate文件中的db的select_db方法进行查询
        if data:
            print("获取选定用户信息 == >> {}".format(data))  # 在pycharm下打印信息
            return jsonify(data)  # 在页面输出返回信息的json格式
        else:
            return '不存在当天的热搜'
    else:
        sql = "SELECT * FROM zhihu WHERE (`rank`={0} and `date`={1})".format(rank, date)
        data = db.select_db(sql)  # 用mysql_operate文件中的db的select_db方法进行查询
        if data:
            print("获取选定用户信息 == >> {}".format(data))  # 在pycharm下打印信息
            return jsonify(data)  # 在页面输出返回信息的json格式
        else:
            return '不存在此热搜排名'


@app.route("/bilibili")  # 自定义query路径
def get_bilibili_users():
    """获取B站爬取信息"""
    today = datetime.date.today()
    formatted_today = today.strftime('%y%m%d')
    date = str(request.args.get('date', default=formatted_today))  # url为页面端输入的值
    rank = str(request.args.get('rank', default=-1))  # url为页面端输入的值
    if rank == '-1':
        sql = "SELECT * FROM bilibili WHERE `date` =" + date  # sql语句，可自行对应自己数据相应的表进行操作
        data = db.select_db(sql)  # 用mysql_operate文件中的db的select_db方法进行查询
        if data:
            print("获取选定用户信息 == >> {}".format(data))  # 在pycharm下打印信息
            return jsonify(data)  # 在页面输出返回信息的json格式
        else:
            return '不存在当天的热搜'
    else:
        sql = "SELECT * FROM bilibili WHERE (`rank`={0} and `date`={1})".format(rank, date)
        data = db.select_db(sql)  # 用mysql_operate文件中的db的select_db方法进行查询
        if data:
            print("获取选定用户信息 == >> {}".format(data))  # 在pycharm下打印信息
            return jsonify(data)  # 在页面输出返回信息的json格式
        else:
            return '不存在此热搜排名'


@app.route("/insert", methods=["GET", "POST"])  # 表示GET和POST方法都可以进行操作
def insert():
    """插入信息"""
    id = str(request.args.get('id'))  # url为页面端输入的值
    title = str(request.args.get('title'))
    sql = "SELECT * FROM tieba WHERE id = '" + id + "'"
    data = db.select_db(sql)
    if data:  # 判断是否有返回数据，如果有则表示已经存在
        return '已收藏'
    else:  # 如果没有，则插入新数据
        sql1 = "insert into tieba(id,title) values('" + id + "','" + title + "');"
        db.execute_db(sql1)
        return '收藏成功'


@app.route("/delete", methods=["GET", "POST"])  #
def delete():
    """删除信息"""
    id = str(request.args.get('id'))
    sql = "SELECT * FROM tieba WHERE id =" + id
    data = db.select_db(sql)
    if data:
        sql1 = "DELETE FROM tieba WHERE id =" + id
        db.execute_db(sql1)
        return '删除成功'
    else:
        return '不存在此id'


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000)  #

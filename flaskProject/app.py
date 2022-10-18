from flask import Flask   # 需自行下载Flask包，并导入这几个内容
from flask import jsonify
from flask import request
from common import mysql_operate  # 从common包中导入mysql_operate，使用其db

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False     # 打印中文

@app.route("/")    # 自定义路径
def index():
    return 'Hello!'

@app.route("/tieba")    # 自定义query路径
def get_tieba_users():
    """获取贴吧爬取信息"""
    sql = "SELECT * FROM tieba"   # sql语句，可自行对应自己数据相应的表进行操作
    data = mysql_operate.db.select_db(sql)   # 用mysql_operate文件中的db的select_db方法进行查询
    print("获取所有用户信息 == >> {}".format(data))  # 在pycharm下打印信息
    return jsonify(data)   # 在页面输出返回信息的json格式

@app.route("/weibo")    # 自定义query路径
def get_weibo_users():
    """获取微博爬取信息"""
    sql = "SELECT * FROM weibo"   # sql语句，可自行对应自己数据相应的表进行操作
    data = mysql_operate.db.select_db(sql)   # 用mysql_operate文件中的db的select_db方法进行查询
    print("获取所有用户信息 == >> {}".format(data))  # 在pycharm下打印信息
    return jsonify(data)   # 在页面输出返回信息的json格式

@app.route("/zhihu")    # 自定义query路径
def get_zhihu_users():
    """获取知乎爬取信息"""
    sql = "SELECT * FROM zhihu"   # sql语句，可自行对应自己数据相应的表进行操作
    data = mysql_operate.db.select_db(sql)   # 用mysql_operate文件中的db的select_db方法进行查询
    print("获取所有用户信息 == >> {}".format(data))  # 在pycharm下打印信息
    return jsonify(data)   # 在页面输出返回信息的json格式

@app.route("/bilibili")    # 自定义query路径
def get_bilibili_users():
    """获取B站爬取信息"""
    sql = "SELECT * FROM bilibili"   # sql语句，可自行对应自己数据相应的表进行操作
    data = mysql_operate.db.select_db(sql)   # 用mysql_operate文件中的db的select_db方法进行查询
    print("获取所有用户信息 == >> {}".format(data))  # 在pycharm下打印信息
    return jsonify(data)   # 在页面输出返回信息的json格式

@app.route("/tieba/select")    # 自定义query路径
def select_tieba_users():
    """获取选定用户信息"""
    id = str(request.args.get('rank'))  # url为页面端输入的值
    sql = "SELECT * FROM tieba WHERE `rank`=" + id   # sql语句，可自行对应自己数据相应的表进行操作
    data = mysql_operate.db.select_db(sql)   # 用mysql_operate文件中的db的select_db方法进行查询
    if data:
        print("获取选定用户信息 == >> {}".format(data))  # 在pycharm下打印信息
        return jsonify(data)  # 在页面输出返回信息的json格式
    else:
        return '不存在此id'

@app.route("/weibo/select")    # 自定义query路径
def select_weibo_users():
    """获取选定用户信息"""
    id = str(request.args.get('rank'))  # url为页面端输入的值
    sql = "SELECT * FROM weibo WHERE `rank`=" + id   # sql语句，可自行对应自己数据相应的表进行操作
    data = mysql_operate.db.select_db(sql)   # 用mysql_operate文件中的db的select_db方法进行查询
    if data:
        print("获取选定用户信息 == >> {}".format(data))  # 在pycharm下打印信息
        return jsonify(data)  # 在页面输出返回信息的json格式
    else:
        return '不存在此id'

@app.route("/zhihu/select")    # 自定义query路径
def select_zhihu_users():
    """获取选定用户信息"""
    id = str(request.args.get('rank'))  # url为页面端输入的值
    sql = "SELECT * FROM zhihu WHERE `rank`=" + id   # sql语句，可自行对应自己数据相应的表进行操作
    data = mysql_operate.db.select_db(sql)   # 用mysql_operate文件中的db的select_db方法进行查询
    if data:
        print("获取选定用户信息 == >> {}".format(data))  # 在pycharm下打印信息
        return jsonify(data)  # 在页面输出返回信息的json格式
    else:
        return '不存在此id'

@app.route("/bilibili/select")    # 自定义query路径
def select_bilibili_users():
    """获取选定用户信息"""
    id = str(request.args.get('rank'))  # url为页面端输入的值
    sql = "SELECT * FROM bilibili WHERE `rank`=" + id   # sql语句，可自行对应自己数据相应的表进行操作
    data = mysql_operate.db.select_db(sql)   # 用mysql_operate文件中的db的select_db方法进行查询
    if data:
        print("获取选定用户信息 == >> {}".format(data))  # 在pycharm下打印信息
        return jsonify(data)  # 在页面输出返回信息的json格式
    else:
        return '不存在此id'

@app.route("/insert", methods=["GET", "POST"])  # 表示GET和POST方法都可以进行操作
def insert():
    """插入信息"""
    id = str(request.args.get('id'))   # url为页面端输入的值
    title = str(request.args.get('title'))
    sql = "SELECT * FROM tieba WHERE id = '" + id + "'"
    data = mysql_operate.db.select_db(sql)
    if data:     # 判断是否有返回数据，如果有则表示已经存在
        return '已收藏'
    else:    # 如果没有，则插入新数据
        sql1 = "insert into tieba(id,title) values('" + id + "','" + title + "');"
        mysql_operate.db.execute_db(sql1)
        return '收藏成功'


@app.route("/delete", methods=["GET", "POST"])   #
def delete():
    """删除信息"""
    id = str(request.args.get('id'))
    sql = "SELECT * FROM tieba WHERE id =" + id
    data = mysql_operate.db.select_db(sql)
    if data:
        sql1 = "DELETE FROM tieba WHERE id =" + id
        mysql_operate.db.execute_db(sql1)
        return '删除成功'
    else:
        return '不存在此id'


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)   #

# host = '127.0.0.1' 表示设置的ip，如果需要连接手机等设备，可以将手机和电脑连接同一个热点，将host设置成对应的ip
# port 为端口号，可自行设置

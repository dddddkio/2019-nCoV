# -×- coding:utf-8 -*-

from flask import Flask
from flask import jsonify
import pymysql


def get_conn():
    # 链接数据库
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='cov',
                           charset='utf8')
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    # 关闭数据库
    if cursor:
        cursor.close()
    if conn:
        conn.close()


app = Flask(__name__)


@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin'] = '*'
    return environ


@app.route("/api/l1")
def get_data_l1():
    date, confirm = [], []

    # 从数据库中读取数据
    conn, cursor = get_conn()
    sql = "SELECT ds,confirm FROM cov.history ORDER BY ds desc;"
    cursor.execute(sql)
    data = cursor.fetchall()
    close_conn(conn, cursor)

    # 解析数据
    for i in data:
        date.append(i[0].strftime("%m-%d"))
        confirm.append(i[1])

    return jsonify({"date": date, "confirm": confirm})


@app.route("/api/c1")
def get_data_c1():
    confirm, suspect, heal, dead = 0, 0, 0, 0

    # 从数据库中读取数据
    sql = "SELECT confirm, suspect, heal, dead FROM cov.history ORDER BY ds desc limit 1;"
    conn, cursor = get_conn()
    cursor.execute(sql)
    data = cursor.fetchall()
    close_conn(conn, cursor)

    # 解析数据
    for i in data:
        confirm = i[0]
        suspect = i[1]
        heal = i[2]
        dead = i[3]
    return jsonify({"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead})


@app.route("/api/l2")
def get_data_l2():
    date, confirm_add = [], []

    # 从数据库中读取数据
    sql = "SELECT ds,confirm_add FROM cov.history ORDER BY ds desc limit 14;"
    conn, cursor = get_conn()
    cursor.execute(sql)
    data = cursor.fetchall()
    close_conn(conn, cursor)

    # 解析数据
    for i in data:
        date.append(i[0].strftime("%m-%d"))
        confirm_add.append(i[1])

    return jsonify({"date": date, "confirm_add":confirm_add})


@app.route("/api/r1")
def get_data_r1():
    heal, confirm, dead = 0,0,0

    # 从数据库中读取数据
    sql = "SELECT confirm,heal,dead FROM cov.history ORDER BY ds desc limit 1;"
    conn, cursor = get_conn()
    cursor.execute(sql)
    data = cursor.fetchall()
    close_conn(conn, cursor)

    # 解析数据
    for i in data:
        confirm = i[0]
        heal = i[1]
        dead = i[2]

    cure_rate = round((heal/confirm)*100,1)
    dead_rate = round((dead/confirm)*100,1)

    return jsonify({"cure_rate":cure_rate,"dead_rate":dead_rate})

@app.route("/api/r2")
def get_data_r2():
    province , confirm = [],[]

    # 从数据库中读取数据
    sql = "(SELECT province,sum(confirm) FROM cov.details WHERE update_time = (SELECT MAX(update_time) from cov.details) GROUP BY province) ORDER BY sum(confirm) DESC LIMIT 5;"
    conn, cursor = get_conn()
    cursor.execute(sql)
    data = cursor.fetchall()
    close_conn(conn, cursor)

    # 解析数据
    for i in data:
        province.append(i[0])
        confirm.append(i[1])
    confirm = list(map(int,confirm))
    # dic = dict(zip(province,confirm))
    #     # print(dic)
    #     # return dic
    return jsonify({"province":province,"confirm":confirm})


@app.route("/api/c2")
def get_data_c2():
    province , confirm = [],[]

    # 从数据库中读取数据
    sql = "(SELECT province,sum(confirm) FROM cov.details WHERE update_time = (SELECT MAX(update_time) from cov.details) GROUP BY province) ORDER BY sum(confirm);"
    conn, cursor = get_conn()
    cursor.execute(sql)
    data = cursor.fetchall()
    close_conn(conn, cursor)

    # 解析数据
    for i in data:
        province.append(i[0])
        confirm.append(i[1])
    confirm = list(map(int,confirm))
    dic = dict(zip(province,confirm))
    dictlist = []
    for key,value in dic.items():
        temps = {'name':key,'value':value}
        dictlist.append(temps)
    return jsonify({"datas": dictlist})


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=Flask,port=8090)

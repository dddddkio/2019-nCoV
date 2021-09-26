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


if __name__ == "__main__":
    date,confirm_add = [], []

    # 从数据库中读取数据
    sql = "SELECT ds,confirm_add FROM cov.history ORDER BY ds desc limit 7;"
    conn, cursor = get_conn()
    cursor.execute(sql)
    data = cursor.fetchall()
    close_conn(conn, cursor)

    # 解析数据
    for i in data:
        date.append(str(i[0])[:10])
        confirm_add.append(i[1])

    print(date)
    print(confirm_add)

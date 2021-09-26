# -×- coding:utf-8 -*-
import requests
import json
import pymysql
import time

headers={
    "userAgent" : "Mozilla\/5.0 (X11; Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/56.0.2924.87 Safari\/537.36"
}

def get_history():
    # 获取腾讯疫情历史数据
    url1 = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other"
    res1 = requests.get(url1, headers=headers)
    tmp1 = json.loads(res1.text)
    data_all1 = json.loads(tmp1['data'])

    # 解析数据
    history = {}
    for i in data_all1['chinaDayList']:
        date = (i['y'] + '-' + i['date']).replace(".", "-")
        history[date] = {
            "confirm": i["confirm"],
            "suspect": i["suspect"],
            "heal": i["heal"],
            "dead": i["dead"]
        }

    for i in data_all1['chinaDayAddList']:
        date = (i['y'] + '-' + i['date']).replace(".", "-")
        history[date].update({
            "confirm_add": i["confirm"],
            "suspect_add": i["suspect"],
            "heal_add": i["heal"],
            "dead_add": i["dead"]})

    return history

def get_detail():
    # 获取腾讯疫情详细数据
    url2 = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    res2 = requests.get(url2, headers=headers)
    tmp2 = json.loads(res2.text)
    data_all2 = json.loads(tmp2['data'])

    #解析数据
    today = []
    update_time = data_all2['lastUpdateTime']
    data_province = data_all2['areaTree'][0]['children']
    for prov in data_province:
        prov_name = prov['name']
        for city in prov['children']:
            city_name = city['name']
            confirm = city['total']['confirm']
            confirm_add = city['total']['nowConfirm']
            dead = city['total']['dead']
            heal = city['total']['heal']
            today.append([update_time, prov_name, city_name, confirm, confirm_add, dead, heal])

    return today

def get_conn():
    # 链接数据库
    conn=pymysql.connect(host='localhost',
                        user='root',
                        password='123456',
                        db='cov',
                        charset='utf8')
    cursor=conn.cursor()
    return conn,cursor

def close_conn(conn,cursor):
    # 关闭数据库
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def update_details(data):
    # 更新详细数据
    conn, cursor = None, None
    try:
        conn,cursor=get_conn()
        sql = "insert into details(update_time,province,city,confirm,confirm_add,heal,dead)values(%s,%s,%s,%s,%s,%s,%s)"
        sql_query="select %s=(select update_time from details order by id desc limit 1)"
        cursor.execute(sql_query,data[0][0])
        if not cursor.fetchone()[0]:
            print("{}开始更新数据".format(time.asctime()))
            for item in data:
                cursor.execute(sql,item)
            conn.commit()
            print("{}更新数据完毕".format(time.asctime()))
        else:
            print("{}已经是最新数据".format(time.asctime()))
    except Exception as e:
        print(e)
    finally:
        close_conn(conn,cursor)

def update_history(data):
    # 更新历史数据
    conn, cursor = None,None
    try:
        print("{}开始更新历史数据".format(time.asctime()))
        conn,cursor=get_conn()
        sql="insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query="select confirm from history where ds=%s"
        for k,v in data.items():
            if not cursor.execute(sql_query,k):
                cursor.execute(sql,[k,
                                v.get('confirm'),v.get('confirm_add'),
                                v.get('suspect'),v.get('suspect_add'),
                                v.get('heal'),v.get('heal_add'),
                                v.get('dead'),v.get('dead_add')])
        conn.commit()
        print("{}完成历史数据更新".format(time.asctime()))
    except Exception as e:
        print(e)
    finally:
        close_conn(conn,cursor)
        

if __name__ == "__main__":
    update_details(get_detail())
    update_history(get_history())
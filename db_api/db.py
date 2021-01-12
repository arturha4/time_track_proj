import asyncio

import mysql.connector
import datetime as dt

from services.vk_api import get_vk_status
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='ghghrfth',
    database='apiproject'
)

cursor = db.cursor()


#cursor.execute("CREATE DATABASE ApiProject")
#cursor.execute("CREATE TABLE tlg_bot_user (telegram_id VARCHAR(50) UNIQUE , vk_id VARCHAR(30),time_in_vk SMALLINT,"
#"start_time VARCHAR(5),end_time VARCHAR(5), urfu_login VARCHAR (40),urfu_password VARCHAR(30), github_login VARCHAR(39))")

l1={'vk_selected':True,'github_selected': True,
'urfu_selected':True, 'vk_login':'yaarturvsemsalam',
'urfu_login':'sadbooys.2001@gmail.com', 'urfu_password':'Arturka_2001',
'github_login':'sfgfd','start_time': '12:50','end_time': '12:53'}

l2={'vk_selected':True,'github_selected': True,
'urfu_selected':True, 'vk_login':'kkosmos1la',
'urfu_login':'sadbooys.2001@gmail.com', 'urfu_password':'Arturka_2001',
'github_login':'sfgfd','start_time': '12:50','end_time': '12:53'}

l3={'vk_selected':True,'github_selected': True,
'urfu_selected':True, 'vk_login':'horkworse',
'urfu_login':'sadbooys.2001@gmail.com', 'urfu_password':'Arturka_2001',
'github_login':'sfgfd','start_time': '12:50','end_time': '12:53'}

l4={'vk_selected':True,'github_selected': True,
'urfu_selected':True, 'vk_login':'id228121715',
'urfu_login':'sadbooys.2001@gmail.com', 'urfu_password':'Arturka_2001',
'github_login':'sfgfd','start_time': '12:50','end_time': '12:53'}

l5={'vk_selected':True,'github_selected': True,
'urfu_selected':True, 'vk_login':'id228121715',
'urfu_login':'sadbooys.2001@gmail.com', 'urfu_password':'Arturka_2001',
'github_login':'sfgfd','start_time': '12:50','end_time': '12:53'}

l6={'vk_selected':True,'github_selected': True,
'urfu_selected':True, 'vk_login':'igasshik',
'urfu_login':'sadbooys.2001@gmail.com', 'urfu_password':'Arturka_2001',
'github_login':'sfgfd','start_time': '12:45','end_time': '13:00'}

l7={'vk_selected':True,'github_selected': True,
'urfu_selected':True, 'vk_login':'igasshik',
'urfu_login':'sadbooys.2001@gmail.com', 'urfu_password':'Arturka_2001',
'github_login':'sfgfd','start_time': '12:50','end_time': '12:53'}

l8={'vk_selected':True,'github_selected': True,
'urfu_selected':True, 'vk_login':'id228121715',
'urfu_login':'sadbooys.2001@gmail.com', 'urfu_password':'Arturka_2001',
'github_login':'sfgfd','start_time': '12:50','end_time': '12:53'}

l9={'vk_selected':True,'github_selected': True,
'urfu_selected':True, 'vk_login':'id228121715',
'urfu_login':'sadbooys.2001@gmail.com', 'urfu_password':'Arturka_2001',
'github_login':'sfgfd','start_time': '12:50','end_time': '12:53'}

l10={'vk_selected':True,'github_selected': True,
'urfu_selected':True, 'vk_login':'id228121715',
'urfu_login':'sadbooys.2001@gmail.com', 'urfu_password':'Arturka_2001',
'github_login':'sfgfd','start_time': '12:50','end_time': '12:53'}




def show_databases():
    cursor.execute("SHOW DATABASES")
    for x in cursor:
        print(x)


def show_tables():
    cursor.execute('SHOW TABLES')
    for x in cursor:
        print(x)

def create_user(data,tlg_chat_id):
    try:
        sql = 'INSERT INTO tlg_bot_user (telegram_id,vk_id,time_in_vk,start_time,end_time,urfu_login,urfu_password,github_login) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        values = (tlg_chat_id, data['vk_login'], 0, data['start_time'], data['end_time'], data['urfu_login'],
                  data['urfu_password'], data['github_login'])
        cursor.execute(sql, values)
        db.commit()
    except Exception as e:
        return (f"Ошибка{e}")





def show_users():
    cursor.execute("SELECT * FROM tlg_bot_user")
    row=cursor.fetchall()
    for data in row:
        yield data


def delete_all_users():
    cursor.execute('DELETE FROM tlg_bot_user')
    db.commit()

def show_colummns():
    cursor.execute('SHOW COLUMNS FROM tlg_bot_user')
    for x in cursor:
        print(x)


def get_users_tel_id():
    cursor.execute('SELECT telegram_id FROM tlg_bot_user')
    for i in cursor.fetchall():
        yield i[0]

'''
брать текущее время и сравнивать с стартом и концом в бд,
запрашивать гет_статус вк и если пользователь онлайн добавлять время в сети вк
'''

def add_vk_time(vk_login):
    try:
        sql="UPDATE tlg_bot_user SET time_in_vk=time_in_vk+5 WHERE vk_id='{}'".format(vk_login)
        data=(vk_login)
        cursor.execute(sql,data)
    except Exception as e:
        print(e)
    finally:
        db.commit()


async def update_db(func):
    data = get_vk_track_info()
    dt_time_now = dt.datetime.now()
    str_time_now=dt_time_now.strftime('%H:%M')
    border=dt.datetime(2020, 12, 20, 23, 59, 0).strftime('%H:%M')
    delta= dt.timedelta(seconds=6)
    for user in data:
        dt_end_time = dt.datetime.strptime(user['end_time'], '%H:%M')
        if str_time_now > user['start_time'] and user['end_time'] > str_time_now and get_vk_status(user['vk_id']) == 1:
            add_vk_time(user['vk_id'])
        if dt.datetime.now().strftime('%H:%M')=='18:04':
            await func(user['vk_id'])





def get_vk_track_info():
    cursor.execute('SELECT vk_id,start_time,end_time FROM tlg_bot_user')
    row = cursor.fetchall()
    l=[{'vk_id':item[0],'start_time':item[1],'end_time':item[2]} for item in row]
    return l



async def get_user_info(tel_id):
    try:
        cursor.execute('SELECT * FROM tlg_bot_user WHERE telegram_id={}'.format(tel_id))
        row = cursor.fetchone()
        d={
            'telegram_id':row[0],
            'start_time':row[3],
            'end_time': row[4],
        }
        return d
    except:
        return None


print(*show_users())
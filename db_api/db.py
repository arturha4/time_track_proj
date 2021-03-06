import asyncio

from telegram_bot.config import db_password
import mysql.connector
import datetime as dt

from services.vk_api import get_vk_status

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password=db_password,
    database='apiproject'
)

cursor = db.cursor()


def show_databases():
    cursor.execute("SHOW DATABASES")
    for x in cursor:
        print(x)


def show_tables():
    cursor.execute('SHOW TABLES')
    for x in cursor:
        print(x)


def create_user(data, tlg_chat_id):
    try:
        sql = 'INSERT INTO tlg_bot_user (telegram_id,vk_id,time_in_vk,start_time,end_time,urfu_login,urfu_password,github_login) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        values = (tlg_chat_id, data['vk_login'], 0, data['start_time'], data['end_time'], data['urfu_login'],
                  data['urfu_password'], data['github_login'])
        cursor.execute(sql, values)
    except Exception as e:
        return (f"Ошибка{e}")
    finally:
        db.commit()


def get_users_data():
    cursor.execute("SELECT * FROM tlg_bot_user")
    row = cursor.fetchall()
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
        sql = "UPDATE tlg_bot_user SET time_in_vk=time_in_vk+5 WHERE vk_id='{}'".format(vk_login)
        data = (vk_login)
        cursor.execute(sql, data)
    except Exception as e:
        print(e)
    finally:
        db.commit()


async def change_time(start_time1,end_time1,tel_id):
    try:
        sql=('UPDATE tlg_bot_user SET start_time=%s,end_time=%s WHERE telegram_id=%s')
        data=(start_time1,end_time1,tel_id)
        cursor.execute(sql,data)
    except Exception as e:
        print(e)
    finally:
        db.commit()


async def update_db(func, urfuStat, gitStat):
    data = get_track_info()
    str_time_now = dt.datetime.now().strftime('%H:%M')
    delta = dt.timedelta(minutes=5)
    for user in data:
        user_end_time = user['end_time']
        dt_end_time = dt.datetime.strptime(user_end_time, '%H:%M')
        if user['vk_id'] != 0 and user['start_time'] < str_time_now < user_end_time and get_vk_status(user['vk_id']) == 1:
            add_vk_time(user['vk_id'])
        if user_end_time <= str_time_now and str_time_now <= (dt_end_time + delta).strftime('%H:%M'):
            await func(user['telegram_id'],str(user['time_in_vk']))
            await urfuStat(user['urfu_login'], user['urfu_password'], user['telegram_id'])
            await gitStat(user['github_login'], user['telegram_id'])

def get_track_info():
    cursor.execute('SELECT vk_id,start_time,end_time,telegram_id,urfu_login,urfu_password,github_login,time_in_vk FROM tlg_bot_user')
    row = cursor.fetchall()
    l = [{'vk_id': item[0],
          'start_time': item[1],
          'end_time': item[2],
          'telegram_id': item[3],
          'urfu_login': item[4],
          'urfu_password': item[5],
          'github_login': item[6],
          'time_in_vk':item[7]} for item in row]
    return l

async def get_user_info(tel_id):
    try:
        cursor.execute('SELECT * FROM tlg_bot_user WHERE telegram_id={}'.format(tel_id))
        row = cursor.fetchone()
        d = {
            'telegram_id': row[0],
            'start_time': row[3],
            'end_time': row[4],
        }
        return d
    except:
        return None


print(*get_users_data())
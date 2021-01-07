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

l={'vk_selected':True,'github_selected': True,
'urfu_selected':True, 'vk_login':'asd',
'urfu_login':'sadbooys.2001@gmail.com', 'urfu_password':'Arturka_2001',
'github_login':'sfgfd','start_time': '10:45','end_time': '22:30'}


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
        print(data)


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

def update_vk_time(vk_login):
    sql=cursor.execute('UPDATE tlg_bot_user SET time_in_vk=time_in_vk+4 WHERE vk_id={}'.format(vk_login))






def update_vk_db_times():
    data=get_vk_track_info()
    time_now = dt.datetime.now().strftime('%H:%M')
    for user in data:
        if time_now > data['start_time']and data['end_time']>time_now and get_vk_status(data['vk_id'])==1:
            pass





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

show_users()
update_vk_time('Dcgtd')
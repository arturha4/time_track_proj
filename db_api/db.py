import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='ghghrfth',
    database='apiproject'
)

cursor = db.cursor()


#cursor.execute("CREATE DATABASE ApiProject")
#cursor.execute("CREATE TABLE tlg_bot_user (telegram_id VARCHAR(50) UNIQUE , vk_id VARCHAR(30),time_in_vk SMALLINT,start_time VARCHAR(5),end_time VARCHAR(5), urfu_login VARCHAR (40),urfu_password VARCHAR(30), github_login VARCHAR(39))")
'''
('vk_selected', True) ('github_selected', True) 
('urfu_selected', True) ('vk_login', 'asd') 
('urfu_login', 'sadbooys.2001@gmail.com') ('urfu_password', 'Arturka_2001') 
('github_login', 'sfgfd') 
('start_time', '10:45') ('end_time', '22:30')
'''

l=[('vk_selected', True),('github_selected', True),
('urfu_selected', True), ('vk_login', 'asd') ,
('urfu_login', 'sadbooys.2001@gmail.com'), ('urfu_password', 'Arturka_2001'),
('github_login', 'sfgfd'),
('start_time', '10:45'), ('end_time', '22:30')]


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
        sql='INSERT INTO tlg_bot_user (telegram_id,vk_id,time_in_vk,start_time,end_time,urfu_login,urfu_password,github_login) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        values=(tlg_chat_id,data[3][1],0,data[6][1],data[7][1],data[4][1],data[5][1],data[6][1])
        cursor.execute(sql,values)
        db.commit()
    except:
      print('error')
    finally:
       print(*data)

# def create_user(tel_id,vk_id,time_in_vk=0):
#     sql='INSERT INTO tlg_bot_user (telegram_id, time_in_vk, vk_id) VALUES(%s,%s,%s)'
#     values=(tel_id,time_in_vk,vk_id)
#     cursor.execute(sql,values)
#     db.commit()


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


def update_track_time(tel_id):
    pass
#обновлять данные по телеграм айди т.к. он индивидуальный
#обработать исключение при одинаковом id
def get_user_info(tel_id):
    try:
        cursor.execute('SELECT * FROM User WHERE telegram_id={}'.format(tel_id))
        row = cursor.fetchone()
        return row
    except:
        return ('Ошибка')


import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='ghghrfth',
    database='apiproject'
)

cursor = db.cursor()


#cursor.execute("CREATE DATABASE ApiProject") создал бд
#cursor.execute("CREATE TABLE User (telegram_id VARCHAR(50) UNIQUE , vk_id VARCHAR(30),time_in_vk SMALLINT,start_time VARCHAR(5),end_time VARCHAR(5))") #создал table


def show_databases():
    cursor.execute("SHOW DATABASES")
    for x in cursor:
        print(x)


def show_tables():
    cursor.execute('SHOW TABLES')
    for x in cursor:
        print(x)


def create_user(tel_id,vk_id,time_in_vk=0):
    sql='INSERT INTO user (telegram_id, time_in_vk, vk_id) VALUES(%s,%s,%s)'
    values=(tel_id,time_in_vk,vk_id)
    cursor.execute(sql,values)
    db.commit()


def show_users():
    cursor.execute("SELECT * FROM user")
    row=cursor.fetchall()
    for data in row:
        print(data)


def delete_all_users():
    cursor.execute('DELETE FROM user')
    db.commit()

def show_colummns():
    cursor.execute('SHOW COLUMNS FROM user')
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


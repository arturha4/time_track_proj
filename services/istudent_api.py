import requests
from datetime import datetime
from telegram_bot.tel_bot_api_proj import bot


def login(userName, password):
    s = requests.Session()
    '''
    ts = int(i)
    print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
    '''
    data = {"UserName": userName,
            "Password": password,
            'AuthMethod': 'FormsAuthentication'}
    url = 'https://istudent.urfu.ru/auth/'
    r = s.get(url)
    r = s.post(r.url, data)
    if r.url.split('/')[-1] != '?auth-ok':
        return -1
    urlCalendar = 'https://istudent.urfu.ru/itribe/schedule_its/?access-token=cdCzdUtX1vf8vPAH&callback' \
                  '=jQuery11100037296088033118124_1605893102341 '
    a = s.post(urlCalendar)
    return a


async def getLessons(userName, password, telId):
    a = login(userName, password)
    s = datetime.now().strftime('%Y-%m-%d')
    dt = datetime.strptime(s, '%Y-%m-%d')
    unix3 = int((dt - datetime(1970, 1, 1)).total_seconds())  # - время по Гринвичу
    await bot.send_message(chat_id=telId, text='Учебная активность в УрФУ за весь день:')
    if str(unix3) in a.json()['schedule']:
        ls = a.json()["schedule"][str(unix3)]['events']
        for i in ls:
            begin_time = ls[i]['begin_time']
            end_time = ls[i]['end_time']
            await bot.send_message(chat_id=telId, text=f'{begin_time} - {end_time} {ls[i]["discipline"]} - {ls[i]["comment"]}')


def main():
    pass


if __name__ == '__main__':
    getLessons('k1n5lobal@gmail.com', '12345567768vk11337228504dfyZ@')

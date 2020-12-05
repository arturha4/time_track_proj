import requests

s = requests.Session()

data = {"UserName": 'k1n5lobal@gmail.com',
        "Password": '12345567768vk11337228504dfyZ@',
        'AuthMethod': 'FormsAuthentication'}
url = 'https://istudent.urfu.ru/auth/'
r = s.get(url)
r = s.post(r.url, data)
urlCalendar = 'https://istudent.urfu.ru/s/schedule'
a = s.post(urlCalendar)
print(a.text)

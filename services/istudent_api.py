import requests


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


def main():
    pass


if __name__ == '__main__':
    main()

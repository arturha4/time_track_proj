import requests


def getEvents(login):
    r = requests.get(f'https://api.github.com/users/{login}/events')
    print(r.json())
    for i in r.json():
        print(i['created_at'] + ' ' + i['type'])


# PullRequestEvent - сделан PullRequest
# CreateEvent - создана ветка


def main():
    getEvents('k1n5-bt')


if __name__ == '__main__':
    main()

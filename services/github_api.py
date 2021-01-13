import requests
from datetime import datetime
from telegram_bot.tel_bot_api_proj import bot

PATTERN_IN = "%Y-%m-%dT%H:%M:%SZ"  # формат даты внутри json
PATTERN_OUT = "%d.%m.%Y %H:%M"  # формат даты, который нам нужен на выходе


async def getEvents(login, telId):
    r = requests.get(f'https://api.github.com/users/{login}/events')
    for i in r.json():
        date = datetime.strptime(i['created_at'], PATTERN_IN)
        dateOutFormat = datetime.strftime(date, PATTERN_OUT)
        await bot.send_message(chat_id=telId, text='Дневная активность в github за весь день:')
        if dateOutFormat.split()[0] == datetime.today().strftime(PATTERN_OUT).split()[0]:
            await bot.send_message(chat_id=telId, text=dateOutFormat.split()[1] + ' ' + i['type'])
        else:
            break


# PullRequestEvent - сделан PullRequest
# CreateEvent - создана ветка


def main():
    pass


if __name__ == '__main__':
    main()

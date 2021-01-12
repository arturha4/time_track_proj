import vk
from telegram_bot import config
vk_token = config.vk_tkn
session = vk.Session()
vk_api = vk.API(session)


def get_vk_status(id):
    data = vk_api.users.get(v=5.124, user_ids=str(id), fields='online, last_seen', access_token=vk_token)[0]['online']
    return data






import vk
vk_token = "46e50d8c46e50d8c46e50d8c8a46917fc2446e546e50d8c196fd185478ce57d33254a43"
session = vk.Session()
vk_api = vk.API(session)


def get_vk_status(id):
    data = vk_api.users.get(v=5.124, user_ids=str(id), fields='online, last_seen', access_token=vk_token)[0]['online']
    return data






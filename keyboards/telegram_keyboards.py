from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext

vk_btn = InlineKeyboardButton('ВК', callback_data='vk')
git_btn = InlineKeyboardButton('GitHub', callback_data='github')
urfu_btn = InlineKeyboardButton('UrFU Account', callback_data='urfu')

inline_kb1 = InlineKeyboardMarkup().add(vk_btn, git_btn, urfu_btn)
inline_git_urfu_kb = InlineKeyboardMarkup().add(git_btn, urfu_btn)

vk_login_yes = InlineKeyboardButton('Да', callback_data='yes')
vk_login_no = InlineKeyboardButton('Нет', callback_data='no')

inline_vk_yes_no_kb = InlineKeyboardMarkup().add(vk_login_yes, vk_login_no)

inline_vk_github_kb = InlineKeyboardMarkup().add(vk_btn, git_btn)
inline_vk_urfu_kb = InlineKeyboardMarkup().add(vk_btn, urfu_btn)
inline_github_urfu = InlineKeyboardMarkup().add(urfu_btn, git_btn)
inline_github_kb = InlineKeyboardMarkup().add(git_btn)
inline_vk_kb = InlineKeyboardMarkup().add(vk_btn)
inline_urfu_kb = InlineKeyboardMarkup().add(urfu_btn)

time1_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

for i in range(6, 24):
    hour = f'0{i}' if i < 10 else i
    time1_kb.insert(f'{hour}:00')
    for j in range(15, 46, 15):
        time1_kb.insert(f'{hour}:{j}')


async def get_choosed_keyboard(state: FSMContext):
    log = await state.get_data()
    vk, github, urfu = log.get('vk_selected'), log.get('github_selected'), log.get('urfu_selected')
    if not vk and not github and urfu:
        return inline_vk_github_kb
    if not vk and github and not urfu:
        return inline_vk_urfu_kb
    if vk and not github and not urfu:
        return inline_github_urfu
    if vk and not github and urfu:
        return inline_github_kb
    if vk and github and not urfu:
        return inline_urfu_kb
    if not vk and github and urfu:
        return inline_vk_kb
    if not urfu and not github and not vk:
        return inline_kb1
    else:
        return None

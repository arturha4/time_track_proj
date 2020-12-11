from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
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


async def get_choosed_keyboard(state: FSMContext):
    log = await state.get_data()
    vk, github, urfu = await log.get('vk_selected'),await log.get('github_selected'),await log.get('urfu_selected')
    if vk == False and github == False and urfu == True:
        return inline_vk_github_kb
    if vk == False and github == True and urfu == False:
        return inline_vk_urfu_kb
    if vk == True and github == False and urfu == False:
        return inline_github_urfu
    if vk == True and github == False and urfu == True:
        return inline_github_kb
    if vk == True and github ==True and urfu == False:
        return inline_urfu_kb
    if vk == False and github == True and urfu == True:
        return inline_vk_urfu_kb




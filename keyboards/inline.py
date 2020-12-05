from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

vk_btn = InlineKeyboardButton('ВК', callback_data='vk')
git_btn = InlineKeyboardButton('GitHub', callback_data='github')
urfu_btn = InlineKeyboardButton('UrFU Account', callback_data='urfu')


inline_kb1 = InlineKeyboardMarkup().add(vk_btn,git_btn,urfu_btn)


vk_login_yes=InlineKeyboardButton('Да', callback_data='yes')
vk_login_no=InlineKeyboardButton('Нет', callback_data='no')
#vk_user_page=InlineKeyboardButton('Перейти',url=f'https://vk.com/')



inline_vk_kb=InlineKeyboardMarkup().add(vk_login_yes,vk_login_no)
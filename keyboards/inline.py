from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

vk_btn = InlineKeyboardButton('ВК', callback_data='vk')
git_btn = InlineKeyboardButton('GitHub', callback_data='github')
urfu_btn = InlineKeyboardButton('UrFU Account', callback_data='urfu')

inline_kb1 = InlineKeyboardMarkup().add(vk_btn,git_btn,urfu_btn)
inline_git_urfu_kb=InlineKeyboardMarkup().add(git_btn,urfu_btn)

vk_login_yes=InlineKeyboardButton('Да', callback_data='yes')
vk_login_no=InlineKeyboardButton('Нет', callback_data='no')

inline_vk_yes_no_kb=InlineKeyboardMarkup().add(vk_login_yes,vk_login_no)


inline_vk_github_kb=InlineKeyboardMarkup().add(vk_btn,git_btn)
inline_vk_urfu_kb=InlineKeyboardMarkup().add(vk_btn,urfu_btn)
inline_github_urfu=InlineKeyboardMarkup().add(urfu_btn,git_btn)
inline_github_kb=InlineKeyboardMarkup().add(git_btn)
inline_vk_kb=InlineKeyboardMarkup().add(vk_btn)
inline_urfu_kb=InlineKeyboardMarkup().add(urfu_btn)


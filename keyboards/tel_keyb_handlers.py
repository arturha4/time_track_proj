from telegram_bot import tel_bot_api_proj
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
from aiogram.dispatcher import FSMContext
from questions.Test import Test

from  telegram_bot.tel_bot_api_proj import bot,dp

@dp.callback_query_handler(text_contains='urfu', state=Test.TAKE_URFU_LOGIN)
async def set_github(call:types.CallbackQuery,state=FSMContext):
    await bot.send_message(chat_id=call.id,text='Введи свой логин от личного кабинета урфу')


import aiogram
import asyncio
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

import database as db
from aiogram import Bot, Dispatcher, executor, types
from keyboards import inline
from aiogram.types import InlineKeyboardButton
from aiogram.dispatcher.filters import Command
from questions.Test import Test


token = '1260767500:AAFq0jjuZ6isvMj4OPn8yizFRDmR8yG4Glc'

logging.basicConfig(level=logging.INFO)

bot=Bot(token=token)
dp=Dispatcher(bot,storage=MemoryStorage())



#start message
@dp.message_handler(commands=['start'])
async def start_message(message:types.Message):
    await message.answer("Привет, я бот для учета времени, я помогу тебе отслеживать твою активность "
                         "в социальных сетях и не только!\n"
                         "Давай начнём, введи /auth для регистрации")


@dp.message_handler(commands=['help'],state=None)
async def start_message(message:types.Message):
    await message.answer("Список команд:\n/auth - авторизация в сервисах \n/starttime - назначить/изменить время начала трекинга\n/endtime - назначить/изменить время конца трекинга")


@dp.message_handler(Command('auth'),state=None)
async def auth(message:types.Message):
    await message.answer('Выбери сервисы, кооторые ты хочешь отслеживать',reply_markup=inline.inline_kb1)
    await  Test.AUTH.set()


@dp.message_handler(state=Test.VK_LOGIN)
async def verify_vk_auth(messsage:types.Message,state:FSMContext):
    await messsage.answer(text=f'https://vk.com/{messsage.text}',reply_markup=inline.inline_vk_kb)

@dp.message_handler(state=Test.VK_LOGIN)
async def xxx(messsage:types.Message,state:FSMContext):
    pass



#InlineButtonsHandlers

@dp.callback_query_handler(text_contains='vk',state=Test.AUTH)#сделать стейт чтобы много раз не выходило
async def login_vk(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, "Введи свой id vk или ник.")
    await Test.VK_LOGIN.set()
#нужно добавить обработчик состояния при сообщении проверять будет по стейту
@dp.callback_query_handler(text_contains='yes',state=Test.VK_LOGIN)
async def success_auth_vk(call: types.CallbackQuery):
    answer = call.messsage.text
    await call.state.update_data(vk_login=answer)
    await bot.send_message(call.from_user.id, "Отлично")
    await Test.VK_AUTH.set()

@dp.callback_query_handler(text_contains='no',state=Test.VK_LOGIN)
async def unsucces_auth_vk(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, 'Проверь ник ещё раз, если что-то не так введи данные ещё раз')




if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)
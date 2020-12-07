import aiogram
import asyncio
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from db_api import db
from aiogram import Bot, Dispatcher, executor, types
from keyboards import inline
from aiogram.types import InlineKeyboardButton
from aiogram.dispatcher.filters import Command
from questions.Test import Test
token = '1260767500:AAFq0jjuZ6isvMj4OPn8yizFRDmR8yG4Glc'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())


# start message
@dp.message_handler(commands=['start'], state=None)
async def start_message(message: types.Message):
    await message.answer("Привет, я бот для учета времени, я помогу тебе отслеживать твою активность "
                         "в социальных сетях и не только!\n"
                         "Давай начнём, введи /auth для регистрации")


@dp.message_handler(commands=['help'])
async def start_message(message: types.Message):
    await message.answer(
        "Список команд:\n/auth - авторизация в сервисах \n/starttime - назначить/изменить время начала трекинга\n/endtime - назначить/изменить время конца трекинга")


@dp.message_handler(Command('auth'), state=None)
async def auth(message: types.Message):
    await message.answer('Выбери сервисы, которые ты хочешь отслеживать', reply_markup=inline.inline_kb1)
    await Test.SET_SERVICE.set()

# @dp.message_handler(state=Test.)
# async def xxx(messsage: types.Message, state: FSMContext):
#     pass


@dp.message_handler(state=Test.TAKE_VK_ID)
async def verify_vk_auth(message: types.Message, state: FSMContext):
    await state.update_data(vk_login=message.text)
    await message.answer(text=f'https://vk.com/{message.text}', reply_markup=inline.inline_vk_kb)
    log=await state.get_data()
    l=log.get('vk_login')
    await message.answer(text=l)
    await Test.VK_YES.set()



# InlineButtonsHandlers

@dp.callback_query_handler(text_contains='vk',state=Test.SET_SERVICE)#сделать стейт чтобы много раз не выходило
async def login_vk(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, "Введи свой id vk или ник.")
    await Test.TAKE_VK_ID.set()


# нужно добавить обработчик состояния при сообщении проверять будет по стейту
@dp.callback_query_handler(text_contains='yes', state=Test.VK_YES)
async def success_auth_vk(call: types.CallbackQuery, state:FSMContext):
    await bot.send_message(call.from_user.id, "Отлично!")
    await Test.VK_END.set()
    id=await state.get_data()
    x=id.get('vk_login')
    db.create_user(call.from_user.id,x)
    #перекинуть на авторизацию на гитхабе, урфу

@dp.callback_query_handler(text_contains='no', state=Test.VK_YES)
async def unsucces_auth_vk(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, 'Проверь ник ещё раз, если что-то не так введи данные ещё раз')
    await Test.TAKE_VK_ID.set()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

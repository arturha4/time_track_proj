from aiogram.dispatcher.filters.state import StatesGroup,State


class Test(StatesGroup):
    AUTH=State()
    VK_LOGIN=State()
    VK_AUTH=State()
    VK_END=State()
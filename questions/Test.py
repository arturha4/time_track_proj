from aiogram.dispatcher.filters.state import StatesGroup,State


class Test(StatesGroup):
    SET_SERVICE=State()
    TAKE_VK_ID=State()
    VK_END=State()
    VK_YES=State()
    VK_NO=State()

from aiogram.dispatcher.filters.state import StatesGroup,State


class Test(StatesGroup):
    SET_SERVICE=State()
    TAKE_VK_ID=State()
    VK_END=State()
    VK_YES=State()
    VK_NO=State()
    TAKE_URFU_LOGIN=State()
    TAKE_URFU_PASSWORD=State()
    TAKE_GITHUB_LOGIN=State()
    DEFAULT=State()
    SET_START_TIME=State()
    SET_END_TIME=State

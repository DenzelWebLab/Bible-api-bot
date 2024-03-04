from aiogram.filters.state import StatesGroup, State


class StateAdmins(StatesGroup):
    text = State()
    text_pic = State()
    pic = State()
    group_text = State()

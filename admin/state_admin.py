from aiogram.filters.state import StatesGroup, State


class StateAdmins(StatesGroup):
    text = State()
    button = State()
    pic = State()
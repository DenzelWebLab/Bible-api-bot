from aiogram.filters.state import StatesGroup, State


class StateWord(StatesGroup):
    query_word: str = State()


class StateIndex(StatesGroup):
    index: str = State()


class StateWeather(StatesGroup):
    city: str = State()

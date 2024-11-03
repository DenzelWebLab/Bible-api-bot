from aiogram.filters.callback_data import CallbackData


class CallFilter(CallbackData, prefix='my'):
    foo: str
    bar: str

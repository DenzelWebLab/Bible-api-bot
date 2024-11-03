from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup


def builder_keyboard(
        text=str | list[str],
        callback=str | list[str],
        sizes=str | list[int],
        **kwargs
        ) -> InlineKeyboardMarkup:

    builder = InlineKeyboardBuilder()

    if isinstance(text, str):
        text = [text]
    if isinstance(callback, str):
        callback = [callback]
    if isinstance(sizes, int):
        sizes = [sizes]

    [builder.button(text=txt, callback_data=cb)
        for txt, cb in zip(text, callback)]

    builder.adjust(*sizes)
    return builder.as_markup(**kwargs)

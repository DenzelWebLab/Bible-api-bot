from string import punctuation

from aiogram import types, Router

from filters.chat_filters import ChatTypeFilter

group_router = Router()
group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))


restricted_words = {'lol', 'gap'}


def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))


@group_router.message()
async def cleaner(message: types.Message):
    if restricted_words.intersection(clean_text(message.text.lower()).split()):
        await message.answer(f'{message.from_user.first_name}, непорушуйте правила!')
        await message.delete()

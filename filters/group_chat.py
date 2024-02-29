from string import punctuation

from aiogram import F, types, Router


from filters.chat_filters import ChatTypeFilter
from for_dell import restricted_words

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))
user_group_router.edited_message.filter(ChatTypeFilter(['group', 'supergroup']))


restricted_words = restricted_words

def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))


@user_group_router.edited_message()
@user_group_router.message()
async def cleaner(message: types.Message):
    if restricted_words.intersection(clean_text(message.text.lower()).split()):
        await message.delete()
        await message.answer(f"{message.from_user.first_name}, правила не порушувати")

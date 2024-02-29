from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram import Router, F

from states.save_state_bot import StateIndex
from cllasses.index_ import IndexSearch
from keyboards.inlaine_button import edit_button_index

index_s = IndexSearch()
index_start_router = Router()
index_next_router = Router()


@index_start_router.callback_query(F.data == 'index')
async def start_index(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StateIndex.index)
    await callback.message.answer(text='🔻Вибрана опція пошуку по індексу\n'
                                       '❗️Для коректного вводу  використати  англійські літери\n'
                                       '❗️Приклад вводу: MAT.1.1\n'
                                       '❗️Три літери це індекс книги\n'
                                       '❗️Перша цифра це номер глави\n'
                                       '❗️Друга цифра це номер вірша\n'
                                       '❗️Список індексів дивитись /listindex'
                                       '❗️для відміни /cancelindex')

    await callback.answer('🔍')


@index_start_router.message(Command("cancelindex"))
@index_start_router.message(F.text.casefold() == "cancelindex")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer(text='Відмінено', reply_markup=edit_button_index)


@index_start_router.message(StateIndex.index)
async def next_index_step(message: Message, state: FSMContext):
    try:
        index = message.text.strip()
        await state.update_data(index=index)
        answer_text = index_s.get_index(index=index)
        await message.answer(answer_text, reply_markup=edit_button_index)
        await state.clear()
    except KeyError:
        await message.reply(text='Невірний формат', reply_markup=edit_button_index)


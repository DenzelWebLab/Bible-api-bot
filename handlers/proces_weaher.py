from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message

from states.save_state_bot import StateWeather
from cllasses.weather_info import Weather
from keyboards.inlaine_button import weather_update, select_menu_button


weather_router = Router()
wh = Weather()


@weather_router.callback_query(F.data == 'weather')
async def start_weather(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StateWeather.city)
    await callback.message.answer(text='🔻Опція погода\nВедіть назву міста:\n'
                                       'Для відміни /cancel')
    await callback.answer('🌤')


@weather_router.message(Command("cancel"))
@weather_router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer(text='*Відмінено*, виберіть дію', reply_markup=select_menu_button)


@weather_router.message(StateWeather.city)
async def next_step(message: Message, state: FSMContext):
    try:
        name_city = message.text.strip()
        text_answer = wh.get_description(city=name_city)
        await message.answer(text_answer, reply_markup=weather_update)
        await state.clear()
    except KeyError:
        await message.reply(text='Не вірний формат воду, ведіть назву міста', reply_markup=weather_update)


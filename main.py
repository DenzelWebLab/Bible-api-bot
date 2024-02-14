import asyncio
import logging
# import sys

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode

from config import token
from commands.bot_list_cmd import private
from handlers.call_back_handler import router_callback_handler
from handlers.main_handler import router_main_handler
from handlers.state_query_word import process_state_word, next_step_for_word
from handlers.start_books import constructor_index
from handlers.proces_weaher import weather_router, next_weather_step
from handlers.index_search import index_start_router, index_next_router
from commands.run_stop import start_bot, stop_bot
from admin.admin_handler import admin_router
from commands.get_commands import commands_router


# ALLOWED_UPDATES = ['message', 'edited_message']

TOKEN = token
router = Router()
dp = Dispatcher()
dp.startup()
dp.include_router(router_callback_handler)
dp.include_router(router_main_handler)
dp.include_router(process_state_word)
dp.include_router(next_step_for_word)
dp.include_router(constructor_index)
dp.include_router(weather_router)
dp.include_router(next_weather_step)
dp.include_router(index_start_router)
dp.include_router(index_next_router)
dp.include_router(admin_router)
dp.include_router(commands_router)


async def main() -> None:
    # Ініціалізуйте екземпляр бота з режимом аналізу за замовчуванням, який буде передано всім викликам API
    bot = Bot(TOKEN, parse_mode=ParseMode.MARKDOWN)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    # І диспетчеризація запущених подій
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

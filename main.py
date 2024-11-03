import asyncio
import logging

from aiogram import Bot, Dispatcher, Router, types
# from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import TOKEN, ADMIN_ID
from commands.bot_list_cmd import private, group, admin

from admin.admin_handler import admin_router
from commands.commands import commands_router
from group_hahdler.group import group_router
from private_handler.private import private_router

TOKEN = TOKEN
router = Router()
dp = Dispatcher()

# new version router
dp.include_router(group_router)
dp.include_router(private_router)
dp.include_router(commands_router)
dp.include_router(admin_router)


async def main() -> None:
    # session = AiohttpSession(proxy=PROXY)
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    bot.my_admins_list = []

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=group, scope=types.BotCommandScopeAllGroupChats())
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=admin, scope=types.BotCommandScopeChat(chat_id=ADMIN_ID))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())




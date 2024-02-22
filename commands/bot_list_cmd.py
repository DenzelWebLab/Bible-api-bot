from aiogram.types import BotCommand


private = [
    BotCommand(command='start', description='Запуск-перезапуск бота'),
    BotCommand(command='help', description='Допомога'),
    BotCommand(command='password', description='Створити пароль'),
    BotCommand(command='listindex', description='Список індексів'),
    BotCommand(command='admin', description='admin_only🔐')
]

group = [
    BotCommand(command='rules', description='Правила')
]

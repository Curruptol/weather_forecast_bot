import logging
from handlers import router
import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.chat_action import ChatActionMiddleware


async def main():
    load_dotenv()  # загрузка токена
    bot = Bot(os.environ['BOT_TOKEN'])
    dp = Dispatcher(storage=MemoryStorage())  # настройка хранения данных
    dp.include_router(router)  # подключение роутеров к диспетчеру
    dp.message.middleware(ChatActionMiddleware())  # подключение chat action
    await bot.delete_webhook(drop_pending_updates=True)  # удаление веб хука и очистка апдейтов, которые могли
    # накопиться пока бот не работал
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())  # запуск пуллинга


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # уровень логирования
    asyncio.run(main())

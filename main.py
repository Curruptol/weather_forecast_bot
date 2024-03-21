import logging
from handlers import router
import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.chat_action import ChatActionMiddleware


async def main():
    load_dotenv()
    bot = Bot(os.environ['BOT_TOKEN'])
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    dp.message.middleware(ChatActionMiddleware())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

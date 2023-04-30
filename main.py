import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.core import settings
from src.handlers import main_router


async def main():
    bot = Bot(token=settings.bot.token, parse_mode="HTML")
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_router(main_router)

    try:
        await dp.start_polling(
            bot,
            # allowed_updates=["message", "callback_query", "chat_member"]
            allowed_updates=dp.resolve_used_update_types(),
        )
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

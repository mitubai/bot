from bot import bot, dp, db
from handlers.start import start_router
from handlers.film import film_router
from aiogram import Bot
import asyncio
import logging

async def on_startup(bot: Bot):
    db.create_tables()

async def main():
    dp.include_router(start_router)

    dp.include_router(film_router)

    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
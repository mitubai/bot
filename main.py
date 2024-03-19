from bot import bot, dp, db
from handlers.start import start_router
from handlers.film import film_router
from handlers.anime import anime_router
from handlers.cartoons import cartoons_router
from handlers.help import help_router
from handlers.survey import survey_router
from handlers.order_book import order_book_router
from handlers.really_order import real_order_router
from aiogram import Bot
import asyncio
import logging

async def on_startup(bot: Bot):
    db.create_tables()

async def main():
    dp.include_router(start_router)
    dp.include_router(film_router)
    dp.include_router(cartoons_router)
    dp.include_router(anime_router)
    dp.include_router(help_router)
    dp.include_router(survey_router)
    dp.include_router(order_book_router)
    dp.include_router(real_order_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
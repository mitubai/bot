from bot import bot, dp, db
from handlers.start import start_router
from handlers.film import film_router
from handlers.anime import anime_router
from handlers.serials import serials_router
from handlers.cartoons import cartoons_router
from handlers.help import help_router
from handlers.survey import survey_router
import asyncio
import logging

async def on_startup():
    db.drop_tables()
    db.create_tables()
    db.populate_tables()

async def main():
    dp.include_router(start_router)
    dp.include_router(film_router)
    dp.include_router(cartoons_router)
    dp.include_router(anime_router)
    dp.include_router(serials_router)
    dp.include_router(help_router)
    dp.include_router(survey_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
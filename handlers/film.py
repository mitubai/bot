from aiogram import Router, F, types
from aiogram.filters import Command
from keyboards.films_kb import (film_kb,film_kb2,film_kb3,film_kb4,film_kb5,film_kb6)
import logging

film_router = Router()

@film_router.message(Command('films'))
async def show_films(message: types.Message):
    logging.info(message.from_user)
    await message.answer("Какой жанр фильмов вы хотите?", reply_markup=film_kb())

@film_router.callback_query(F.data == "Comedian_for_film")
async def show_comedian(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите фильм:", reply_markup=film_kb2())


@film_router.callback_query(F.data == "Horrors_for_film")
async def show_horror(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите фильм:", reply_markup=film_kb3())

@film_router.callback_query(F.data == "Fantastic_for_film")
async def show_fantastic(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите фильм:", reply_markup=film_kb4())

@film_router.callback_query(F.data == "Thrillers_for_film")
async def show_thrillers(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите фильм:", reply_markup=film_kb5())

@film_router.callback_query(F.data == "Popular_for_film")
async def show_populars(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите фильм:", reply_markup=film_kb6())


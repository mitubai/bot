from aiogram import Router, F, types
from aiogram.filters import Command
from keyboards.keyboard import (film_kb, film_kb3, film_kb4, film_kb6, proch, dune, potter)
import logging
from handlers.get_data import Data
from pathlib import Path

film_router = Router()


@film_router.message(Command('films'))
async def show_films(message: types.Message):
    logging.info(message.from_user)
    await message.answer("Какой жанр фильмов вы хотите?", reply_markup=film_kb())


@film_router.callback_query(F.data == "Horrors_for_film")
async def show_horror(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите фильм:", reply_markup=film_kb3())


@film_router.callback_query(F.data == "Fantastic_for_film")
async def show_fantastic(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите фильм:", reply_markup=film_kb4())


@film_router.callback_query(F.data == "Popular_for_film")
async def show_populars(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите фильм:", reply_markup=film_kb6())


data = Data()


@film_router.callback_query(F.data == "proch")
async def show_proch(callback: types.CallbackQuery):
    first = data.get_proch()
    info = f"Название: {first[1]}\nГод выпуска: {first[2]}\nОписание: {first[3]}"
    file_path = Path(__file__).parent.parent / "images" / first[4]
    file = types.FSInputFile(file_path)
    logging.info(file_path)
    await callback.message.answer_photo(file, caption=info, reply_markup=proch())


@film_router.callback_query(F.data == "potter")
async def show_proch(callback: types.CallbackQuery):
    first = data.get_potter()
    info = f"Название: {first[1]}\nГод выпуска: {first[2]}\nОписание: {first[3]}"
    file_path = Path(__file__).parent.parent / "images" / first[4]
    file = types.FSInputFile(file_path)
    logging.info(file_path)
    await callback.message.answer_photo(file, caption=info, reply_markup=potter())


@film_router.callback_query(F.data == "dune")
async def show_proch(callback: types.CallbackQuery):
    first = data.get_dune()
    info = f"Название: {first[1]}\nГод выпуска: {first[2]}\nОписание: {first[3]}"
    file_path = Path(__file__).parent.parent / "images" / first[4]
    file = types.FSInputFile(file_path)
    logging.info(file_path)
    await callback.message.answer_photo(file, caption=info, reply_markup=dune())
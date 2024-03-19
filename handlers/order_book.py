from aiogram import Router, F, types
from aiogram.filters import Command
import logging
from db.base import Database
from pathlib import Path
from keyboards.order_book_kb import (order_book_kb,
                                     anime_book_kb,
                                     cartoon_book_kb,
                                     film_book_kb,
                                     popular_book_kb)
from keyboards.really_order import (really_order_bers,
                                    really_order_come,
                                    really_order_riders,
                                    really_order_home)

order_book_router = Router()


@order_book_router.message(Command('order_book'))
async def show_anime(message: types.Message):
    logging.info(message.from_user)
    await message.answer("Какую жанр книг вы хотите приобрести?", reply_markup=order_book_kb())


@order_book_router.callback_query(F.data == "Anime")
async def show_comedian(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите книгу:", reply_markup=anime_book_kb())


@order_book_router.callback_query(F.data == "Cartoons")
async def show_comedian(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите книгу:", reply_markup=cartoon_book_kb())


@order_book_router.callback_query(F.data == "Films")
async def show_horror(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите книгу:", reply_markup=film_book_kb())


@order_book_router.callback_query(F.data == "Popular_books")
async def show_fantastic(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите книгу:", reply_markup=popular_book_kb())


db = Database()


@order_book_router.callback_query(F.data == "Berserk")
async def berserk(callback: types.CallbackQuery):
    first_book = db.get_berserk()
    info = f"Название: {first_book[1]}\nОписание: {first_book[2]}\nЦена: {first_book[3]}"
    file_path = Path(__file__).parent.parent / "images" / first_book[4]
    file = types.FSInputFile(file_path)
    logging.info(file_path)
    await callback.message.answer_photo(file, caption=info, reply_markup=really_order_bers())


@order_book_router.callback_query(F.data == "urhome")
async def urhome(callback: types.CallbackQuery):
    first_book = db.get_urhome()
    info = f"Название: {first_book[1]}\nОписание: {first_book[2]}\nЦена: {first_book[3]}"
    file_path = Path(__file__).parent.parent / "images" / first_book[4]
    file = types.FSInputFile(file_path)
    logging.info(file_path)
    await callback.message.answer_photo(file, caption=info, reply_markup=really_order_home())


@order_book_router.callback_query(F.data == "riders")
async def riders(callback: types.CallbackQuery):
    first_book = db.get_riders()
    info = f"Название: {first_book[1]}\nОписание: {first_book[2]}\nЦена: {first_book[3]}"
    file_path = Path(__file__).parent.parent / first_book[4]
    file = types.FSInputFile(file_path)
    logging.info(file_path)
    await callback.message.answer_photo(file, caption=info, reply_markup=really_order_riders())


@order_book_router.callback_query(F.data == "comeget")
async def comeget(callback: types.CallbackQuery,):
    first_book = db.get_comeget()
    info = f"Название: {first_book[1]}\nОписание: {first_book[2]}\nЦена: {first_book[3]}"
    file_path = Path(__file__).parent.parent / "images" / first_book[4]
    file = types.FSInputFile(file_path)
    logging.info(file_path)
    await callback.message.answer_photo(file, caption=info, reply_markup=really_order_come())

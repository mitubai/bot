from aiogram import Router, F, types
from aiogram.filters import Command
from keyboards.cartoon_kb import (cartoon_kb, cartoon_kb2, cartoon_kb3, cartoon_kb4, cartoon_kb5, cartoon_kb6,)
import logging

cartoons_router = Router()

@cartoons_router.message(Command('cartoons'))
async def show_cartoons(message: types.Message):
    logging.info(message.from_user)
    await message.answer("Какой жанр мультфильмов вы хотите?", reply_markup=cartoon_kb())

@cartoons_router.callback_query(F.data == "Comedian_for_cartoon")
async def show_comedian(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите мультфильм:", reply_markup=cartoon_kb2())

@cartoons_router.callback_query(F.data == "Adventures_for_cartoon")
async def show_adventures(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите мультфильм:", reply_markup=cartoon_kb3())

@cartoons_router.callback_query(F.data == "Fantastic_for_cartoon")
async def show_fantastic(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите мультфильм:", reply_markup=cartoon_kb4())

@cartoons_router.callback_query(F.data == "ForKids")
async def show_for_kids(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите мультфильм:", reply_markup=cartoon_kb5())

@cartoons_router.callback_query(F.data == "Popular_for_cartoon")
async def show_populars(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите мультфильм:", reply_markup=cartoon_kb6())

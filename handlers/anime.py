from aiogram import Router, F, types
from aiogram.filters import Command
import logging
from keyboards.anime_kb import (
    anime_keyboard,
    anime_popular_kb,
    anime_comedy_kb,
    anime_thrillers_kb,
    anime_fantasy_kb,
    anime_horror_kb)


anime_router = Router()

@anime_router.message(Command('anime'))
async def show_anime(message: types.Message):
    logging.info(message.from_user)
    await message.answer("Какой жанр аниме вы хотите?", reply_markup=anime_keyboard())

@anime_router.callback_query(F.data == "Comedian_for_anime")
async def show_comedian(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите аниме:", reply_markup=anime_comedy_kb())

@anime_router.callback_query(F.data == "Horrors_for_anime")
async def show_horror(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите аниме:", reply_markup=anime_horror_kb())

@anime_router.callback_query(F.data == "Fantastic_for_anime")
async def show_fantastic(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите аниме:", reply_markup=anime_fantasy_kb())

@anime_router.callback_query(F.data == "Thrillers_for_anime")
async def show_thrillers(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите аниме:", reply_markup=anime_thrillers_kb())

@anime_router.callback_query(F.data == "Popular_for_2024")
async def show_populars(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите аниме:", reply_markup=anime_popular_kb())

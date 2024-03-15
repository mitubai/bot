from aiogram import Router, F, types
from aiogram.filters import Command
from keyboards.serials_kb import (serials_kb,serials_kb2,serials_kb3,serials_kb4,serials_kb5,serials_kb6)
import logging

serials_router = Router()

@serials_router.message(Command('serials'))
async def show_serials(message: types.Message):
    logging.info(message.from_user)
    await message.answer("Какой жанр сериалов вы хотите?", reply_markup=serials_kb())

@serials_router.callback_query(F.data == "Comedian_for_serials")
async def show_comedian(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите сериал:", reply_markup=serials_kb2())

@serials_router.callback_query(F.data == "Horrors_for_serials")
async def show_horror(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите сериал:", reply_markup=serials_kb3())

@serials_router.callback_query(F.data == "Fantastic_for_serials")
async def show_fantastic(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите сериал:", reply_markup=serials_kb4())

@serials_router.callback_query(F.data == "Thrillers_for_serials")
async def show_thrillers(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите сериал:", reply_markup=serials_kb5())

@serials_router.callback_query(F.data == "Popular_for_serials")
async def show_populars(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Выберите сериал:", reply_markup=serials_kb6())

from aiogram import Router, F, types
from aiogram.filters import Command
from keyboards.help_kb import (help_kb,help_kb1)
import logging

help_router = Router()


@help_router.message(Command("help"))
async def show_anime(message: types.Message):
    logging.info(message.from_user)
    await message.answer("Наша поддержка!", reply_markup=help_kb())


@help_router.callback_query(F.data == "about")
async def about(callback: types.CallbackQuery):
    await callback.message.answer("О нас:\n"
                                  "Мы компания которая старается помогать\n"
                                  "людам находить фильмы, сериалы, аниме, мультики")


@help_router.callback_query(F.data == "contacts")
async def about(callback: types.CallbackQuery):
    logging.info(callback.from_user)
    await callback.message.answer("Наши контакты:", reply_markup=help_kb1())

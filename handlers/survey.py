from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from keyboards.survey_kb import (survey_gender_kb,
                                 survey_genre_kb,
                                 survey_edu_kb)
import logging


class Survey(StatesGroup):
    name = State()
    age = State()
    gender = State()
    job_title = State()
    fav_genre = State()
    fav_book = State()
    fav_movie = State()
    education = State()
    fav_autor = State()
    book_to_read = State()
    movie_to_watch = State()
    back = State()


survey_router = Router()


@survey_router.message(Command("survey"))
async def start_survey(message: types.Message, state: FSMContext):
    await state.set_state(Survey.name)
    await message.answer("Как вас зовут?")


@survey_router.message(Survey.name)
async def survey(message: types.Message, state: FSMContext):
    name = message.text
    await state.set_state(Survey.age)
    await message.answer("Сколько вам лет?")

@survey_router.message(Survey.age)
async def survey(message: types.Message, state: FSMContext):
    age = message.text
    await state.set_state(Survey.gender)
    await message.answer("Какой ваш пол?", reply_markup=survey_gender_kb())


@survey_router.message(Survey.gender)
async def survey(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardRemove()
    gender = message.text
    await state.set_state(Survey.job_title)
    await message.answer("Какая у вас работа?", reply_markup=kb)


@survey_router.message(Survey.job_title)
async def survey(message: types.Message, state: FSMContext):
    job_title = message.text
    await state.set_state(Survey.fav_genre)
    await message.answer("Ваш любимый жанр?", reply_markup=survey_genre_kb())


@survey_router.message(Survey.fav_genre)
async def survey(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardRemove()
    fav_genre = message.text
    await state.set_state(Survey.fav_book)
    await message.answer("Ваша любимая книга?", reply_markup=kb)


@survey_router.message(Survey.fav_book)
async def survey(message: types.Message, state: FSMContext):
    fav_book = message.text
    await state.set_state(Survey.fav_movie)
    await message.answer("Ваш любимый фильм?")


@survey_router.message(Survey.fav_movie)
async def survey(message: types.Message, state: FSMContext):
    fav_movie = message.text
    await state.set_state(Survey.education)
    await message.answer("Какое обучение вы имеете?", reply_markup=survey_edu_kb())


@survey_router.message(Survey.education)
async def survey(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardRemove()
    education = message.text
    await state.set_state(Survey.fav_autor)
    await message.answer("Ваш любимый автор?", reply_markup=kb)


@survey_router.message(Survey.fav_autor)
async def survey(message: types.Message, state: FSMContext):
    fav_autor = message.text
    await state.set_state(Survey.book_to_read)
    await message.answer("Какую книгу вы посоветуете, начинающим?")


@survey_router.message(Survey.book_to_read)
async def survey(message: types.Message, state: FSMContext):
    book_to_read = message.text
    await state.set_state(Survey.movie_to_watch)
    await message.answer("Какой фильм вы посоветуете, другим?")


@survey_router.message(Survey.movie_to_watch)
async def survey(message: types.Message, state: FSMContext):
    movie_to_watch = message.text
    await state.set_state(Survey.back)
    await message.answer(f"Спасибо большое за пройденный опрос, вы можете перейти на такие сыллки как -\n"
                         "/films - фильмы\n"
                         "/cartoons - мультики\n"
                         "/anime - аниме\n"
                         "/serials - сериалы\n"
                         "/help - для жалобы либо для связи с нами\n"
                         "/survey - для прохождения опроса")

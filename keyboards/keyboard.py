from aiogram import types

def film_kb():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Ужасы", callback_data="Horrors_for_film")
            ],
            [
                types.InlineKeyboardButton(text="Фантастика", callback_data="Fantastic_for_film")
            ],
            [
                types.InlineKeyboardButton(text="Популярные за 2024-год", callback_data="Popular_for_film")
            ]
        ]
    )
    return kb


def film_kb3():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Прочь", callback_data="proch")
            ]
        ]
    )
    return kb

def film_kb4():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Гарри Поттер и философский камень",
                                           callback_data="potter")
            ]
        ]
    )
    return kb



def film_kb6():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Дюна: Часть вторая", callback_data="dune")
            ]
        ]
    )
    return kb


def proch():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Смотреть", url="https://kinogo.inc/films/208-proch-2017-hd-maintv1-v77.html")
            ]
        ]
    )
    return kb


def dune():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Смотреть", url="https://kinogo.film/films/12840-djuna-2-2023-smotret-onlajn-besplatno.html")
            ]
        ]
    )
    return kb


def potter():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Смотреть", url="https://kinogo.uk/948-garri-potter-i-filosofskij-kamen-2001.html")
            ]
        ]
    )
    return kb

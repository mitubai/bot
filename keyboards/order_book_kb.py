from aiogram import types


def order_book_kb():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Аниме", callback_data="Anime")
            ],
            [
                types.InlineKeyboardButton(text="Мультики", callback_data="Cartoons")
            ],
            [
                types.InlineKeyboardButton(text="Фильмы", callback_data="Films")
            ],
            [
                types.InlineKeyboardButton(text="Популярные за 2024-год", callback_data="Popular_books")
            ],
        ]
    )
    return kb


def anime_book_kb():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Berserk", callback_data="Berserk")
            ],
            [
                types.InlineKeyboardButton(text="Attack on titan", url="https://example.com/attack_on_titan")
            ],
            [
                types.InlineKeyboardButton(text="Naruto",
                                           url="https://example.com/naruto")
            ]
        ]
    )
    return kb


def cartoon_book_kb():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="You are home", callback_data="urhome")
            ],
            [
                types.InlineKeyboardButton(text="War and peas", url="https://example.com/war_peas")
            ],
            [
                types.InlineKeyboardButton(text="False knees",
                                           url="https://example.com/false_knees")
            ]
        ]
    )
    return kb


def film_book_kb():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Easy Riders", callback_data="riders")
            ],
            [
                types.InlineKeyboardButton(text="Adventures in the screen", url="https://example.com/another")
            ],
            [
                types.InlineKeyboardButton(text="The moon's ballon", url="https://example.com/parasyte")
            ]
        ]
    )
    return kb


def popular_book_kb():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Come and Get It", callback_data="comeget")
            ],
            [
                types.InlineKeyboardButton(text="The Fury", url="https://example.com/fury")
            ],
            [
                types.InlineKeyboardButton(text="The woman", url="https://example.com/woman")
            ]
        ]
    )
    return kb
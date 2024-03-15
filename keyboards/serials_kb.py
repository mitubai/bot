from aiogram import types

def serials_kb():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Комедии", callback_data="Comedian_for_serials")
            ],
            [
                types.InlineKeyboardButton(text="Ужасы", callback_data="Horrors_for_serials")
            ],
            [
                types.InlineKeyboardButton(text="Фантастика", callback_data="Fantastic_for_serials")
            ],
            [
                types.InlineKeyboardButton(text="Боевики", callback_data="Thrillers_for_serials")
            ],
            [
                types.InlineKeyboardButton(text="Популярные за 2024-год", callback_data="Popular_for_serials")
            ],
        ]
    )
    return kb

def serials_kb2():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Friends", url="https://example.com/friends")
            ],
            [
                types.InlineKeyboardButton(text="The Office", url="https://example.com/the_office")
            ],
            [
                types.InlineKeyboardButton(text="Brooklyn Nine-Nine", url="https://example.com/brooklyn_nine_nine")
            ]
        ]
    )
    return kb

def serials_kb3():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="American Horror Story",
                                           url="https://example.com/american_horror_story")
            ],
            [
                types.InlineKeyboardButton(text="The Haunting of Hill House",
                                           url="https://example.com/haunting_of_hill_house")
            ],
            [
                types.InlineKeyboardButton(text="Stranger Things", url="https://example.com/stranger_things")
            ]
        ]
    )
    return kb

def serials_kb4():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Game of Thrones", url="https://example.com/game_of_thrones")
            ],
            [
                types.InlineKeyboardButton(text="The Witcher", url="https://example.com/the_witcher")
            ],
            [
                types.InlineKeyboardButton(text="Doctor Who", url="https://example.com/doctor_who")
            ]
        ]
    )
    return kb

def serials_kb5():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Breaking Bad", url="https://example.com/breaking_bad")
            ],
            [
                types.InlineKeyboardButton(text="Money Heist", url="https://example.com/money_heist")
            ],
            [
                types.InlineKeyboardButton(text="Prison Break", url="https://example.com/prison_break")
            ]
        ]
    )
    return kb

def serials_kb6():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Stranger Things", url="https://example.com/stranger_things")
            ],
            [
                types.InlineKeyboardButton(text="The Mandalorian", url="https://example.com/the_mandalorian")
            ],
            [
                types.InlineKeyboardButton(text="Game of Thrones", url="https://example.com/game_of_thrones")
            ]
        ]
    )
    return kb
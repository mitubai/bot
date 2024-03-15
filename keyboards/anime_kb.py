from aiogram import types


def anime_keyboard():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Комедии", callback_data="Comedian_for_anime")
            ],
            [
                types.InlineKeyboardButton(text="Ужас", callback_data="Horrors_for_anime")
            ],
            [
                types.InlineKeyboardButton(text="Фантастика", callback_data="Fantastic_for_anime")
            ],
            [
                types.InlineKeyboardButton(text="Боевики", callback_data="Thrillers_for_anime")
            ],
            [
                types.InlineKeyboardButton(text="Популярные за 2024-год", callback_data="Popular_for_2024")
            ],
        ]
    )
    return kb

def anime_comedy_kb():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="One Punch Man", url="https://example.com/one_punch_man")
            ],
            [
                types.InlineKeyboardButton(text="Gintama", url="https://example.com/gintama")
            ],
            [
                types.InlineKeyboardButton(text="Daily Lives of High School Boys", url="https://example.com/daily_lives_of_high_school_boys")
            ]
        ]
    )
    return kb

def anime_horror_kb():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Tokyo Ghoul", url="https://example.com/tokyo_ghoul")
            ],
            [
                types.InlineKeyboardButton(text="Another", url="https://example.com/another")
            ],
            [
                types.InlineKeyboardButton(text="Parasyte", url="https://example.com/parasyte")
            ]
        ]
    )
    return kb

def anime_fantasy_kb():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Attack on Titan", url="https://example.com/attack_on_titan")
            ],
            [
                types.InlineKeyboardButton(text="Fullmetal Alchemist: Brotherhood", url="https://example.com/fullmetal_alchemist")
            ],
            [
                types.InlineKeyboardButton(text="Hunter x Hunter", url="https://example.com/hunter_x_hunter")
            ]
        ]
    )
    return kb

def anime_thrillers_kb():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Death Note", url="https://example.com/death_note")
            ],
            [
                types.InlineKeyboardButton(text="Psycho-Pass", url="https://example.com/psycho_pass")
            ],
            [
                types.InlineKeyboardButton(text="Steins;Gate", url="https://example.com/steins_gate")
            ]
        ]
    )
    return kb

def anime_popular_kb():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Demon Slayer: Kimetsu no Yaiba",
                                           url="https://example.com/demon_slayer")
            ],
            [
                types.InlineKeyboardButton(text="My Hero Academia", url="https://example.com/my_hero_academia")
            ],
            [
                types.InlineKeyboardButton(text="Naruto", url="https://example.com/naruto")
            ]
        ]
    )
    return kb
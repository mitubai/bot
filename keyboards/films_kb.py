from aiogram import types

def film_kb():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Комедии", callback_data="Comedian_for_film")
            ],
            [
                types.InlineKeyboardButton(text="Ужасы", callback_data="Horrors_for_film")
            ],
            [
                types.InlineKeyboardButton(text="Фантастика", callback_data="Fantastic_for_film")
            ],
            [
                types.InlineKeyboardButton(text="Боевики", callback_data="Thrillers_for_film")
            ],
            [
                types.InlineKeyboardButton(text="Популярные за 2024-год", callback_data="Popular_for_film")
            ]
        ]
    )
    return kb

def film_kb2():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наполеон: динамит", url="https://example.com/napoleon_dynamite")
            ],
            [
                types.InlineKeyboardButton(text="Оффисное пространство", url="https://example.com/office_space")
            ],
            [
                types.InlineKeyboardButton(text="Поездка в америку", url="https://example.com/trip_to_america")
            ]
        ]
    )
    return kb

def film_kb3():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Прочь", url="https://example.com/get_out")
            ],
            [
                types.InlineKeyboardButton(text="Сияние", url="https://example.com/the_shining")
            ],
            [
                types.InlineKeyboardButton(text="Реинкарнация", url="https://example.com/reincarnation")
            ]
        ]
    )
    return kb

def film_kb4():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Гарри Поттер и философский камень",
                                           url="https://example.com/harry_potter")
            ],
            [
                types.InlineKeyboardButton(text="Властелин колец: Братство кольца", url="https://example.com/lotr")
            ],
            [
                types.InlineKeyboardButton(text="Дева и дракон", url="https://example.com/dragonheart")
            ]
        ]
    )
    return kb

def film_kb5():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Безумный Макс: Дорога ярости",
                                           url="https://example.com/mad_max_fury_road")
            ],
            [
                types.InlineKeyboardButton(text="Бесславные ублюдки", url="https://example.com/inglourious_basterds")
            ],
            [
                types.InlineKeyboardButton(text="Kingsman: Секретная служба", url="https://example.com/kingsman")
            ]
        ]
    )
    return kb

def film_kb6():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Дюна: Часть вторая", url="https://example.com/dune_2")
            ],
            [
                types.InlineKeyboardButton(text="Каскадёры", url="https://example.com/cascaders")
            ],
            [
                types.InlineKeyboardButton(text="Фуриоса: Хроники Безумного Макса", url="https://example.com/furiosa")
            ]
        ]
    )
    return kb

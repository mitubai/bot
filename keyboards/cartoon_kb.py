from aiogram import types

def cartoon_kb():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Комедии", callback_data="Comedian_for_cartoon")
            ],
            [
                types.InlineKeyboardButton(text="Приключения", callback_data="Adventures_for_cartoon")
            ],
            [
                types.InlineKeyboardButton(text="Фантастика", callback_data="Fantastic_for_cartoon")
            ],
            [
                types.InlineKeyboardButton(text="Для детей", callback_data="ForKids")
            ],
            [
                types.InlineKeyboardButton(text="Популярные", callback_data="Popular_for_cartoon")
            ],
        ]
    )
    return kb

def cartoon_kb2():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Семейка Симпсонов", url="https://example.com/simpsons")
            ],
            [
                types.InlineKeyboardButton(text="Футурама", url="https://example.com/futurama")
            ],
            [
                types.InlineKeyboardButton(text="Гравити Фолз", url="https://example.com/gravity_falls")
            ]
        ]
    )
    return kb

def cartoon_kb3():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Рик и Морти", url="https://example.com/rick_and_morty")
            ],
            [
                types.InlineKeyboardButton(text="Аватар: Легенда об Аанге", url="https://example.com/avatar")
            ],
            [
                types.InlineKeyboardButton(text="Наруто", url="https://example.com/naruto")
            ]
        ]
    )
    return kb

def cartoon_kb4():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Аладдин", url="https://example.com/aladdin")
            ],
            [
                types.InlineKeyboardButton(text="Холодное сердце", url="https://example.com/frozen")
            ],
            [
                types.InlineKeyboardButton(text="Тачки", url="https://example.com/cars")
            ]
        ]
    )
    return kb

def cartoon_kb5():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Пингвины из Мадагаскара", url="https://example.com/penguins_of_madagascar")
            ],
            [
                types.InlineKeyboardButton(text="Шрек", url="https://example.com/shrek")
            ],
            [
                types.InlineKeyboardButton(text="Маша и Медведь", url="https://example.com/masha_and_the_bear")
            ]
        ]
    )
    return kb

def cartoon_kb6():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Семейка Крудс", url="https://example.com/the_croods")
            ],
            [
                types.InlineKeyboardButton(text="Как приручить дракона",
                                           url="https://example.com/how_to_train_your_dragon")
            ],
            [
                types.InlineKeyboardButton(text="История игрушек", url="https://example.com/toy_story")
            ]
        ]
    )
    return kb
from aiogram import types

def survey_gender_kb():
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Мужской"),
                types.KeyboardButton(text="Женский")
            ]
        ]
    )
    return kb


def survey_genre_kb():
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Комедии", callback_data="genre_comedy"),
                types.KeyboardButton(text="Хоррор", callback_data="genre_horror")
            ],
            [
                types.KeyboardButton(text="Боевики", callback_data="genre_action"),
                types.KeyboardButton(text="Фантастика", callback_data="genre_scifi")
            ],
            [
                types.KeyboardButton(text="Документальные", callback_data="genre_documentary")
            ]
        ]
    )
    return kb

def survey_edu_kb():
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Дошкольное", callback_data="edu_preschool"),
                types.KeyboardButton(text="Начальное общее", callback_data="edu_primary")
            ],
            [
                types.KeyboardButton(text="Основное общее", callback_data="edu_lower_secondary"),
                types.KeyboardButton(text="Среднее общее", callback_data="edu_upper_secondary")
            ],
            [
                types.KeyboardButton(text="Среднее профессиональное", callback_data="edu_vocational"),
                types.KeyboardButton(text="Высшее I степени", callback_data="edu_higher_i")
            ],
            [
                types.KeyboardButton(text="Высшее II степени", callback_data="edu_higher_ii"),
                types.KeyboardButton(text="Высшее III степени", callback_data="edu_higher_iii")
            ]
        ]
    )
    return kb

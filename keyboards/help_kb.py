from aiogram import types

def help_kb():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about")
            ],
            [
                types.InlineKeyboardButton(text="Контакты", callback_data="contacts")
            ]
        ]
    )
    return kb

def help_kb1():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Ватсапп", url="https://Wa.me/996755044489")
            ],
            [
                types.InlineKeyboardButton(text="Телеграмм", url="https://t.me/Timurskii_M"),
                types.InlineKeyboardButton(text="Жалоба", url="https://Wa.me")
            ]
        ]
    )
    return kb
from aiogram import types


def really_order_bers():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Купить", callback_data="Order_bers")
            ]
        ]
    )
    return kb


def really_order_home():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Купить", callback_data="Urhome")
            ]
        ]
    )
    return kb


def really_order_riders():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Купить", callback_data="esriders")
            ]
        ]
    )
    return kb


def really_order_come():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Купить", callback_data="come")
            ]
        ]
    )
    return kb


def confirm_order_kb():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Подтверждаю", callback_data="confirm"),
                types.InlineKeyboardButton(text="Отмена", callback_data="cancel")
            ],
        ]
    )
    return kb
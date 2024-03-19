from aiogram import Router, F, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup

from db.base import Database
from keyboards.really_order import confirm_order_kb


class Order(StatesGroup):
    full_name = State()
    address = State()
    phone_number = State()
    back = State()


real_order_router = Router()
db = Database()


@real_order_router.callback_query(F.data == "Order_bers")
@real_order_router.callback_query(F.data == "Urhome")
@real_order_router.callback_query(F.data == "esriders")
@real_order_router.callback_query(F.data == "come")
async def order(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Order.full_name)
    await callback.message.answer("ФИО, получателя:")


@real_order_router.message(Order.full_name)
async def order(message: types.Message, state: FSMContext):
    full_name = message.text
    await state.update_data(full_name=full_name)
    await state.set_state(Order.address)
    await message.delete()
    await message.answer("Аддрес, получателя:")


@real_order_router.message(Order.address)
async def order(message: types.Message, state: FSMContext):
    address = message.text
    await state.update_data(address=address)
    await state.set_state(Order.phone_number)
    await message.delete()
    await message.answer("Номер телефона, получателя:")


@real_order_router.message(Order.phone_number)
async def confirm_order(message: types.Message, state: FSMContext):
    data = await state.get_data()
    full_name = data.get('full_name')
    address = data.get('address')
    phone_number = message.text
    if not phone_number.isdigit() or len(phone_number) != 9:
        await message.answer("Введите в формате без 0 и 996 в начале\n"
                             "только номер телефона без бкув и пробелов.\n"
                             "Пример: 755044489")
        return
    await state.set_state(Order.back)
    await message.delete()
    await message.answer(f"Пожалуйста, проверьте свои данные и подтвердите ваш заказ\n"
                         f"Номер телефона: +996{phone_number}\n"
                         f"Аддрес: {address}\n"
                         f"ФИО: {full_name}", reply_markup=confirm_order_kb())


@real_order_router.callback_query(F.data == "confirm")
async def order(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Спасибо за заказ, мы свяжемся с вами в течении 30 минут.")


@real_order_router.callback_query(F.data == "cancel")
async def order(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Ваш заказ успешно отменен.")
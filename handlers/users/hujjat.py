import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.callBackData import local_callback
from loader import dp
from states.xujjatData import HujjatData


@dp.callback_query_handler(local_callback.filter(item_name="tolash"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Passport seriyangizni kiriting(AA0010101): ")
    await HujjatData.passport.set()

@dp.message_handler(state=HujjatData.passport)
async def next_full_name(message: types.Message, state: FSMContext):
    passport = message.text
    await state.update_data(
        {'passport': passport}
    )

    await message.answer("Karta raqamingizni kiriting:")
    await HujjatData.next()


@dp.message_handler(state=HujjatData.karta)
async def next_full_name(message: types.Message, state: FSMContext):
    karta = message.text
    await state.update_data(
        {'karta': karta}
    )

    await message.answer("Kartangizni muddatini kiriting(00/00):")
    await HujjatData.next()

@dp.message_handler(state=HujjatData.karta_date)
async def next_phone(message: types.Message, state: FSMContext):
    phone = message.text
    await state.update_data(
        {'karta_date': phone}
    )

    data = await state.get_data()
    name = data.get('passport')
    email = data.get('karta')
    phone = data.get('karta_date')

    msg = "Quyidagi ma'lumotlar saqlandi!\n"
    msg += f"Passportingiz: {name}\n"
    msg += f"Karta raqamingiz: {email}\n"
    msg += f"Karta muddati: {phone}"

    await message.answer(msg)

    await state.reset_state(with_data=False)
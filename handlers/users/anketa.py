from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Regexp
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.replayKeyboardMenu import menuStart
from keyboards.default.startKeyboardPhone import phoneButton
from loader import dp
from states.personalData import PersonData

EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
PHONE_REGEX = r'^[\+]?[(]?[0-9]{2,5}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{2,4}[-\s\.]?[0-9]{2,4}$'


@dp.message_handler(text_contains='Registratsiya')
async def enter_anketa(message: types.Message):
    await message.answer("To'liq ism familiyangizni kiriting:", reply_markup=ReplyKeyboardRemove())
    await PersonData.full_name.set()

@dp.message_handler(state=PersonData.full_name)
async def next_full_name(message: types.Message, state: FSMContext):
    full_name = message.text
    await state.update_data(
        {'name': full_name}
    )

    await message.answer("Emailingizni kiriting:")
    await PersonData.next()

@dp.message_handler(Regexp(EMAIL_REGEX), state=PersonData.email)
async def next_email(msg: types.Message, state: FSMContext):
    email = msg.text
    await state.update_data(
        {'email': email}
    )

    await msg.answer("Telefon raqamingizni kiriting:")
    await PersonData.next()

@dp.message_handler(state=PersonData.email)
async def else_next_email(message: types.Message):
    await message.answer("Noto'g'ri email kiritdingiz, qayta kiriting:")

@dp.message_handler(Regexp(PHONE_REGEX), state=PersonData.phone)
async def next_phone(message: types.Message, state: FSMContext):
    phone = message.text
    await state.update_data(
        {'phone': phone}
    )

    data = await state.get_data()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    msg = "Quyidagi ma'lumotlar saqlandi!\n"
    msg += f"To'liq Ismingiz: {name}\n"
    msg += f"Email manzilingiz: {email}\n"
    msg += f"Telefoningiz: {phone}"

    await message.answer(msg)

    await state.reset_state(with_data=False)
    await message.answer("Botimizdan foydalanishingiz mumkin", reply_markup=menuStart)

@dp.message_handler(state=PersonData.phone)
async def else_next_phone(message: types.Message):
    await message.answer("Noto'g'ri telefon kiritdingiz, qayta kiriting:")
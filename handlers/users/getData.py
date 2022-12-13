from aiogram import types

from loader import dp
from aiogram.dispatcher import FSMContext
from states.personalData import PersonData


@dp.message_handler(commands='profile')
async def send_profile(message: types.Message, state: FSMContext):
    await PersonData.phone.set()

    data = await state.get_data()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    msg = "Sizning ma'lumotlaringiz!\n"
    msg += f"To'liq Ismingiz: {name}\n"
    msg += f"Email manzilingiz: {email}\n"
    msg += f"Telefoningiz: {phone}"

    await message.answer(msg)
    await state.reset_state(with_data=False)
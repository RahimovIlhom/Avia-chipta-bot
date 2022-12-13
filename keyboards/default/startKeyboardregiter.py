from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

registerButton = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Registratsiya'),
        ],
    ],
    resize_keyboard=True,
)
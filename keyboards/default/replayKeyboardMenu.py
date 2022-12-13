from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✈ Aviachiptalar'),
            KeyboardButton(text='🗒 Qo\'llanma'),
            KeyboardButton(text='⚙ Sozlamalar'),
        ],
    ],
    resize_keyboard=True,
)
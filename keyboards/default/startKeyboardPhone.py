from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phoneButton = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📞 Contact', request_contact=True),
        ],
    ],
    resize_keyboard=True,
)
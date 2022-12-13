from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callBackData import global_callback

manzillar = {
    "Toshkent": "Tashkent",
    "London": "London",
    "Washington": "Washington",
    "Istanbul": "Istanbul",
    "Tokio": "Tokio",
    "Moskva": "Moskow",
}

#manzil inline keyboard
globalChiptaKetmoqMenu = InlineKeyboardMarkup(row_width=2)
globalChiptaManzilMenu = InlineKeyboardMarkup(row_width=2)

for key, value in manzillar.items():
    globalChiptaKetmoqMenu.insert(InlineKeyboardButton(text=key, callback_data=global_callback.new(value+"_k")))
    globalChiptaManzilMenu.insert(InlineKeyboardButton(text=key, callback_data=global_callback.new(value)))

back = InlineKeyboardButton(text="🔙 Orqaga", callback_data='g_cancel')
back_k = InlineKeyboardButton(text="🔙 Orqaga", callback_data='g_cancel_k')
globalChiptaKetmoqMenu.insert(back_k)
globalChiptaManzilMenu.insert(back)
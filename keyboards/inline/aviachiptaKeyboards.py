from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callBackData import local_callback, global_callback

aviaChiptaMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mahalliy", callback_data='local'),
            InlineKeyboardButton(text="Xalqaro", callback_data='global'),
        ],
        [
            InlineKeyboardButton(text="🔗 Saytimiz orqali buyurtma", url='https://www.uzairways.com/'),
        ],
        [
            InlineKeyboardButton(text="✉ Ulashish", switch_inline_query="Botga qo'shiling"),
        ],
    ], row_width=1
)

manzillar = {
    "Toshkent": "Tashkent",
    "Farg'ona": "Fergana",
    "Andijon": "Andijan",
    "Namangan": "Namangan",
    "Buxoro": "Bukhara",
    "Navoiy": "Navoiy",
    "Surxondaryo": "Surxondaryo",
    "Qashqadaryo": "Qashqadaryo",
    "Sirdaryo": "Sirdaryo",
    "Qoraqalpog'iston": "Qoraqalpoq",
}

#manzil inline keyboard
localChiptaKetmoqMenu = InlineKeyboardMarkup(row_width=2)
localChiptaManzilMenu = InlineKeyboardMarkup(row_width=2)

for key, value in manzillar.items():
    localChiptaKetmoqMenu.insert(InlineKeyboardButton(text=key, callback_data=local_callback.new(value+"_k")))
    localChiptaManzilMenu.insert(InlineKeyboardButton(text=key, callback_data=local_callback.new(value)))

back = InlineKeyboardButton(text="🔙 Orqaga", callback_data='cancel')
back_k = InlineKeyboardButton(text="🔙 Orqaga", callback_data='cancel_k')
localChiptaKetmoqMenu.insert(back_k)
localChiptaManzilMenu.insert(back)

months = {
    "Yanvar": "january",
    "Fevral": "february",
    "Mart": "march",
    "Aprel": "april",
    "May": "may",
    "Iyun": "june",
    "Iyul": "july",
    "Avgust": "august",
    "Sentabr": "september",
    "Oktabr": "october",
    "Noyabr": "november",
    "Dekabr": "december",
}

#Oy inline keyboard
localChiptaMonthMenu = InlineKeyboardMarkup(row_width=2)
back_month = InlineKeyboardButton(text="🔙 Orqaga", callback_data='cancel_oy')
for key, value in months.items():
    localChiptaMonthMenu.insert(InlineKeyboardButton(text=key, callback_data=local_callback.new(value)))
localChiptaMonthMenu.insert(back_month)

#Kun inline keyboard
localChiptaKunMenu = InlineKeyboardMarkup(row_width=5)
back_day = InlineKeyboardButton(text="🔙 Orqaga", callback_data='cancel_kun')
for i in range(1, 32):
    localChiptaKunMenu.insert(InlineKeyboardButton(text=str(i), callback_data=local_callback.new(str(i))))
localChiptaKunMenu.insert(back_day)

#Chiptalar ro'yxati
localChiptamenu = InlineKeyboardMarkup(row_width=1)
back_airways = InlineKeyboardButton(text="🔙 Orqaga", callback_data='cancel_air')
localChiptamenu.insert(InlineKeyboardButton(text="Uchish vaqti: 9:45. Narxi: 1000000", callback_data=local_callback.new("airways1")))
localChiptamenu.insert(InlineKeyboardButton(text="Uchish vaqti: 12:45. Narxi: 1100000", callback_data=local_callback.new("airways2")))
localChiptamenu.insert(InlineKeyboardButton(text="Uchish vaqti: 19:45. Narxi: 900000", callback_data=local_callback.new("airways3")))
localChiptamenu.insert(back_airways)

localYolovchiMenu = InlineKeyboardMarkup(row_width=3)
back_yolovchi = InlineKeyboardButton(text="🔙 Orqaga", callback_data='cancel_yol')
for i in range(1, 10):
    localYolovchiMenu.insert(InlineKeyboardButton(text=str(i), callback_data=local_callback.new(str(i)+"ta")))
localYolovchiMenu.insert(back_yolovchi)

localYolovchiBolaMenu = InlineKeyboardMarkup(row_width=3)
back_bola = InlineKeyboardButton(text="🔙 Orqaga", callback_data='cancel_bola')
for i in range(0, 9):
    localYolovchiBolaMenu.insert(InlineKeyboardButton(text=str(i), callback_data=local_callback.new(str(i)+"ta_b")))
localYolovchiBolaMenu.insert(back_bola)

paymentMenu = InlineKeyboardMarkup(row_width=1)
back_pay = InlineKeyboardButton(text="🔙 Orqaga", callback_data='cancel_pay')
paymentMenu.insert(InlineKeyboardButton(text="Uzcard", callback_data=local_callback.new("uzcard")))
paymentMenu.insert(InlineKeyboardButton(text="Humo", callback_data=local_callback.new("humo")))
paymentMenu.insert(InlineKeyboardButton(text="Visa", callback_data=local_callback.new("visa")))
paymentMenu.insert(back_pay)

tolashMenu = InlineKeyboardMarkup()
back_tol = InlineKeyboardButton(text="🔙 Orqaga", callback_data='cancel_tol')
tolashMenu.insert(InlineKeyboardButton(text="To'lash", callback_data=local_callback.new("tolash")))
tolashMenu.insert(back_tol)
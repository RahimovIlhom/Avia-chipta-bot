import logging

from aiogram import types
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from keyboards.inline.callBackData import local_callback
from keyboards.inline.aviachiptaKeyboards import aviaChiptaMenu, localChiptaManzilMenu, localChiptaKetmoqMenu, \
    localChiptaMonthMenu, localChiptaKunMenu, localChiptamenu, localYolovchiMenu, localYolovchiBolaMenu, paymentMenu, \
    tolashMenu
from loader import dp

from keyboards.inline.aviachiptaKeyboards import manzillar


@dp.message_handler(text_contains='Aviachiptalar')
async def select_category(message: types.Message):
    await message.answer("Kategoriyani tanlang:", reply_markup=aviaChiptaMenu)

@dp.message_handler(text_contains='Qo\'llanma')
async def select_category(message: types.Message):
    await message.answer("Qo'llanma")

@dp.message_handler(text_contains='Sozlamalar')
async def select_category(message: types.Message):
    await message.answer("Sozlamalar")

@dp.callback_query_handler(text='local')
async def send_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    await call.message.answer("Qayerdan ketmoqchisiz?", reply_markup=localChiptaKetmoqMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='cancel_k')
async def back_to_category(call: CallbackQuery):
    await call.message.edit_text("Kategoriyani tanlang:")
    await call.message.edit_reply_markup(reply_markup=aviaChiptaMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name='Tashkent_k'))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qayerga bormoqchisiz?", reply_markup=localChiptaManzilMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name='Fergana_k'))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qayerga bormoqchisiz?", reply_markup=localChiptaManzilMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name='Andijan_k'))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qayerga bormoqchisiz?", reply_markup=localChiptaManzilMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="Namangan_k"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qayerga bormoqchisiz?", reply_markup=localChiptaManzilMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="Bukhara_k"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qayerga bormoqchisiz?", reply_markup=localChiptaManzilMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="Navoiy_k"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qayerga bormoqchisiz?", reply_markup=localChiptaManzilMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="Surxondaryo_k"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qayerga bormoqchisiz?", reply_markup=localChiptaManzilMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="Qashqadaryo_k"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qayerga bormoqchisiz?", reply_markup=localChiptaManzilMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="Sirdaryo_k"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qayerga bormoqchisiz?", reply_markup=localChiptaManzilMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="Qoraqalpoq_k"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qayerga bormoqchisiz?", reply_markup=localChiptaManzilMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='cancel')
async def back_to_category(call: CallbackQuery):
    await call.message.edit_text("Qayerdan ketmoqchisiz?")
    await call.message.edit_reply_markup(reply_markup=localChiptaKetmoqMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(local_callback.filter(item_name='Tashkent'))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi oy uchmoqchisiz?", reply_markup=localChiptaMonthMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(local_callback.filter(item_name='Fergana'))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi oy uchmoqchisiz?", reply_markup=localChiptaMonthMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(local_callback.filter(item_name='Andijan'))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi oy uchmoqchisiz?", reply_markup=localChiptaMonthMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(local_callback.filter(item_name="Namangan"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi oy uchmoqchisiz?", reply_markup=localChiptaMonthMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(local_callback.filter(item_name="Bukhara"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi oy uchmoqchisiz?", reply_markup=localChiptaMonthMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(local_callback.filter(item_name="Navoiy"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi oy uchmoqchisiz?", reply_markup=localChiptaMonthMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(local_callback.filter(item_name="Surxondaryo"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi oy uchmoqchisiz?", reply_markup=localChiptaMonthMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(local_callback.filter(item_name="Qashqadaryo"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi oy uchmoqchisiz?", reply_markup=localChiptaMonthMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(local_callback.filter(item_name="Sirdaryo"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi oy uchmoqchisiz?", reply_markup=localChiptaMonthMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(local_callback.filter(item_name="Qoraqalpoq"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi oy uchmoqchisiz?", reply_markup=localChiptaMonthMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='cancel_oy')
async def back_to_category(call: CallbackQuery):
    await call.message.edit_text("Qayerga bormoqchisiz?")
    await call.message.edit_reply_markup(reply_markup=localChiptaManzilMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="january"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi kun uchmoqchisiz?", reply_markup=localChiptaKunMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="february"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi kun uchmoqchisiz?", reply_markup=localChiptaKunMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="march"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi kun uchmoqchisiz?", reply_markup=localChiptaKunMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="april"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi kun uchmoqchisiz?", reply_markup=localChiptaKunMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="may"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi kun uchmoqchisiz?", reply_markup=localChiptaKunMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="june"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi kun uchmoqchisiz?", reply_markup=localChiptaKunMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="july"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi kun uchmoqchisiz?", reply_markup=localChiptaKunMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="august"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi kun uchmoqchisiz?", reply_markup=localChiptaKunMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="september"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi kun uchmoqchisiz?", reply_markup=localChiptaKunMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="october"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi kun uchmoqchisiz?", reply_markup=localChiptaKunMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="november"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi kun uchmoqchisiz?", reply_markup=localChiptaKunMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="december"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Qaysi kun uchmoqchisiz?", reply_markup=localChiptaKunMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='cancel_kun')
async def back_to_category(call: CallbackQuery):
    await call.message.edit_text("Qaysi oy uchmoqchisiz?")
    await call.message.edit_reply_markup(reply_markup=localChiptaMonthMenu)
    await call.answer(cache_time=60)

for i in range(1, 32):
    @dp.callback_query_handler(local_callback.filter(item_name=str(i)))
    async def buying_course(call: CallbackQuery, callback_data: dict):
        # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
        logging.info(f"{callback_data=}")
        await call.message.delete()
        await call.message.answer(f"Sotib olish. Bu kundagi chiptalar:\n", reply_markup=localChiptamenu)
        await call.answer(cache_time=60)

@dp.callback_query_handler(text='cancel_air')
async def back_to_category(call: CallbackQuery):
    await call.message.edit_text("Qaysi kun uchmoqchisiz?")
    await call.message.edit_reply_markup(reply_markup=localChiptaKunMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="airways1"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Kattalar uchun nechta chipta sotib olmoqchisiz?", reply_markup=localYolovchiMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="airways2"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Kattalar uchun nechta chipta sotib olmoqchisiz?", reply_markup=localYolovchiMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="airways3"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"Kattalar uchun nechta chipta sotib olmoqchisiz?", reply_markup=localYolovchiMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='cancel_yol')
async def back_to_category(call: CallbackQuery):
    await call.message.edit_text(f"Sotib olish. Bu kundagi chiptalar:")
    await call.message.edit_reply_markup(reply_markup=localChiptaKunMenu)
    await call.answer(cache_time=60)

for i in range(1, 10):
    @dp.callback_query_handler(local_callback.filter(item_name=str(i)+"ta"))
    async def buying_course(call: CallbackQuery, callback_data: dict):
        # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
        logging.info(f"{callback_data=}")
        await call.message.delete()
        await call.message.answer(f"Bolalar uchun nechta chipta sotib olmoqchisiz?", reply_markup=localYolovchiBolaMenu)

@dp.callback_query_handler(text='cancel_bola')
async def back_to_category(call: CallbackQuery):
    await call.message.edit_text(f"Kattalar uchun nechta chipta sotib olmoqchisiz?")
    await call.message.edit_reply_markup(reply_markup=localYolovchiMenu)
    await call.answer(cache_time=60)

for i in range(0, 9):
    @dp.callback_query_handler(local_callback.filter(item_name=str(i)+"ta_b"))
    async def buying_course(call: CallbackQuery, callback_data: dict):
        # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
        logging.info(f"{callback_data=}")
        await call.message.delete()
        await call.message.answer(f"Umumiy summa: 2000000\nTo'lovni amalga oshirish: karta turini tanlang!", reply_markup=paymentMenu)

@dp.callback_query_handler(text='cancel_pay')
async def back_to_category(call: CallbackQuery):
    await call.message.edit_text(f"Bolalar uchun nechta chipta sotib olmoqchisiz?")
    await call.message.edit_reply_markup(reply_markup=localYolovchiBolaMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="uzcard"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"To'lovni amalga oshirish:", reply_markup=tolashMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="humo"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"To'lovni amalga oshirish:", reply_markup=tolashMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(local_callback.filter(item_name="visa"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer(f"To'lovni amalga oshirish:", reply_markup=tolashMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='cancel_tol')
async def back_to_category(call: CallbackQuery):
    await call.message.edit_text("Umumiy summa: 2000000\nTo'lovni amalga oshirish: karta turini tanlang!")
    await call.message.edit_reply_markup(reply_markup=paymentMenu)
    await call.answer(cache_time=60)
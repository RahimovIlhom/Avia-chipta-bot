import logging

from aiogram import types
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from keyboards.inline.callBackData import global_callback
from keyboards.inline.glocalChiptaKeyboards import globalChiptaKetmoqMenu, manzillar, globalChiptaManzilMenu
from loader import dp

from keyboards.inline.aviachiptaKeyboards import aviaChiptaMenu, localChiptaMonthMenu


@dp.callback_query_handler(text='global')
async def send_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    await call.message.answer("Qayerdan ketmoqchisiz?", reply_markup=globalChiptaKetmoqMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='g_cancel_k')
async def back_to_category(call: CallbackQuery):
    await call.message.edit_text("Kategoriyani tanlang:")
    await call.message.edit_reply_markup(reply_markup=aviaChiptaMenu)
    await call.answer(cache_time=60)

for value in manzillar.values():
    @dp.callback_query_handler(global_callback.filter(item_name=value+"_k"))
    async def buying_course(call: CallbackQuery, callback_data: dict):
        # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
        logging.info(f"{callback_data=}")
        await call.message.delete()
        await call.message.answer(f"Qayerga bormoqchisiz?", reply_markup=globalChiptaManzilMenu)
        await call.answer(cache_time=60)

@dp.callback_query_handler(text='g_cancel')
async def back_to_category(call: CallbackQuery):
    await call.message.edit_text("Qayerdan ketmoqchisiz?")
    await call.message.edit_reply_markup(reply_markup=globalChiptaKetmoqMenu)
    await call.answer(cache_time=60)

for value in manzillar.values():
    @dp.callback_query_handler(global_callback.filter(item_name=value))
    async def buying_course(call: CallbackQuery, callback_data: dict):
        # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
        logging.info(f"{callback_data=}")
        await call.message.delete()
        await call.message.answer(f"Qaysi oy uchmoqchisiz?", reply_markup=localChiptaMonthMenu)
        await call.answer(cache_time=60)
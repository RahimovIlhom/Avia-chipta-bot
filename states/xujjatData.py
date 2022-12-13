from aiogram.dispatcher.filters.state import StatesGroup, State

class HujjatData(StatesGroup):
    passport = State()
    karta = State()
    karta_date = State()

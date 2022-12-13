from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonData(StatesGroup):
    full_name = State()
    email = State()
    phone = State()

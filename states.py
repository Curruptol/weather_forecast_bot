from aiogram.fsm.state import StatesGroup, State


class Periods(StatesGroup):
    menu = State()
    weather_period = State()
    current_day = State()
    incorrect_city = State()
    weather_sent = State()

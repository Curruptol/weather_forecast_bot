from aiogram.fsm.state import StatesGroup, State


class Periods(StatesGroup):
    menu = State()
    weather_period = State()
    current_day = State()
    incorrect_city = State()
    weather_sent = State()
    tomorrow = State()
    incorrect_city_for_tomorrow = State()
    three_days = State()
    incorrect_city_for_3_days = State()

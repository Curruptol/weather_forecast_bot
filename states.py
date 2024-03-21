from aiogram.fsm.state import StatesGroup, State


class Periods(StatesGroup):
    weather_period = State()
    current_day = State()

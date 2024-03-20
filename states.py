from aiogram.fsm.state import StatesGroup, State


class Periods(StatesGroup):
    current_day = State()

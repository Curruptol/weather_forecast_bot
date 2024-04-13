from aiogram.fsm.state import StatesGroup, State


class Periods(StatesGroup):
    menu = State()  # главное меню
    weather_period = State()  # выбор пероида погоды
    current_day = State()  # выбрана погода на сегодня
    incorrect_city = State()  # неверно указан город на сегодня
    weather_sent = State()  # погода отправлена
    tomorrow = State()  # выбрана погода на завтра
    incorrect_city_for_tomorrow = State()  # неверно указан город на завтра
    three_days = State()  # выбрана погода за три дня
    incorrect_city_for_3_days = State()  # неверное указан город на три дня

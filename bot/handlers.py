from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram import flags
from aiogram.fsm.context import FSMContext
import keyboards as kb
import get_weather
from states import Periods
import asyncio
import get_weather_forecast

router = Router()


@router.message(Command("start"))
async def start(msg: Message, state: FSMContext) -> object:
    await state.set_state(Periods.menu)
    await msg.answer(f"Привет, {msg.from_user.first_name}!👋🏻\n"
                     f"👀Выбери что ты хочешь:", reply_markup=kb.menu)


@router.message(Periods.menu)
@router.callback_query(F.data == "weather")
async def choose_weather_period(callback: CallbackQuery, state: FSMContext) -> object:
    await state.set_state(Periods.weather_period)
    await callback.message.edit_text(f"📅За какой период?", reply_markup=kb.weather_period)


@router.message(Periods.weather_period)
@router.callback_query(F.data == "today")
async def input_city(callback: CallbackQuery, state: FSMContext) -> object:
    await state.set_state(Periods.current_day)
    await callback.message.edit_text(f"⬇️Напиши город:")


@router.message(Periods.weather_period)
@router.callback_query(F.data == "tomorrow")
async def input_city_for_tomorrow(callback: CallbackQuery, state: FSMContext) -> object:
    await state.set_state(Periods.tomorrow)
    await callback.message.edit_text(f"⬇️Напиши город:")


@router.message(Periods.weather_period)
@router.callback_query(F.data == "3_days")
async def input_city_for_3_days(callback: CallbackQuery, state: FSMContext) -> object:
    await state.set_state(Periods.three_days)
    await callback.message.edit_text(f"⬇️Напиши город:")


@router.message(Periods.weather_period)
@router.callback_query(F.data == "back_to_menu")
async def back_from_weather_period(callback: CallbackQuery, state: FSMContext) -> object:
    await state.set_state(Periods.menu)
    await callback.message.edit_text(f"📍Главное меню", reply_markup=kb.menu)


@router.message(Periods.three_days)
@flags.chat_action("typing")
async def send_weather_3_days(msg: Message, state: FSMContext) -> object:
    ans = get_weather_forecast.get_weather_forecast(msg.text, 3)
    msg_wait = await msg.answer(f"⏳Пожалуйста, подожди немного, сейчас я отправлю тебе погоду...")
    await asyncio.sleep(1.5)
    if ans is None:
        await state.set_state(Periods.incorrect_city_for_3_days)
        await msg_wait.edit_text(f"❗️Неверный город❗️", reply_markup=kb.try_again)
    else:
        await state.set_state(Periods.weather_sent)
        await msg_wait.edit_text(ans, reply_markup=kb.exit_to_menu)


@router.message(Periods.tomorrow)
@flags.chat_action("typing")
async def send_weather_tomorrow(msg: Message, state: FSMContext) -> object:
    ans = get_weather_forecast.get_weather_forecast(msg.text, 2)
    msg_wait = await msg.answer(f"⏳Пожалуйста, подожди немного, сейчас я отправлю тебе погоду...")
    await asyncio.sleep(1.5)
    if ans is None:
        await state.set_state(Periods.incorrect_city_for_tomorrow)
        await msg_wait.edit_text(f"❗️Неверный город❗️", reply_markup=kb.try_again)
    else:
        await state.set_state(Periods.weather_sent)
        await msg_wait.edit_text(ans, reply_markup=kb.exit_to_menu)


@router.message(Periods.current_day)
@flags.chat_action("typing")
async def send_weather_today(msg: Message, state: FSMContext) -> object:
    ans = get_weather.get_current_weather(msg.text)
    msg_wait = await msg.answer(f"⏳Пожалуйста, подожди немного, сейчас я отправлю тебе погоду...")
    await asyncio.sleep(1.5)
    if ans is None:
        await state.set_state(Periods.incorrect_city)
        await msg_wait.edit_text(f"❗️Неверный город❗️", reply_markup=kb.try_again)
    else:
        await state.set_state(Periods.weather_sent)
        await msg_wait.edit_text(ans, reply_markup=kb.exit_to_menu)


@router.message(Periods.weather_sent)
@router.callback_query(F.data == "menu")
async def back_to_menu(callback: CallbackQuery, state: FSMContext) -> object:
    await state.set_state(Periods.menu)
    await callback.message.answer(f"📍Главное меню", reply_markup=kb.menu)


@router.message(Periods)
@router.callback_query(F.data == "try_again")
async def try_again(callback: CallbackQuery, state: FSMContext) -> object:
    current_state = await state.get_state()
    if current_state == Periods.incorrect_city:
        await input_city(callback, state)
    elif current_state == Periods.incorrect_city_for_tomorrow:
        await input_city_for_tomorrow(callback, state)
    elif current_state == Periods.incorrect_city_for_3_days:
        await input_city_for_3_days(callback, state)

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram import flags
from aiogram.fsm.context import FSMContext
import keyboards as kb
import weather
from states import Periods
import asyncio

router = Router()


@router.message(Command("start"))
async def start(msg: Message):
    await msg.answer(f"Привет, {msg.from_user.first_name}!👋🏻\n"
                     f"👀Выбери что ты хочешь:", reply_markup=kb.menu)


@router.callback_query(F.data == "weather")
async def choose_weather_period(callback: CallbackQuery, state: FSMContext):
    # await state.set_state(Periods.weather_period)
    await callback.message.answer(f"📅За какой период?", reply_markup=kb.weather_period)


# @router.message(Periods.weather_period)
@router.callback_query(F.data == "today")
async def input_city(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Periods.current_day)
    await callback.message.edit_text(f"⬇️Напиши город:")


@router.message(Periods.current_day)
@flags.chat_action("typing")
async def send_weather_today(msg: Message):
    ans = weather.get_weather(msg.text)
    msg_wait = await msg.answer(f"⏳Пожалуйста, подожди немного, сейчас я отправлю тебе погоду...")
    await asyncio.sleep(1.5)
    await msg_wait.edit_text(ans, reply_markup=kb.exit_to_menu)


@router.message(Periods.current_day)
@router.callback_query(F.data == "menu")
async def back_to_menu(callback: CallbackQuery):
    await callback.message.answer(f"📍Главное меню", reply_markup=kb.menu)
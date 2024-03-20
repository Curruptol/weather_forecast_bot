from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram import flags
from aiogram.fsm.context import FSMContext
import keyboards as kb

import weather
from states import Periods

router = Router()


@router.message(Command("start"))
async def start(msg: Message):
    # print(f"{dt.now()}. {msg.from_user.username}: {msg.text}")
    await msg.answer(f"Привет, {msg.from_user.first_name}!\n"
                     f"Выбери что ты хочешь:", reply_markup=kb.menu)
    # print(f"{dt.now()}. Bot: {ans_1.text}")
    # print(f"{dt.now()}. Bot: {ans_2.text}")


@router.callback_query(F.data == "weather")
async def choose_weather_period(callback: CallbackQuery):
    await callback.message.answer(f"За какой период?", reply_markup=kb.weather_period)


@router.callback_query(F.data == "today")
async def input_city(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Periods.current_day)
    await callback.message.edit_text(f"Напиши город:")


@router.message(Periods.current_day)
@flags.chat_action("typing")
async def send_weather_today(msg: Message, state: FSMContext):
    ans = weather.get_weather(msg.text)
    msg_wait = await msg.answer(f"Пожалуйста, подожди немного, сейчас я отправлю тебе погоду...")
    await msg_wait.edit_text(ans)

from aiogram.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup,
                           KeyboardButton,
                           ReplyKeyboardMarkup,
                           ReplyKeyboardRemove
                           )


menu = [
        [
         InlineKeyboardButton(text="Узнать погоду", callback_data="weather")
        ]
       ]


weather_period = [
                 [
                  InlineKeyboardButton(text="Сегодня", callback_data="today"),
                  InlineKeyboardButton(text="За 3 дня", callback_data="3_days")
                 ]
                ]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
weather_period = InlineKeyboardMarkup(inline_keyboard=weather_period)

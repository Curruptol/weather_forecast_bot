from aiogram.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup,
                           KeyboardButton,
                           ReplyKeyboardMarkup,
                           ReplyKeyboardRemove
                           )

menu = [[InlineKeyboardButton(text="🌡️Узнать погоду", callback_data="weather")]]

weather_period = [[InlineKeyboardButton(text="Сегодня", callback_data="today"),
                   InlineKeyboardButton(text="Завтра", callback_data="tomorrow"),
                   InlineKeyboardButton(text="За 3 дня", callback_data="3_days"), ],
                  [InlineKeyboardButton(text="◀️Назад", callback_data="back_to_menu")]]

exit_to_menu = [[InlineKeyboardButton(text="◀️В меню", callback_data="menu")]]

try_again = [[InlineKeyboardButton(text="↪️Попробовать снова", callback_data="try_again")]]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
weather_period = InlineKeyboardMarkup(inline_keyboard=weather_period)
exit_to_menu = InlineKeyboardMarkup(inline_keyboard=exit_to_menu)
try_again = InlineKeyboardMarkup(inline_keyboard=try_again)

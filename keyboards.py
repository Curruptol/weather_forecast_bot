from aiogram.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup,
                           KeyboardButton,
                           ReplyKeyboardMarkup,
                           ReplyKeyboardRemove
                           )


menu = [[InlineKeyboardButton(text="🌡️Узнать погоду", callback_data="weather")]]

weather_period = [[InlineKeyboardButton(text="Сегодня", callback_data="today"),
                   InlineKeyboardButton(text="За 3 дня", callback_data="3_days")]]

exit_to_menu = [[InlineKeyboardButton(text="◀️В меню", callback_data="menu")]]

try_again = [[InlineKeyboardButton(text="↪️Попробовать снова", callback_data="try_again")]]

# back_to_menu = InlineKeyboardMarkup(inline_keyboard=[
#                                                      [
#                                                       InlineKeyboardButton(text="◀️В меню", callback_data="menu")
#                                                      ]
#                                                     ]
#                                    )
#
# back = ReplyKeyboardMarkup(keyboard=[
#                                      [
#                                       KeyboardButton(text="◀️Назад")
#                                      ]
#                                     ], resize_keyboard=True
#                           )

menu = InlineKeyboardMarkup(inline_keyboard=menu)
weather_period = InlineKeyboardMarkup(inline_keyboard=weather_period)
exit_to_menu = InlineKeyboardMarkup(inline_keyboard=exit_to_menu)
try_again = InlineKeyboardMarkup(inline_keyboard=try_again)

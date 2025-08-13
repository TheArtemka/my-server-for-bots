from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


del_kbd = ReplyKeyboardRemove()


start_kb = ReplyKeyboardBuilder()
start_kb.add(
    KeyboardButton(text="Услуги💇‍♀️"),
    KeyboardButton(text="О Заведении🏙"),
    KeyboardButton(text="Уходы💆🏼‍♀️"),
    KeyboardButton(text="Запись📝"),
    KeyboardButton(text="(FAQ) Вопросы⁉️"),
    KeyboardButton(text="Об Ольгине👩🏻"),
)
start_kb.adjust(2, 2, 2)




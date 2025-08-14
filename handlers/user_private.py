from aiogram import  F, types, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import (
    as_list,
    as_marked_section,
    Bold,
    )
from aiogram.filters import Command


from aiogram.types import FSInputFile

from aiogram import Bot, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import asyncio

from filteres.chat_types import ChatTypeFilter

from keybds import reply

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        "Привет, я виртуальный помощник Ольгини, чем могу помочь?",
        reply_markup=reply.start_kb.as_markup(
        resize_keyboard=True,
                          )
                    )
    


@user_private_router.message(or_f(Command("menu"), (F.text.lower() == "услуги💇‍♀️")))
async def menu_cmd(message: types.Message):
    text = (
        "<b>Услуги💇‍♀️:</b>\n"
        "<b><u>Прайс</u></b>:\n"
        "  \n"
        "<b>✂️Стрижка:</b>\n"
        "  • Короткие волосы - 4.000₽\n"
        "  • Средние волосы - 5.000₽\n"
        "  • Длинные волосы - 6.000₽\n"
        "                                -\n"
        "<b>🧑🏼‍🎤Окрашивание в один тон\n"
        "(Vegan краситель Thermal, гипоаллергенно.):</b>\n"
        "  • Короткие волосы - 10.000₽\n"
        "  • Средние волосы - 12.000₽\n"
        "  • Длинные волосы - 15.000₽\n"
        "                                -\n"
        "<b>👩🏼‍🦳Окрашивание седины за 10 минут:</b>\n"
        "  • Короткие волосы - 7.000₽\n"
        "  • Средние волосы - 9.000₽\n"
        "  • Длинные волосы - 12.000₽\n"
        "                                -\n"
        "<b>🌀Окрашивание по авторской методике с бличинг-эффектом:</b>\n"
        "  • Короткие волосы - 10.000₽\n"
        "  • Средние волосы - 12.000₽\n"
        "  • Длинные волосы - 15.000₽\n"
        "                                -\n"
        "<b>🪔Арома-Окрашивание:</b>\n"
        "  • Короткие волосы - 15.000₽\n"
        "  • Средние волосы - 17.000₽\n"
        "  • Длинные волосы - 20.000₽\n"
        "                                -\n"
        "<b>👩🏼AirTouch:</b>\n"
        "  • Короткие волосы - 13.000₽\n"
        "  • Средние волосы - 16.000₽\n"
        "  • Длинные волосы - 20.000₽"
    )
    await message.answer(text, parse_mode="HTML")


@user_private_router.message(F.text.lower() == "о заведении🏙")
@user_private_router.message(Command("about"))
async def about_cmd(message: types.Message):
    text = (
        "<b>О Заведении🏙:</b>\n"
        "📍 <b>Адрес:</b> Шелепиховская набережная, 16, Москва\n"
        "🔴 <a href='https://yandex.com/maps/?ol=geo&text=Shelepikhinskaya%20Embankment,%2016&sll=37.519404,55.755211&sspn=0.004630,0.008211&si=jj52vfgrefq7hgetjcqbw6fyp8'>"
        "Открыть на Яндекс.Картах</a>\n"
        "<b>ИЛИ:</b>\n"
        "🟠 <a href='https://maps.app.goo.gl/6M6GkVQV81ayHb3B9'>"
        "Открыть на Google.Maps</a>\n"
        "                                -\n"
        "<b>Маршрут по видео🗺:</b>\n"
        "📹 <a href='https://drive.google.com/file/d/1UZlGYbedSB8TlhUyCi1kfKU8CUjfJh2m/view?usp=drivesdk'>"
        "Смотреть видео</a>"
    )
    await message.answer(text, parse_mode="HTML")


@user_private_router.message(F.text.lower() == "уходы💆🏼‍♀️")
@user_private_router.message(Command("care"))
async def care_cmd(message: types.Message):
    text = (
        "<b>Уходы💆🏼‍♀️:</b>\n"
        "<b>🧴Масло Ethe, уход Absolute Beauty:</b>\n"
        "  • Короткие волосы - 2.000₽\n"
        "  • Средние волосы - 3.000₽\n"
        "  • Длинные волосы - 4.000₽\n"
        "                                -\n"
        "<b>⚡️KeyFibre, супер машинное востанновление структуры волоса:</b>\n"
        "  • Короткие волосы - 2.000₽\n"
        "  • Средние волосы - 4.000₽\n"
        "  • Длинные волосы - 6.000₽"
    )
    await message.answer(text, parse_mode="HTML")


@user_private_router.message((F.text.lower().contains('запис')) | (F.text.lower() == 'запись📝'))
@user_private_router.message(Command("sign_up"))
async def sign_up_cmd(message: types.Message):
    text = (
        "<b>Запись:📝</b>\n"
        "<b>Номер и Ник Ольгини:</b>\n"
        "☎️ +7 910 008-45-23\n"
        "👤 @olginyaAHD\n"
        " \n"
        "<b>Как это работает?</b>\n"
        "🗓 Вы смотрите свободные даты в календаре, связываетесь с Ольгиней, "
        "договариваетесь о времени и дате — она вас записывает.\n"
        " \n"
        "📅 <a href='https://docs.google.com/spreadsheets/d/12PUuuHDNrVhVoA2t6kAqGYMHJHfvM7VSO29tFkqLgyU/edit?usp=sharing'>"
        "Смотреть свободные даты в календаре</a>\n"
        "<b>(Переверните экран горизонтально для лучшего обзора!)</b>\n"
        " \n"
        "<b>Приемные часы: <u>12:00-21:00</u></b>\n"
        "⏰ Возможен выход в ночное время +50% к прайсу, время: <b><u>21:00-2:00</u></b>\n"
        " \n"
        "<b>Варианты оплаты:</b>\n"
        "✅ Наличными в заведении\n"
        "✅ Переводом"
    )
    await message.answer(text, parse_mode="HTML", disable_web_page_preview=True)


@user_private_router.message(F.text == "(FAQ) Вопросы⁉️")
@user_private_router.message(Command("questions"))
async def questions_cmd(message: types.Message):
    text = (
        "<b>(FAQ) Вопросы⁉️:</b>\n"
        "🔴 1. Какие препараты используются?\n"
        "🔴 2. Делаю Total Blond?\n"
        "🔴 3. Что такое бличинг эффект?\n"
        "🔴 4. Нужно ли что-то брать с собой?\n"
        "🔴 5. Нужно ли мыть голову перед каждым посещением мастера?\n"
        "🔴 6. Есть ли Wi-Fi в заведении?\n"
        "🔴 7. Есть ли Медицинская книжка?\n"
        " \n"
        "<b>Ответы:</b>\n"
        "✅ 1. Итальянская косметика премиум класса EMSIBETH.\n"
        "✅ 2. Нет, вредно для здоровья.\n"
        "✅ 3. <b>Бличинг эффект</b> - это эффект выгоревших волос на солнце.\n"
        "✅ 4. Если дорогая одежда - берите сменку.\n"
        "✅ 5. Окрашивание — <u>ОБЯЗАТЕЛЬНО</u>\n           Стрижка — <u>НЕ НУЖНО</u>\n"
        "✅ 6. Да, Wi-Fi присутствует.\n"
        "✅ 7. Да, Медицинская книжка присутствует."
    )
    await message.answer(text, parse_mode="HTML")

@user_private_router.message(F.text == "Об Ольгине👩🏻")
@user_private_router.message(Command("about_olginya"))
async def about_cmd(message: types.Message):
    text = (
        "<b>Об Ольгине👩🏻:</b>\n"
        " <b>•</b> Я — парикмахер Ольгиня с более чем 28-летним опытом. Специализируюсь на бережном окрашивании и модных стрижках — от коротких до длинных, не требующих сложной укладки. Обучалась в школе Dolores, проходила стажировку в Испании. Регулярно повышаю квалификацию в области окрашивания, стрижек и ухода за волосами. ⭐️\n"
        " \n"
        " <b>•</b> Работаю с премиальной итальянской косметикой Emsibeth. Благодаря её составу, уход уже включён в процесс окрашивания — волосы восстанавливаются, приобретают блеск, здоровый вид и становятся легкими в укладке. Краска держится долго, выглядит качественно и естественно.📍\n"
        " \n"
        " <b>•</b> Также обучаю клиентов простым укладкам: за один сеанс пошагово показываю, как самостоятельно собираться дома быстро и красиво. Даю рекомендации по домашнему уходу — с несмываемыми средствами и уходовыми процедурами, чтобы поддерживать результат между визитами в салон.😉"
)
    await message.answer(text, parse_mode="HTML")



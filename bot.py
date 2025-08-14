import asyncio
import os
import re

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode, ChatAction
from aiogram.filters import ChatMemberUpdatedFilter, IS_NOT_MEMBER, IS_MEMBER

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from middlewares.db import DataBaseSession
from database.engine import create_db, drop_db, session_maker
from handlers.user_private import user_private_router
from common.bot_cmds_list import private

bot = Bot(token=os.getenv('TOKEN'))
bot.my_admins_list = []

dp = Dispatcher()

dp.include_router(user_private_router)



def contains_emoji(text: str) -> bool:
  
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002500-\U00002BEF"  # chinese char
        "\U00002702-\U000027B0"
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "\U0001f926-\U0001f937"
        "\U00010000-\U0010ffff"
        "\u2640-\u2642"
        "\u2600-\u2B55"
        "\u200d"
        "\u23cf"
        "\u23e9"
        "\u231a"
        "\u231b"
        "\u2328"
        "\u23cf"
        "\u23e9"
        "\u23ed"
        "\u23f0"
        "\u23f3"
        "\u23f8-\u23fa"
        "]+",
        flags=re.UNICODE,
    )
    return bool(emoji_pattern.search(text))


@user_private_router.message()
async def unknown_command(message: types.Message):
   
    if message.sticker:
        await message.delete() 
        await message.answer("❌ Стикеры запрещены. Пожалуйста, используйте кнопки.")
        return

   
    if message.text:
        if contains_emoji(message.text):
            await message.delete()
            await message.answer("❌ Эмодзи запрещены. Пожалуйста, используйте кнопки.")
            return

        if message.text.startswith('/'):
            await message.answer("Неизвестная команда. Пожалуйста, используйте кнопки.")
            return

   
    if not message.text:
        await message.delete()
        await message.answer("❌ Разрешены только кнопки.")
        return

   
    await message.answer("❌ Неизвестная команда. Пожалуйста, используйте кнопки.")


async def on_startup(bot: Bot):
    run_param = False
    if run_param:
        await drop_db()
    await create_db()
    print("База данных создана. Бот запущен.")


async def on_shutdown(bot: Bot):
    print('бот лег')


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())


    print("Запуск поллинга...")
    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True
    )


if __name__ == "__main__":
    asyncio.run(main())
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import os

# Логирование
logging.basicConfig(level=logging.INFO)

# Получаем токен и ID админа из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

# Создаём экземпляры бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: Message):
    user = message.from_user
    user_data = (
        f"👤 Новый пользователь:\n\n"
        f"🆔 ID: {user.id}\n"
        f"👤 Имя: {user.first_name}\n"
        f"🔗 Ник: @{user.username if user.username else 'нет'}\n"
        f"🌐 Язык: {user.language_code}\n"
        f"📅 Дата: {message.date.strftime('%Y-%m-%d %H:%M:%S')}"
    )

    # Отправляем админу
    await bot.send_message(chat_id=ADMIN_ID, text=user_data)

    # Ответ пользователю
    await message.reply("Сәлем! Қош келдің 👋")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

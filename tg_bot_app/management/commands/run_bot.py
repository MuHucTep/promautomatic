import asyncio
from django.core.management.base import BaseCommand
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from asgiref.sync import sync_to_async

# Импортируем модели Django
from tg_bot_app.models import TelegramUser 

from config import BOT_TOKEN

TOKEN = BOT_TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher()

@sync_to_async
def get_or_create_user(user_id, username):
    obj, created = TelegramUser.objects.get_or_create(
        user_id=user_id,
        defaults={'username': username}
    )
    return obj, created

# Хэндлер aiogram
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    # Безопасно обращаемся к Django ORM
    user, created = await get_or_create_user(message.from_user.id, message.from_user.username)
    
    if created:
        await message.answer(f"Привет, {message.from_user.full_name}! Ты успешно зарегистрирован.")
    else:
        await message.answer(f"Рад видеть тебя снова, {message.from_user.full_name}!")

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

class Command(BaseCommand):
    help = "Запуск Telegram бота на aiogram"

    def handle(self, *args, **options):
        # Запускаем асинхронный event loop для бота
        asyncio.run(main())
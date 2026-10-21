import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Привет! Я помощник сообщества.\n\n"
        "Я умею:\n"
        "• приветствовать новичков\n"
        "• помогать админу с модерацией\n\n"
        "Команды:\n"
        "/rules — правила\n"
        "/help — помощь"
    )

@dp.message(Command("rules"))
async def rules(message: types.Message):
    await message.answer("Правила: будьте вежливы, без спама и рекламы.")

@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer("Напиши /start, чтобы начать.")

if __name__ == "__main__":
    dp.run_polling(bot)
import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())

async def cmd_start(message: Message):
    await message.answer(f"Hello World!")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try :
        asyncio.run(main())
    except KeyboardInterrupt :
        print("Stopped")
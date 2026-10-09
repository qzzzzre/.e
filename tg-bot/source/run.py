import asyncio
import logging
import random


from aiogram import Dispatcher, Bot
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from pathlib import Path

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


file_path = Path(__file__).parent / 'text.txt'

with open(file_path, 'r', encoding="utf-8") as f:
    text = f.readlines()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("meooow")

@dp.message(Command('swaga'))
async def cmd_swaga(message: Message):
    await message.answer(random.choice(text))

@dp.message(Command('help'))
async def cmd_help(message: Message):
   await message.answer('''
Сайт университета: fa.ru
Телеграм канал Информционного Комитета: https://t.me/informationcommittee''')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    try :
        asyncio.run(main())
    except KeyboardInterrupt :
        print("meow")
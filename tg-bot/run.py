import asyncio
import logging

from aiogram import Dispatcher, Bot, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("meooow")

@dp.message(Command('swaga'))
async def cmd_help(message: Message):
    await message.answer("meow")

@dp.message(F.text == 'freak')
async def cmd_freak(message: Message):
   await message.answer("freak")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try :
        asyncio.run(main())
    except KeyboardInterrupt :
        print("meow")
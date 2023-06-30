import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

with open("D:\\Python apps\\telegram bot\\config.txt") as f:
    TOKEN = f.read().strip()

API_TOKEN = TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Web', web_app=WebAppInfo(url='https://telegramapp.vercel.app/')))
    await message.reply("Привет, сейчас протестируем веб приложение!", reply_markup=markup)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
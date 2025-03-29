import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

API_TOKEN = '7344001504:AAFm9GovNta2Tj00Wc6Xax9KuXNfICJNi3s'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


button_schedule = KeyboardButton(' Расписание уроков')
keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_schedule)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я бот школы. Нажми на кнопку, чтобы узнать расписание уроков.", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == ' Расписание уроков')
async def schedule(message: types.Message):
    schedule_text = "Расписание уроков:\n1. Математика - Пн 9:00\n2. Английский - Вт 10:00\n3. Информатика - Ср 11:00\n4. Физика - Чт 12:00\n5. Химия - Пт 13:00"
    await message.answer(schedule_text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

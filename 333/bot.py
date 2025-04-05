import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

API_TOKEN = '7344001504:AAFm9GovNta2Tj00Wc6Xax9KuXNfICJNi3s'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Кнопки для всех дней недели
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
for day in days:
    keyboard.add(KeyboardButton(f'Расписание уроков {day}'))

# Функция логирования действий пользователя
def log_user_action(username, action):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("действия_пользователей.txt", "a", encoding="utf-8") as file:
        file.write(f"[{now}] Пользователь @{username} нажал \"{action}\"\n")

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я бот школы. Нажми на кнопку, чтобы узнать расписание уроков.", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == 'Расписание уроков Понедельник')
async def schedule_monday(message: types.Message):
    log_user_action(message.from_user.username or message.from_user.id, message.text)
    schedule_text = " Понедельник:\n1. Математика - 9:00\n2. Литература - 10:00\n3. История - 11:00\n4. Физкулбтура - 12:00"
    await message.answer(schedule_text)

@dp.message_handler(lambda message: message.text == 'Расписание уроков Вторник')
async def schedule_tuesday(message: types.Message):
    log_user_action(message.from_user.username or message.from_user.id, message.text)
    schedule_text = " Вторник:\n1. Английский - 9:00\n2. Физкультура - 10:00\n3. Химия - 11:00\n4. Обезьяны - 12:00"
    await message.answer(schedule_text)

@dp.message_handler(lambda message: message.text == 'Расписание уроков Среда')
async def schedule_wednesday(message: types.Message):
    log_user_action(message.from_user.username or message.from_user.id, message.text)
    schedule_text = " Среда:\n1. Русский язык - 9:00\n2. Информатика - 10:00\n3. Музыка - 11:00\n4. История - 12:00"
    await message.answer(schedule_text)

@dp.message_handler(lambda message: message.text == 'Расписание уроков Четверг')
async def schedule_thursday(message: types.Message):
    log_user_action(message.from_user.username or message.from_user.id, message.text)
    schedule_text = " Четверг:\n1. Биология - 9:00\n2. География - 10:00\n3. Физика - 11:00\n4. ИЗО - 12:00"
    await message.answer(schedule_text)

@dp.message_handler(lambda message: message.text == 'Расписание уроков Пятница')
async def schedule_friday(message: types.Message):
    log_user_action(message.from_user.username or message.from_user.id, message.text)
    schedule_text = "Пятница:\n1. Технология - 9:00\n2. ИЗО - 10:00\n3. Классный час - 11:00\n4. Музыка - 12:00"
    await message.answer(schedule_text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

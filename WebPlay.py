from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6691193910:AAEKQqgYYBC7-Bc6kTwqbk4r2UD8Jga30lk')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://novbichannel.github.io/')))
    await message.answer('Привет, мой друг!', reply_markup=markup)





executor.start_polling(dp)
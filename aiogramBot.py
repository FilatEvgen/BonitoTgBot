from aiogram import Bot, Dispatcher, executor, types

bot = Bot('6691193910:AAEKQqgYYBC7-Bc6kTwqbk4r2UD8Jga30lk')
dp = Dispatcher(bot)

@dp.message_handler(content_types=['photo'])
async def start(message: types.message):
    # await bot.send_message(message.chat.id, 'Hello')
    # await message.answer('Hello')
    await message.reply('Hello')
    # file = open('/some.png', 'rb')
    # await message.answer_photo(file)


@dp.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Site', url='https://vk.com/'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello', reply_markup=markup)

@dp.callback_query_handler()
async def callbeck(call):
    await call.message.answer(call.data)


@dp.message_handler(commands=['reply'])
async def reply(message: types.message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('Website'))
    await message.answer('Hello', reply_markup=markup)




executor.start_polling(dp)

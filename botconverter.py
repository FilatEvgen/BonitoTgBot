import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('6691193910:AAEKQqgYYBC7-Bc6kTwqbk4r2UD8Jga30lk')
currecy = CurrencyConverter()
amount = 0
# Обработка кнопки старт
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, введите сумму')
    bot.register_next_step_handler(message, summa)

# функция срабатывающая после получения суммы от пользователя
def summa(message):
    global amount
    try:
        amount =int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат ввода')
        bot.register_next_step_handler(message,summa)
        return

    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        btn4 = types.InlineKeyboardButton('Другое значение', callback_data='else')
        markup.add(btn1, btn2,btn3,btn4)
        bot.send_message(message.chat.id,'Выберите пару валют', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Число должно быть больше 0')
        bot.register_next_step_handler(message, summa)

#  Обработка callback_data(т.е. кнопок)
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = currecy.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id,f'Получается: {round(res, 2)}. Можете заного вписать сумму')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Введите пару значений через слэш')
        bot.register_next_step_handler(call.message, my_currency)
def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currecy.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Получается: {round(res, 2)}. Можете заного вписать сумму')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, f'Что-то не так. Впишите значение заново')
        bot.register_next_step_handler(message, my_currency)


bot.polling(none_stop=True)
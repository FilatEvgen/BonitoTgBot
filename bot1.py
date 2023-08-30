import telebot
from telebot import types
import webbrowser
import sqlite3

bot = telebot.TeleBot('6418994897:AAGHN6QoTZB8Wzya5j3nQexlDVqpWLzxfVw')
# Полностью описанна работа с сервером SQL

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введите ваше имя')
#     bot.register_next_step_handler(message, user_name)
#
# def user_name(message):
#     name = message.text.strip()
#     bot.send_message(message.chat.id, 'Введите пароль')
#     bot.register_next_step_handler(message, user_pass, name)
#
# def user_pass(message, name):
#     password = message.text.strip()
#     conn = sqlite3.connect('bottel1.sql')
#     cur = conn.cursor()
#
#     cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, pass TEXT)")
#     cur.execute("INSERT INTO users (name, pass) VALUES (?, ?)", (name, password))
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Список пользователей', callback_data='users'))
#
#     bot.send_message(message.chat.id, "Пользователь зарегистрирован!", reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     conn = sqlite3.connect('bottel1.sql')
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM users")
#     users =  cur.fetchall()
#
#     info = ''
#     for el in users:
#         info += f'Имя: {el[1]}, пароль: {el[2]}\n'
#
#
#     cur.close()
#     conn.close()
#
#     bot.send_message(call.message.chat.id, info)
#
#
#
# bot.polling()



# Обычный бот где все расписано

# bot.send_message(message.chat.id, 'Введите пароль')
# bot.register_next_step_handler(message, user_pass)

#Добавление кнопок вначале
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('Перейти на сайт☝🏻')
#     markup.row(btn1)
#     btn2 = types.KeyboardButton('Удалить фото')
#     btn3 = types.KeyboardButton('Изменить текст')
#     markup.row(btn2, btn3)
#     file = open('./bonito2.jpg', 'rb')
#     bot.send_photo(message.chat.id, file,reply_markup=markup)
#     # bot.send_message(message.chat.id, f'Приветствую тебя мой Ментор! , {message.from_user.first_name} {message.from_user.last_name}', reply_markup=markup)
#     bot.register_next_step_handler(message, on_click)
#
# def on_click(message):
#     if message.text == 'Перейти на сайт':
#         bot.send_message(message.chat.id, 'Website is open')
#     elif message.text == 'Удалить фото':
#         bot.send_message(message.chat.id, 'Deleted')
#
# # Cоздание кнопок и редактор вида кнопок
# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 =(types.InlineKeyboardButton('Перейти на сайт', url='https://vk.com/bonitodeti'))
#     markup.row(btn1)
#     btn2 = (types.InlineKeyboardButton('Удалить фото', callback_data='delete'))
#     btn3 = (types.InlineKeyboardButton('Изменить текст', callback_data='edit'))
#     markup.row(btn2,btn3)
#
#     bot.reply_to(message, 'Какое красивое фото!',reply_markup=markup)
#
# # функция для обработки callback_data
# @bot.callback_query_handler(func=lambda callback: True)
# def callback_massage(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
#     elif callback.data == 'edit':
#         bot.edit_message_text('Edit text',callback.message.chat.id, callback.message.message_id )
#
#
#
# # Вывод сайта(ссылки)
# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open('https://vk.com/bonitodeti')
#
#
# @bot.message_handler(commands=['start','main','Hello'])
# def main(message):
#     bot.send_message(message.chat.id, f'Приветствую тебя мой Ментор✌️! , {message.from_user.first_name} {message.from_user.last_name} ')
#
# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, 'Help Information',parse_mode='html')
#
#
#
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(massage.chat.id,
#                          f'Приветствую тебя мой Ментор!, {message.from_user.first_name} {message.from_user.last_name} ')
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f'ID: {message.from_user.id}')
#     elif message.text.lower() == '/start':
#         bot.send_message(massage.chat.id,
#                          f'Приветствую тебя мой Ментор!, {message.from_user.first_name} {message.from_user.last_name} ')
#
#
#
# bot.polling(none_stop=True)
import telebot
import requests
import json

bot = telebot.TeleBot('6691193910:AAEKQqgYYBC7-Bc6kTwqbk4r2UD8Jga30lk')
# Ключ для получения погоды
API = '59bcc71d476f78073cea0d3ce53a7339'

# Обработка кнопки старт
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет, я рад тебя видеть! Напиши название города')

# Получение погоды через URL адрес и добавление картинок в зависимости от темпера
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data =json.loads(res.text)
        temp = data ['main']['temp']
        bot.reply_to(message,f'Сейчас погода: {temp}')

        image = 'ocr.jpeg' if temp > 5.0 else '1683718751_papik-pro-p-otkritki-u-pogodi-net-plokhoi-pogodi-24.jpg'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id,file)
    else:
        bot.reply_to(message, 'Город указан не верно!!!')


bot.polling(none_stop=True)




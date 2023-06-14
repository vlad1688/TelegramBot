import json
import telebot
import requests

bot = telebot.TeleBot("6121313023:AAFTJhDHwRygi5tRFC49zIDAIGJOLedBHXc")
API = "29d4796418a2468831b621594537b4b4"

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, напиши название города")


@bot.message_handler(content_types=['text'])
def weather(message):
    city = message.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    if res.status_code == 200:
        weatherCity = json.loads(res.text)
        bot.reply_to(message, f'Сейчас погода: {weatherCity["main"]["temp"]}')
    else:
        bot.reply_to(message, "Город введен не верно")
bot.polling(none_stop=True)

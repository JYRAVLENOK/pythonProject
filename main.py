import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot("1735384641:AAE_LoZ6D4AMDUe2_mxuWG7ajou4CnfKbY4", parse_mode=None)
DOLLAR_RUB = 'https://www.google.com/search?client=opera-gx&q=rehc+ljkkfhf&sourceid=opera&ie=UTF-8&oe=UTF-8'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.438'}

full_page = requests.get(DOLLAR_RUB, headers=headers)
soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll("span", {"class": "Dflfde", "class": "SwHCTb", "data-precision": 2})
value = "Один доллар США равен " + convert[0].text + " рублей"

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Что ты хочешь сделать?")
    meeting = "Привет! <i>{0}</i> Что ты хочешь сделать?"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_weather = types.KeyboardButton("Прогноз погоды")
    key_value = types.KeyboardButton("Курс валюты")
    markup.add(key_weather, key_value)
    bot.send_message(message.chat.id, meeting.format(message.from_user.first_name),
                     parse_mode="html", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def answer_key(message):
    if message.chat.type == "private":
        if message.text == "Прогноз погоды":
            pass
        if message.text == "Курс валюты":
            bot.send_message(message.chat.id, value.format(message.from_user.first_name))
bot.polling()
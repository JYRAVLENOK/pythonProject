import telebot
from telebot import types
import rates

bot = telebot.TeleBot("1735384641:AAE_LoZ6D4AMDUe2_mxuWG7ajou4CnfKbY4", parse_mode=None)

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
            value_rate = rates.Rates.GetRate(page=rates.Rates.DOLLAR_RUB, headers=rates.Rates.headers)
            bot.send_message(message.chat.id, value_rate.format(message.from_user.first_name))
bot.polling()
import telebot
from telebot import types
import Config
EUR=50
USD=60
GOLD=1000
BTC=20000
bot = telebot.TeleBot(Config.token)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text=="/start":
        bot.send_message(message.chat.id, "Привет, приступим к конвертации")
        markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("Евро")
        markup.row("Доллар")
        markup.row("Золото")
        markup.row("Биток")
        msg=bot.send_message(message.chat.id,"Выберите валюту",reply_markup=markup)
        bot.register_next_step_handler(msg,convert)
    elif message.text!="/start":
        bot.send_message(message.chat.id, "Напиши /start ")
def convert(message):
        if message.text=="Евро":
            msg=bot.send_message(message.chat.id,"Введите сумму в рублях")
            bot.register_next_step_handler(msg,eur)
        elif message.text=="Доллар":
            msg=bot.send_message(message.chat.id,"Введите сумму в рублях")
            bot.register_next_step_handler(msg,usd)
        elif message.text=="Золото":
            msg=bot.send_message(message.chat.id,"Введите сумму в рублях")
            bot.register_next_step_handler(msg,gold)
        elif message.text=="Биток":
            msg=bot.send_message(message.chat.id,"Введите сумму в рублях")
            bot.register_next_step_handler(msg,btc)
        else:
            msg=bot.send_message(message.chat.id,"Введите корректные данные")
            bot.register_next_step_handler(msg,convert)
def eur(message):
    try:
        bot.send_message(message.chat.id,float(message.text)/EUR)
    except ValueError:
        bot.send_message(message.chat.id,"Введите число")
        msg = bot.send_message(message.chat.id, "Введите сумму в рублях")
        bot.register_next_step_handler(msg, eur)
def usd(message):
    try:
        bot.send_message(message.chat.id,float(message.text)/USD)
    except ValueError:
        bot.send_message(message.chat.id,"Введите число")
def gold(message):
    try:
        bot.send_message(message.chat.id,float(message.text)/GOLD)
    except ValueError:
        bot.send_message(message.chat.id,"Введите число")
def btc(message):
    try:
        bot.send_message(message.chat.id,float(message.text)/BTC)
    except ValueError:
        bot.send_message(message.chat.id,"Введите число")

bot.polling(none_stop=True, interval=0)
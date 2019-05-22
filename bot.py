import telebot
from telebot.types import Message
import random

TOKEN = '727281713:AAFeNruJlHcYEo_Hdb3yOrvAyNtHfFhmDvE'
bot = telebot.TeleBot(TOKEN)

updates = bot.get_updates()

smile = ['😂', '😘', '❤', '😍', '😊', '😁', '☺', '😔', '😄', '😭', '😳']


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message):
    bot.reply_to(message, 'Привет %s %s!' % (message.from_user.first_name, message.from_user.last_name))
    print(message)


@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    bot.reply_to(message, random.choice(smile))
    print(message)


bot.polling()

import telebot
from telebot.types import Message
import random

TOKEN = '727281713:AAFeNruJlHcYEo_Hdb3yOrvAyNtHfFhmDvE'

bot = telebot.TeleBot(TOKEN)

smile = ['😂', '😘', '❤', '😍', '😊', '😁', '☺', '😔', '😄', '😭', '😳']


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello!")


@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    bot.reply_to(message, random.choice(smile))


bot.polling()

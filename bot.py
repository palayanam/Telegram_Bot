import telebot
from telebot.types import Message
import random

TOKEN = '727281713:AAFeNruJlHcYEo_Hdb3yOrvAyNtHfFhmDvE'
bot = telebot.TeleBot(TOKEN)

updates = bot.get_updates()
smile = ['😂', '😘', '❤', '😍', '😊', '😁', '☺', '😔', '😄', '😭', '😳']
user_val = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
i = 0


@bot.message_handler(commands=['start', 'help'], )
def send_welcome(message: Message):
    global i
    bot.reply_to(message, 'Привет %s!' % message.from_user.username)
    user_val[i] = message.from_user
    print(user_val[i])
    i += 1


@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    global i
    bot.reply_to(message, random.choice(smile))
    user_val[i] = message.from_user
    print(user_val[i], i)
    i += 1


bot.polling()

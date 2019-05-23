import telebot
from telebot import types
from telebot.types import Message
import random

TOKEN = '727281713:AAFeNruJlHcYEo_Hdb3yOrvAyNtHfFhmDvE'
bot = telebot.TeleBot(TOKEN)

updates = bot.get_updates()
smile = ['😂', '😘', '❤', '😍', '😊', '😁', '☺', '😔', '😄', '😭', '😳']
user_val = [{}]
i = 0

markup = types.ReplyKeyboardMarkup()
itembtna = types.KeyboardButton('Cords')
itembtnv = types.KeyboardButton('Data')
markup.row(itembtna, itembtnv)


@bot.message_handler(commands=['start', 'help'], )
def send_welcome(message: Message):
    global i
    bot.send_message(message.from_user.id, 'Look:', reply_markup=markup)
    user_val.insert(i, message.from_user)
    print(user_val[i], i)
    i += 1


@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    global i
    bot.send_location(message.from_user.id, -19.79831, 32.70595, reply_markup=markup)
    user_val.insert(i, message.from_user)
    print(user_val[i], i)
    i += 1


bot.polling()

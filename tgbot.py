import telebot
import random

from telebot.types import Message

TOKEN = '721378927:AAF3OX-i_oXfK0asbUJzDi5JhVVujShLomI'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start','help'])
def command_handler(message: Message):
    reply_to(message, str('hello, im is helpless bot'))

@bot.message_handler(content_types=['text'])
def echo_digits(message: Message):
    bot.reply_to(message, str(random.random()))

import time
while True:
    time.sleep(1)



bot.polling(none_stop=True, )

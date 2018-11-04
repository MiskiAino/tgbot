import telebot
import random

TOKEN = '721378927:AAF3OX-i_oXfK0asbUJzDi5JhVVujShLomI'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def echo_digits(message: Message):
    bot.reply_to(message, str(random.random()))

bot = polling(timeout=60)

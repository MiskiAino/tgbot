import telebot
import random

from telebot.types import Message

TOKEN = '721378927:AAF3OX-i_oXfK0asbUJzDi5JhVVujShLomI'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start','help'])
def command_handler(message: Message):
    bot.reply_to(message, 'hello, im is helpless bot')

@bot.message_handler(content_types=['text'])
def echo_digits(message: Message):
    bot.reply_to(message, str(random.random()))

# fdf

while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        logger.error(e)  # или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)

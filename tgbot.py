import telebot
import random

from telebot.types import Message

TOKEN = '721378927:AAF3OX-i_oXfK0asbUJzDi5JhVVujShLomI'

bot = telebot.TeleBot(TOKEN)
USERS = set()


@bot.message_handler(commands=['start','help'])
def command_handler(message: Message):
    bot.reply_to(message, 'ya nichego ne umeyu')


@bot.message_handler(commands=['pogoda'])
def command_handler(message: Message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('a')
    itembtn2 = types.KeyboardButton('v')
    itembtn3 = types.KeyboardButton('d')
    markup.add(itembtn1, itembtn2, itembtn3)
    tb.send_message(chat_id, "Choose one letter:", reply_markup=markup)



@bot.message_handler(content_types=['text'])
def echo_digits(message: Message):
    reply = str(random.random())

    if message.from_user.id in USERS:
        reply = f"{message.from_user.username}, hello again"

    bot.reply_to(message, reply)
    USERS.add(message.from_user.id)


@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.reply_to(message, 'опять стикеры с оняме')


bot.polling(none_stop=True)

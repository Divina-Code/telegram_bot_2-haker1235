import telebot
from myToken import TOKEN
from random import randint
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def otvet_na_text(message):

    random_number = randint(1000, 9999)
    bot.send_message(message.chat.id, random_number)

bot.polling()

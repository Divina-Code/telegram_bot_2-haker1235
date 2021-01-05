
from myToken import TOKEN
import telebot
from random import choice, shuffle

words = ['антарктида', 'амплитуда', 'локомотив', 'индустриализация']

word = choice(words).lower()
shuffle_word = list(word)
shuffle(shuffle_word)
a = 0


bot = telebot.TeleBot(TOKEN)
@bot.message_handler(content_types = ['text'])

def otvet_na_text(message):
    global a
    if a == 0:
        bot.send_message(message.chat.id,"Угадай слово: "+ ''.join(shuffle_word) +'\t')
        a = a + 1
        message.text.lower().split()

    else:
        if message.text == word:
            bot.send_message(message.chat.id,"Угадал")
            bot.send_message(message.chat.id,"#"*30)
            a = 0

        else:
            bot.send_message(message.chat.id,"Не Угадал")


bot.polling()

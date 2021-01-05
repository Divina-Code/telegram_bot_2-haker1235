
from myToken import TOKEN
import telebot
from random import choice, shuffle, randint

words = ['антарктида', 'амплитуда', 'локомотив', 'индустриализация']

word = choice(words).lower()
shuffle_word = list(word)
shuffle(shuffle_word)
a = 0


bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands = ['pass'])

def komanda_pass(message):
    bot.send_message(message.chat.id, "Я сгенерирую тебе пароль из 4х цифр")
    rand_number = randint(1000, 9999)
    bot.send_message(message.chat.id, str(rand_number))

@bot.message_handler(commands=['play'])
def komanda_start(message):
    global a
    if a == 0:
        bot.send_message(message.chat.id,"Угадай слово: "+ ''.join(shuffle_word) +'\t')
        a = a + 1
        message.text.lower().split()

    else:
        if message.text == word:
            bot.send_message(message.chat.id,"Угадал, молодец")
            a = 0

        else:
            bot.send_message(message.chat.id,"Не Угадал, попробуй ещё раз")


bot.polling()

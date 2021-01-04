import telebot
from myToken import TOKEN
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def otvet_na_text(message):
    mes = message.text
    user = message.chat.username
    id = message.chat.id
    inp = message.text.lower().split()
    for word in inp:
        if word[::-1] == word:
            bot.send_message(id, f"{word} это палиндром")
        else:
            bot.send_message(id, f"{word} это не палиндром")
bot.polling()

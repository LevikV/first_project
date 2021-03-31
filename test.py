import telebot
bot = telebot.TeleBot('1798432712:AAFKD_GMpkCeFhyMFzm6Kg3gSBXABh_jix0')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.from_user.id, 'Привет, я Яна! Прежде, чем начать наше общение, ты должен пообещать никому об этом не рассказывать)')
@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.reply_to(message, 'Не понимаю, что это значит,хм...')
bot.polling(none_stop=True)
import telebot
bot = telebot.TeleBot('1798432712:AAFKD_GMpkCeFhyMFzm6Kg3gSBXABh_jix0')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот, приятно познакомиться, {message.from_user.first_name}')
@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит,хм...')
bot.polling(none_stop=True)
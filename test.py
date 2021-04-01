import telebot
bot = telebot.TeleBot('1798432712:AAFKD_GMpkCeFhyMFzm6Kg3gSBXABh_jix0')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Согласен', callback_data='sog-1'),
        telebot.types.InlineKeyboardButton('Не согласен', callback_data='sog-0')
    )
    bot.send_message(message.from_user.id, 'Привет, я бот Яна! Прежде, чем пообщаться с моей хозяйкой, ты должен пообещать никому об этом не рассказывать)',reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.reply_to(message, 'Не понимаю, что это значит,хм...')
#Функция обработчик нажатия кнопок
@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('sog-1'):
        bot.send_message(query.message.chat.id, 'Я рада, что ты согласен. Сохранить конфеденциальность для меня очень важно!')
    bot.edit_message_reply_markup(query.message.chat.id, query.message.message_id)

bot.polling(none_stop=True)
import telebot
bot = telebot.TeleBot('1798432712:AAFKD_GMpkCeFhyMFzm6Kg3gSBXABh_jix0')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing') #Показываем индикатор ввода клавиатуры
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
    bot.send_chat_action(query.message.chat.id, 'typing') #Показываем индикатор ввода клавиатуры
    data = query.data
    if data.startswith('sog-1'):
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('😍Конечно😍', callback_data='get-anket'),
            telebot.types.InlineKeyboardButton('🔥Давай быстрее🔥', callback_data='get-anket')
        )
        bot.send_message(query.message.chat.id, 'Я рада 😍, что ты согласился держать в тайне наше общение)) Сохранить конфеденциальность для меня очень важно!')
        bot.send_message(query.message.chat.id, 'Показать тебе моих хозяек?', reply_markup=keyboard)
        bot.edit_message_reply_markup(query.message.chat.id, query.message.message_id) #убираем клавиатуру
    elif data.startswith('sog-0'):
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Обещаю', callback_data='sog-1'),
            telebot.types.InlineKeyboardButton('Не обещаю', callback_data='sog-0')
        )
        bot.send_message(query.message.chat.id, 'Ммм, так нельзя)) но я как и моя хозяйка, не из стеснительных, спрошу еще раз)) Обещаешь никому не рассказывать про наше общение?', reply_markup=keyboard)
        bot.edit_message_reply_markup(query.message.chat.id, query.message.message_id)  # убираем клавиатуру
@bot.message_handler(content_types=['photo'])
#Получение id фото
def photoid(message):
   photo = max(message.photo, key=lambda x: x.height) #Получаем максимальный размер изображения
   bot.send_message(message.chat.id, photo.file_id)

bot.polling(none_stop=True)
import telebot
from telebot import  types

bot = telebot.TeleBot("5392280821:AAHE92CPmueuQLb8gbuxAe6KXjZD8CwkurM")

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привіт!👋 <b>{message.from_user.first_name}</b> \n\nЯ Файно бот 🤖 \n\nЗаливай своє фото на оцінку, та оцінюй інших людей 💁 \nНабирай бали за оцінки інших людей, та виривайся вперед у рейтингу🔝'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(message.chat.id, 'Давай створимо тобі анкету прямо зараз!')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    create_ank = types.InlineKeyboardButton('Створити анккету', callback_data='create')
    peredumav = types.InlineKeyboardButton('Ні, я передумав', callback_data='nope')
    markup.add(create_ank, peredumav)
    bot.send_message(message.chat.id, 'Напиши свою відповідь \n\nСтворити анккету\nНі, я передумав', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'create':
        bot.send_message(call.message.chat.id, 'Супер!')
    elif call.data == 'nope':
        bot.send_message(call.message.chat.id, 'Шкода😢')


bot.polling(none_stop=True)

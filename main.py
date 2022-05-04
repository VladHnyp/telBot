import telebot
from telebot import  types


bot = telebot.TeleBot("5392280821:AAHE92CPmueuQLb8gbuxAe6KXjZD8CwkurM")

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привіт!👋 <b>{message.from_user.first_name}</b> \n\nЯ Файно бот 🤖 \n\nЗаливай своє фото на оцінку, та оцінюй інших людей 💁 \nНабирай бали за оцінки інших людей, та виривайся вперед у рейтингу🔝'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(message.chat.id, 'Давай створимо тобі анкету прямо зараз!')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    create_ank = types.InlineKeyboardButton('Створити анккету',)
    peredumav = types.InlineKeyboardButton('Ні, я передумав',)
    markup.add(create_ank, peredumav)
    bot.send_message(message.chat.id, 'Напиши свою відповідь \n\nСтворити анккету\nНі, я передумав', reply_markup=markup)


@bot.message_handler()
def get_usser_text(message):
    if message.text == "Створити анккету":
        bot.send_message(message.chat.id, "Супер!", reply_markup=telebot.types.ReplyKeyboardRemove())
    elif message.text == "Ні, я передумав":
        bot.send_message(message.chat.id, "Шкода", reply_markup=telebot.types.ReplyKeyboardRemove())
    elif message.text == "путін":
        bot.send_message(message.chat.id, "Хуйло")




bot.polling(none_stop=True)

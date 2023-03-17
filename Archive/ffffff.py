import telebot
from telebot import types  # для указание типов
import config


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def send_welcome(message: types.Message):
    bot.send_message(chat_id=message.chat.id, text='Привет, как твое имя?')
    k = 0
    dic = {'chat_id': message.chat.id}
    bot.register_next_step_handler(message, get_name, k, dic)


def get_name(message: types.Message, k, dic):
    # print(k)
    # тут у вас то что ввел юзер
    if k == 5:
        print(dic)
        bot.send_message(chat_id=message.chat.id, text=f'"Предыдущее сбщ:", {message.text}\n'
                                                       f'Этап: {k} - ФИНИШ')
    else:
        dic.update({k: message.text})
        bot.send_message(chat_id=message.chat.id, text=f'"Предыдущее сбщ:", {message.text}\n'
                                                       f'Этап: {k}')
        k +=1
        bot.register_next_step_handler(message, get_name, k, dic)


bot.polling(none_stop=True)
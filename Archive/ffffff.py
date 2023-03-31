import telebot
import config
bot = telebot.TeleBot(config.token)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=message.chat.id, text="Привет, я эхо-бот! Напиши, что-нибудь, а я повторю.")

@bot.message_handler()
def echo_message(message):
    bot.send_message(chat_id=message.chat.id, text='Привет, как твое имя?')
    k = 0
    bot.register_next_step_handler(message, new_text, k)


def new_text(message, k):
    if k == 5:
        bot.send_message(chat_id=message.chat.id, text=f'"Предыдущее сбщ:", {message.text}\n'
                                                       f'Этап: {k} - ФИНИШ')
    else:
        bot.send_message(chat_id=message.chat.id, text=f'"Предыдущее сбщ:", {message.text}\n'
                                                       f'Этап: {k}')
        k +=1
        bot.register_next_step_handler(message, new_text, k)

bot.polling()
import telebot
from telebot import types  # для указание типов
import config
from poll import text_result, questions
import json
import os

bot = telebot.TeleBot(config.token)



answers = list()
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/next")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     text="Я тестовый бот. Задам тебе вопрос, выбери /next", reply_markup=markup)

@bot.message_handler(commands=['next'])
def question(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    id = message.chat.id
    file_path = f"{id}.json"
    if os.path.exists(file_path):
        with open(f'{id}.json') as f:
            d = json.load(f)
        question_number = len(d)
        question = questions[question_number]
    else:
        data = []
        with open(f'{id}.json', 'w') as f:
            json.dump(data, f)
        question = questions[0]

    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text=question, reply_markup=markup)


@bot.message_handler()
def catch_answer(message):
    id = message.chat.id
    text = message.text
    with open(f'{id}.json', 'w') as f:
        d = json.load(f)
        d.append(text)
        json.dump(d, f)

bot.polling(none_stop=True)
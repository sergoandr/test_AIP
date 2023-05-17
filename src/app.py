import os
import json
from telebot import types, TeleBot
from dto import DbConnection

bot = TeleBot(os.environ['BOT_TOKEN'])
db = DbConnection()

def gen_markup(options, k):
    markup = types.InlineKeyboardMarkup(row_width=2)
    l = [types.InlineKeyboardButton(x, callback_data='{\"questionNumber\": ' +
                                                     str(k) + ',\"answerText\": "' + x + '"}')
         for x in options]
    markup.add(*l)
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    data = call.data
    if data == 'Start: No':
        return bot.edit_message_text(chat_id=call.message.chat.id,
                                     message_id=call.message.message_id,
                                     text='На нет и суда нет :)')
    elif data == 'Start: Yes':
        # print(call.message)
        db.insert_user(name=call.message.chat.first_name, chat_id=call.message.chat.id)
        text, options = db.get_question_by_id(qid=0)
        return bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=text,
                              reply_markup=gen_markup(options, 0))
    req = data.split('_')
    print(req)
    # Распарсим полученный JSON
    json_string = json.loads(req[0])
    k = json_string['questionNumber']
    answer = json_string['answerText']
    db.add_answer(chat_id=call.message.chat.id,
                  question_id=k,
                  answer=answer)  # записываем ответ на предыдущий вопрос

    print()
    if k+1 == len(db.questions.all()):
        score = 2
        return bot.edit_message_text(chat_id=call.message.chat.id,
                                     message_id=call.message.message_id,
                                     text=f'спасибо за ответы, вы набрали: {score} баллов')

    text, options = db.get_question_by_id(qid=k + 1)
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text=text,
                          reply_markup=gen_markup(options, k + 1))


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton('Да', callback_data='Start: Yes'),
               types.InlineKeyboardButton('Нет', callback_data='Start: No'),)
    bot.send_message(chat_id=message.chat.id, text='Привет, я бот! Ответишь на мои вопросы?',
                     reply_markup=markup)


# ['{"questionNumber":0,"answerText":"Да"}']
if __name__ == '__main__':
    bot.polling()

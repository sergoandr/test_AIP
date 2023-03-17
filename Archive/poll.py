
close_options = ['Да', 'Нет']

questions = [
    {'text': 'Выходите ли вы из себя по малейшему поводу?', 'type': 'closed', 'options': close_options},
    {'text': 'Боитесь ли вы разозлить человека, который заведомо физически сильнее вас?', 'type': 'closed', 'options': close_options},
    {'text': 'Начинаете ли вы скандалить, чтобы на вас обратили внимание?', 'type': 'closed', 'options': close_options},
    {'text': 'Любите ли вы ездить на большой скорости, даже если это связано с риском для жизни?', 'type': 'closed', 'options': close_options},
    {'text': 'Увлекаетесь ли вы лекарствами, когда заболеете?', 'type': 'closed', 'options': close_options},
    {'text': 'Пойдете ли вы на все, чтобы получить то, что вам очень хочется?', 'type': 'closed', 'options': close_options},
    {'text': 'Любите ли вы больших собак?', 'type': 'closed', 'options': close_options},
    {'text': 'Любите ли вы сидеть часами на солнце?', 'type': 'closed', 'options': close_options},
    {'text': 'Уверены ли вы, что когда-нибудь станете знаменитостью?', 'type': 'closed', 'options': close_options},
    {'text': 'Умеете ли вы вовремя остановиться, если чувствуете, что начинаете проигрывать?', 'type': 'closed', 'options': close_options},
    {'text': 'Привыкли ли вы много есть, даже если не голодны?', 'type': 'closed', 'options': close_options},
    {'text': 'Любите ли вы знать заранее, что вам подарят?', 'type': 'closed', 'options': close_options}
]

class Anket:
    def __init__(self, config):
        self.config = config
        self.length = len(config)
        self.answers = None
        self.scores = 0
    def add_answers(self, answers: list):
        self.answers = answers
        self._counter()
    def _counter(self):
        if not self.answers:
            return print("Нет ответов")
        for i in range(self.length):
            qtype = self.config[i]['type']
            qoptions =  self.config[i]['options']
            qanswer = self.answers[i]
            if qtype == 'closed':
                self.scores += 1 if qanswer == 'Да' else + 0
            if qtype == 'multiple_choice':
                pass
            if qtype == 'number':
                pass

        print(self.scores)


answers = ['Да', 'Нет', 'Нет', 'Нет', 'Нет', 'Нет', 'Да', 'Нет', 'Нет', 'Нет', 'Нет', 'Нет']

anketa = Anket(questions)
anketa.add_answers(answers)



# positive = [2, 10]
# negative = [1, 3, 4, 5, 6, 8, 9, 11, 12]
# превратить вопросы и варианты ответов в конфиг
# создать класс с методами обработки конфига (каунтер сравнивает словарь ответов с конфигом и выдает балл)
# что если ответы это множественный выбор с выбором нескольких вариантов (есть ли ответ в конфиге - балл), свободный ответ (поиск слов?)
# протавить балл 1-10
# виды получения баллов - полное попадание, неск из вариантов, коэффициент(для шкал
# паспортичка - без баллов
# ООП отдельные классы вопрос и ответ, ответ наследуется от вопроса и содержит методы обработки,
# отдельный класс анкета, который инициализирует вопросы по конфигу
# примимает ответы словарем и возвращает анкету и результат

def text_result(answers: list):
    int_result = counter(answers)
    if int_result > 8:
        result = "Вы - сама мудрость. Вы благоразумны, потребности ваши умеренны. \n\
                 Вы не ждете разочарования. Но, наверное, можно быть немного  \n \
                 подинамичнее. Это облегчит общение с людьми и сделает жизнь немного \n\
                проще..."
    elif int_result <= 8 and int_result >= 4:
        result =    "Золотая середина. У вас есть прекрасное чувство меры. \n" \
                    "Вы точно знаете свои возможности и не пытаетесь поймать журавля в небе. \n"\
                    "Хотя в вас есть и немного сумасбродства, которое придает людям такое очарование!"

    else:# int_result < 4:
        result = "Можно сказать одно: вы абсолютно безрассудны. Вам всего всегда мало.  \n\
                 Вы часто чувствуете себя несчастным из-за этой кажущейся  \n\
                 неудовлетворенности. Наш совет: научитесь радоваться приятным мелочам, \n\
                  которых в жизни не так уж мало. Это поможет стать вам спокойнее и  \n\
                 рассудительнее."


    return result


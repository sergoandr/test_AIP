import abc


class AbstractFactory(metaclass=abc.ABCMeta):
    """
    Создаем шаблон Абстрактной фабрики
    """
    def __init__(self, questions, answers):
        self.questions = questions
        self.answers = answers
    @abc.abstractmethod
    def create_poll(self):
        pass

class FormFactory(AbstractFactory):
    """
    Создаем первую реальную фабрику по шаблону
    """
    def create_poll(self):
        score = 0
        for a in range(len(self.answers)):
            if questions[a]["type"] == "age":
                score += 1 if self.answers[a] > 20 else +0
            if questions[a]["type"] == "close":
                score += 1 if self.answers[a] == "Да" else +0
        return ConcreteForm(self.questions, score)

class AbstractForm(metaclass=abc.ABCMeta):
    """
    Создаем шаблон для продукта, который хотим получать из фабрики
    """
    def __init__(self, questions, score):
        self.questions = questions
        self.score = score

    @abc.abstractmethod
    def save(self):
        pass

class ConcreteForm(AbstractForm):
    """
    Создаем класс второго продукта типа А, который требует бизнес,
    со своим функционалом
    """
    # s = 1
    def save(self):
        pass
    def message_text(self):
        return f"Вы набрали {self.score} баллов!"


answers = ['Тимур', 20]
questions = [
    {"text": "Как вас зовут?", "type": "open"},
    {"text": "Сколько вам лет?", "type": "age"},
    # {"text": "Вы обучаетесь в КИУ?", "type": "close"}
]
factory = FormFactory(questions,answers)
form = factory.create_poll()
score = form.score
text = form.message_text()
f = form.s
f = 1+1
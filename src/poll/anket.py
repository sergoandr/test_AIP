from .config import questions
from dto.base import db


class Anket:
    def __init__(self, config):
        self.config = config
        self.length = len(config)
        self.answers = None
        self.scores = 0

    def add_answers(self, answers: list):
        print(f"Add_answers {answers}")
        self.scores = 0
        self.answers = answers
        return self.scores

    def get_question(self, k):
        return db.get_text_by_id(k)


    def get_score(self, chat_id: int):
        answers = db.get_user_answers(chat_id)

        score = 0
        for i in range(len(answers)):
            qtype = db.get_type_by_id(i)
            if qtype == 'closed':
                    if answers[i] == 'Да':
                        score += 1
                    else:
                        score += 0
            if qtype == 'multiple_choice':
                score += db.get_options_by_id(i + 1).index(answers[i])

        return score


anket = Anket(questions)
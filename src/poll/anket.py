class Anket:
    def __init__(self, config):
        self.config = config
        self.length = len(config)
        self.answers = None
        self.scores = 0

    def add_answers(self, answers: list):
        self.scores = 0
        self.answers = answers
        self._counter()
        return self.scores

    def get_question(self,k):
      return self.config[k].get('text')

    def _counter(self):
        for i in range(self.length):
            qtype = self.config[i].get('qtype')
            qoptions =  self.config[i].get('options')
            right_answer =  self.config[i].get('right_answer')
            qanswer = self.answers[i]
            if qtype == 'closed':
                self.scores += 1 if qanswer == 'Да' else + 0
            if qtype == 'multiple_choice':
                pass
            if qtype == 'number':
                pass
        print(self.scores)

from app.util.responses import ButtonResponse
from app.models.do import Question
from app.enums.dao_enum import QuestionDifficulty


class UserQuizStatus:
    def __init__(self, cap, id=None, reserve_easy=None,
                 reserve_medium=None,
                 reserve_hard=None,
                 education_level=None):
        self.id = id
        self.size = 0
        self.cap = cap
        self.questions = []
        self.answer = []
        self.reserve_easy = reserve_easy
        self.reserve_medium = reserve_medium
        self.reserve_hard = reserve_hard
        self.education_level = education_level
        self.fished = False
        self.cur = -1
        self.score = 0
        if self.reserve_medium:
            self.questions.append((self.reserve_medium.pop()))

    def get_question(self) -> ButtonResponse:
        self.cur += 1
        if self.cur > self.cap - 1:
            return None
        print(self.cur,self.questions)
        question = self.questions[self.cur]
        resp = ButtonResponse(question.title + "[{}]".format(question.difficulty.value),
                              [button for button in question.choices])

        return resp

    def get_cur_question(self):
        if self.cur < 0:
            return None
        return self.questions[self.cur]

    def check(self, ans):
        if not self.questions:
            return None
        q = self.questions[self.cur]

        return (ans in q.choices) and (q.choices.index(ans) == q.answer)

    def add(self, level: QuestionDifficulty):
        if self.size + 1 > self.cap:
            raise Exception("You cannot add more question")
        self.size += 1
        if level == QuestionDifficulty.EASY:
            self.questions.append(self.reserve_easy.pop())
        elif level == QuestionDifficulty.MEDIUM:
            self.questions.append(self.reserve_medium.pop())
        elif level == QuestionDifficulty.HARD:
            self.questions.append(self.reserve_hard.pop())

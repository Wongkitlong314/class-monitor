from app.util.responses import ButtonResponse
from app.models.do import Question
from app.enums.dao_enum import QuestionDifficulty


class UserQuizStatus:
    def __init__(self, size, id=None, reserve_easy=None,
                 reserve_medium=None,
                 reserve_hard=None,
                 education_level=None):
        self.id = id
        self.size = size
        self.questions = []
        self.answer = []
        self.reserve_easy = reserve_easy
        self.reserve_medium = reserve_medium
        self.reserve_hard = reserve_hard
        self.education_level = education_level
        self.fished = False
        self.cur = -1

    def get_question(self) -> ButtonResponse:
        self.cur += 1
        if self.cur > self.size - 1:
            return None

        question = self.questions[self.cur]
        resp = ButtonResponse(question.title,
                              [button for button in question.choices])

        return resp

    def check(self, ans):
        if not self.questions:
            return None
        q = self.questions[self.cur]

        return q.choices.index(ans) == q.answer

    def add(self, level: QuestionDifficulty):
        if level == QuestionDifficulty.EASY:
            self.questions.append(self.reserve_easy.pop())
        elif level == QuestionDifficulty.MEDIUM:
            self.questions.append(self.reserve_medium.pop())
        elif level == QuestionDifficulty.HARD:
            self.questions.append(self.reserve_hard.pop())

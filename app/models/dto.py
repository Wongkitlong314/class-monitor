from app.util.responses import ButtonResponse
from app.models.do import Question


class UserQuizStatus:
    def __init__(self, id=None,reserve_easy=None,
                 reserve_medium=None,
                 reserve_hard=None,
                 education_level=None):
        self.id = id
        self.questions = []

        self.reserve_easy = reserve_easy
        self.reserve_medium = reserve_medium
        self.reserve_hard = reserve_hard
        self.education_level = education_level
        self.fished = False
        self.cur = 0

    def get_question(self) -> ButtonResponse:
        if self.cur > len(self.questions) - 1:
            return None

        question = self.questions[self.cur]
        resp = ButtonResponse(question.title,
                              [button for button in question.choices])
        self.cur += 1
        return resp

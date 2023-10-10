from app.util.responses import ButtonResponse
from app.models.do import Question


class UserQuizStatus:
    def __init__(self, id=None, questions: Question = None, education_level=None):
        self.id = id
        self.questions = questions
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

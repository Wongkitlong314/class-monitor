from app.util.responses import TextResponse
from app.models.message import Message
from app.config.variables import session
from app.enums.status_enum import StatusEnum


def start_quiz(msg: Message):
    phone = msg.fromNo
    bot = session.get(phone)
    if bot.main_status != StatusEnum.QUIZ:
        return TextResponse("Something wrong! You are not supposed to do quiz right now")

    return "test"
def cont_quiz(msg:Message):
    ...

def form_quiz(easy:int,medium:int,hard:int):
    # randomly form a quiz
    # it is not the most efficient way. will be changed in future
    ...


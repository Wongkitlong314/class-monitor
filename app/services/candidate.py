from app.services import quiz_service as quiz, role_play,writing,dashboard_service
from app.util.responses import TextResponse
from app.models.message import Message


def start_quiz(user_msg: Message):
    return quiz.start_quiz(user_msg)


def start_role_play(user_msg: Message):
    return role_play.start_role_play(user_msg)


def start_writing(user_msg: Message):
    return writing.start_writing(user_msg)


def dashboard(user_msg: Message):
    return dashboard_service.dashboard(user_msg)


def recommend(user_msg: Message):
    return TextResponse("recommend")


def talk_and_ask_english_learning_topic(userMsg):
    # dummy function
    ...


def introduce_function(userMsg):
    # dummy function
    ...
def dailyread_function(article):
    # dummy function
    ...

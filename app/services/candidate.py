from app.services import quiz_service as quiz, role_play
from app.util.responses import TextResponse
from app.models.message import Message


def start_quiz(user_msg: Message):
    return quiz.start_quiz(user_msg)


def start_role_play(user_msg: Message):
    return role_play.start_role_play(user_msg)


def start_writing(studentId):
    return TextResponse("writing mode")


def dashboard(studentId):
    return TextResponse("dashboard")


def recommend(studentId):
    return TextResponse("recommend")


def talk_english_learning_topic(userMsg):
    # dummy function
    ...


def introduce_function(userMsg):
    # dummy function
    ...

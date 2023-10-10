from app.services import quiz_service as quiz
from app.util.responses import TextResponse
from app.models.message import Message

def start_quiz(user_msg:Message ):

    return quiz.start_quiz(user_msg)


def start_role_play(studentId):
    return TextResponse("role play mode")


def start_writing(studentId):
    return TextResponse("writing mode")


def dashboard(studentId):
    return TextResponse("dashboard")


def recommend(studentId):
    return TextResponse("recommend")

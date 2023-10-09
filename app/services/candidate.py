from app.services import quiz_service as quiz
from app.utli.responses import TextResponse


def start_quiz(studentId: int):
    quiz.start_quiz(studentId)
    return 0


def start_role_play(studentId):
    return TextResponse("role play mode")


def start_writing(studentId):
    return TextResponse("writing mode")


def dashboard(studentId):
    return TextResponse("dashboard")


def recommend(studentId):
    return TextResponse("recommend")

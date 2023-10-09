from app.utli.responses import TextResponse
def start_quiz(studentId:int):
    return TextResponse("student {} starting quiz".format(studentId))
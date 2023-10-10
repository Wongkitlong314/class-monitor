from app.util.responses import TextResponse, ButtonResponse
from app.models.message import Message
from app.config.variables import session
from app.enums.status_enum import StatusEnum
from app.dao.question_mapper import QuestionDao
from app.enums.dao_enum import QuestionDifficulty
import random
from enum import Enum
from app.models.dto import UserQuizStatus

data_key = "quiz_user_quiz_status"


def start_quiz(msg: Message):
    phone = msg.fromNo
    bot = session.get(phone)
    if bot.main_status != StatusEnum.QUIZ:
        return TextResponse("Something wrong! You are not supposed to do quiz right now")
    if (not bot.inner_status == InnerStatus.DOING) and (not bot.inner_status == InnerStatus.END):
        bot.inner_status = InnerStatus.DOING
        return ButtonResponse("Enter anything to start the quiz or " +
                              "type /exit to quit",
                              ["Ok", "/exit"])
    elif bot.inner_status == InnerStatus.DOING:
        # doing quiz. iterate the questions.
        quiz = bot.data.get(data_key, form_quiz(1, 1, 1))
        resp = quiz.get_question()
        if resp:
            return resp

    return TextResponse("function developing, but at least you finished the quiz")


def form_quiz(easy: int, medium: int, hard: int) -> UserQuizStatus:
    # randomly form a quiz
    # it is not the most efficient way. will be changed in future
    easy_question = QuestionDao.get_by_difficulty(level=QuestionDifficulty.EASY)
    medium_question = QuestionDao.get_by_difficulty(level=QuestionDifficulty.MEDIUM)
    hard_question = QuestionDao.get_by_difficulty(level=QuestionDifficulty.HARD)

    easy_question = random.sample(easy_question, min(easy, len(easy_question)))
    medium_question = random.sample(medium_question, min(medium, len(medium_question)))
    hard_question = random.sample(hard_question, min(hard, len(hard_question)))
    questions = easy_question + medium_question + hard_question
    random.shuffle(questions)

    return UserQuizStatus(questions=questions)

def quiz_exit(msg: Message):
    phone = msg.fromNo
    bot = session.get(phone)
    try:
        del bot.data[data_key]
    except Exception as e:
        # todo change it to log later
        print(e)


class InnerStatus(Enum):
    DOING = 0
    END = 1

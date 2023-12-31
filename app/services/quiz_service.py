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
        if data_key not in bot.data:
            bot.data[data_key] = form_quiz(3)
        quiz = bot.data[data_key]
        resps = []
        pre_ans = msg.text
        # resp_text = ""
        if quiz.cur > -1:
            cur_question = quiz.get_cur_question()
            cur_difficulty = cur_question.difficulty
            if quiz.check(pre_ans):
                print("correct")
                # did correct
                if cur_difficulty == QuestionDifficulty.HARD:
                    resps.append(TextResponse("You did right!"))
                    # resp_text = "You did right!"
                    quiz.add(QuestionDifficulty.HARD)
                else:
                    if cur_difficulty == QuestionDifficulty.EASY:

                        quiz.add(QuestionDifficulty.MEDIUM)
                    else:
                        quiz.add(QuestionDifficulty.HARD)
                    resps.append(TextResponse("You did right!" +
                                              "Let's do more difficult question"))
                    # resp_text = "You did right!" + "Let's do more difficult question"
                quiz.score += 1
            else:
                print("wrong")
                if not cur_difficulty == QuestionDifficulty.EASY:
                    resps.append(TextResponse("Sorry you did wrongly" +
                                              "The correct answer" +
                                              " should be {}".format(cur_question.choices[cur_question.answer]) +
                                              "\nThe explanation is:\n{}".format(cur_question.explanation) +
                                              "Let's do something easier!"))
                    # resp_text = "Sorry you did wrongly" + "The correct answer" + \
                    #             " should be {}".format(cur_question.choices[cur_question.answer]) + \
                    #             "\nThe explanation is:\n{}".format(cur_question.explanation) + \
                    #             "Let's do something easier!"
                    if cur_difficulty == QuestionDifficulty.HARD:
                        quiz.add(QuestionDifficulty.MEDIUM)
                    else:
                        quiz.add(QuestionDifficulty.EASY)
                else:
                    resps.append(TextResponse("Sorry you did wrongly" +
                                              "The correct answer" +
                                              " should be {}".format(cur_question.choices[cur_question.answer]) +
                                              "\nThe explanation is:\n{}".format(cur_question.explanation)))
                    # resp_text = "Sorry you did wrongly" + \
                    #             "The correct answer" + \
                    #             " should be {}".format(cur_question.choices[cur_question.answer]) + \
                    #             "\nThe explanation is:\n{}".format(cur_question.explanation)
                    quiz.add(QuestionDifficulty.EASY)

        resp = quiz.get_question()
        resps.append(resp)


        if resp:
            # resp.set_text(resp_text + "\n\n" + resp.text)
            return resps
        else:
            bot.main_status = StatusEnum.BEGIN
            return resps[:len(resps)-1]+[TextResponse("You finished. Now you are in menu again")]

    return TextResponse("function developing, but at least you finished the quiz")


def form_quiz(n) -> UserQuizStatus:
    # randomly form a quiz
    # it is not the most efficient way. will be changed in future
    print("create a quiz")
    easy_question = QuestionDao.get_by_difficulty(level=QuestionDifficulty.EASY)
    medium_question = QuestionDao.get_by_difficulty(level=QuestionDifficulty.MEDIUM)
    hard_question = QuestionDao.get_by_difficulty(level=QuestionDifficulty.HARD)

    easy_question = random.sample(easy_question, min(n, len(easy_question)))
    medium_question = random.sample(medium_question, min(n, len(medium_question)))
    hard_question = random.sample(hard_question, min(n, len(hard_question)))

    result = UserQuizStatus(n, reserve_easy=easy_question,
                            reserve_medium=medium_question,
                            reserve_hard=hard_question)

    return result


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

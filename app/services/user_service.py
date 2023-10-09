from app.dao import user_mapper
from app.models.message import Message
from enum import Enum
from app.config.variables import session
from app.core.chatbot import Bot
from app.enums.status_enum import StatusEnum
from app.util.responses import TextResponse
from app.util.responses import ButtonResponse
from app.util.responses import ListResponse
from app.enums.dao_enum import grade
from app.models.do import User, Student


def get_all_users():
    result = user_mapper.UserDAO.get_all_users()
    # handle the result here
    return result
    ...


def get_one_user(id=1):
    result = user_mapper.UserDAO.get_one_user(id=id)
    return result


def create_user(user_msg: Message):
    phone = user_msg.fromNo
    user_bot = session.get(phone, None)
    if not user_bot:
        user_bot = Bot(id=phone, main_status=StatusEnum.CREATE,
                       inner_status=InnerStatus.BEGIN, resp=TextResponse(""))
        session[phone] = user_bot
        user_bot.data["user_info"] = User()
        user_bot.data["student_info"] = Student()
    userDO = user_bot.data["user_info"]
    studentDO = user_bot.data["student_info"]
    ans = user_msg.text
    if user_bot.inner_status == InnerStatus.BEGIN:
        # begin creating user
        begin(user_bot)

    elif user_bot.inner_status == InnerStatus.ASK_FOR_GRADE:
        # answer for previous question

        ask_for_grade(user_bot, ans, studentDO, userDO)
    elif user_bot.inner_status == InnerStatus.ASK_FOR_INTEREST:
        ask_for_interest(user_bot, ans, studentDO)

    return user_bot.resp

    ...


def begin(bot, loop_back=False):
    if not loop_back:
        bot.resp = ButtonResponse("You are new here, do you want to start a sign-up process?",
                                  ["yes", "no"])
    else:
        bot.resp = ButtonResponse("I don't understand the command" +
                                  "Do you want to start a sign-up process?",
                                  ["yes", "no"])

    bot.inner_status = InnerStatus.ASK_FOR_GRADE


def ask_for_grade(bot, pre_ans, loop_back=False):
    if not loop_back:
        if pre_ans == "yes":
            bot.resp = ListResponse("Please give me your grade leve: ",
                                    "Grade Level",
                                    [grade.p1_3.value,
                                     grade.p4_6.value,
                                     grade.s1_3.value,
                                     grade.s4_6.value,
                                     grade.u.value])
        elif pre_ans == "no":
            # do stuff when user say no
            ...
        else:
            # user does not answer in proper way
            bot.inner_status = InnerStatus.BEGIN
            begin(bot, True)
    else:
        bot.resp = ListResponse("Your choice is not in the list.\n" +
                                "Please give me your grade leve: ",
                                "Grade Level",
                                [grade.p1_3.value,
                                 grade.p4_6.value,
                                 grade.s1_3.value,
                                 grade.s4_6.value,
                                 grade.u.value])
    bot.inner_status = InnerStatus.ASK_FOR_INTEREST


def ask_for_interest(bot, pre_ans, student, loop_back=False):
    if not loop_back:
        grade_list = [grade.p1_3,
                      grade.p4_6,
                      grade.s1_3,
                      grade.s4_6,
                      grade.u]
        found = list(filter(lambda ele: pre_ans == ele.value, grade_list))
        if found:
            student.grade = found[0].name

        else:
            # choice not in list
            bot.inner_status = InnerStatus.ASK_FOR_GRADE
            ask_for_grade(bot, pre_ans, loop_back=True)
    else:
        ...


class InnerStatus(Enum):
    BEGIN = 0
    ASK_FOR_GRADE = 1
    ASK_FOR_INTEREST = 2
    ASK_FOR_ROLE = 3

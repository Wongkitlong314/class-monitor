from app.dao import user_mapper
from app.models.message import Message
from enum import Enum
from app.config.variables import session
from app.core.chatbot import Bot
from app.enums.status_enum import StatusEnum
from app.util.responses import TextResponse
from app.util.responses import ButtonResponse
from app.util.responses import ListResponse
from app.enums.dao_enum import EducationLevel, Role
from app.models.do import User, Student
from app.config.database import SessionLocal
from app.dao.user_mapper import UserDAO
from app.dao.student_mapper import StudentDAO


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
    userDO.name = user_msg.fromName
    userDO.phone = phone
    userDO.role = Role.STUDENT
    studentDO = user_bot.data["student_info"]
    ans = user_msg.text
    if user_bot.inner_status == InnerStatus.BEGIN:
        # begin creating user
        begin(user_bot)

    elif user_bot.inner_status == InnerStatus.ASK_FOR_GRADE:
        # answer for previous question

        ask_for_grade(user_bot, ans)
    elif user_bot.inner_status == InnerStatus.ASK_FOR_INTEREST:
        ask_for_interest(user_bot, ans, studentDO)
    elif user_bot.inner_status == InnerStatus.END:
        end_process(user_bot, ans, studentDO)
    db = SessionLocal()
    db.begin()
    try:

        StudentDAO.insert_student(db, studentDO)
        db.flush()
        userDO.role_id = studentDO.id
        UserDAO.insert_user(db, userDO)
    except:
        db.rollback()
    return user_bot.resp


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
            bot.resp = ListResponse("Please give me your education leve: ",
                                    "Education Level",
                                    [EducationLevel.p1_3.value,
                                     EducationLevel.p4_6.value,
                                     EducationLevel.s1_3.value,
                                     EducationLevel.s4_6.value,
                                     EducationLevel.u.value])
        elif pre_ans == "no":
            # do stuff when user say no
            ...
        else:
            # user does not answer in proper way
            bot.inner_status = InnerStatus.BEGIN
            begin(bot, True)
    else:
        bot.resp = ListResponse("Your choice is not in the list.\n" +
                                "Please give me your education level: ",
                                "Education Level",
                                [EducationLevel.p1_3.value,
                                 EducationLevel.p4_6.value,
                                 EducationLevel.s1_3.value,
                                 EducationLevel.s4_6.value,
                                 EducationLevel.u.value])
    bot.inner_status = InnerStatus.ASK_FOR_INTEREST


def ask_for_interest(bot, pre_ans, student, loop_back=False):
    if not loop_back:
        grade_list = [EducationLevel.p1_3,
                      EducationLevel.p4_6,
                      EducationLevel.s1_3,
                      EducationLevel.s4_6,
                      EducationLevel.u]
        found = list(filter(lambda ele: pre_ans == ele.value, grade_list))
        if found:
            student.grade = found[0].name
            bot.resp = ButtonResponse("Could you tell me some interests of you( separated by ',')",
                                      ["Skip"])

        else:
            # choice not in list
            bot.inner_status = InnerStatus.ASK_FOR_GRADE
            ask_for_grade(bot, pre_ans, loop_back=True)
    else:
        bot.resp = ButtonResponse("Something wrong!\n" +
                                  "Could you tell me again about some interests of you( separated by ',')",
                                  ["Skip"])

    bot.inner_status = InnerStatus.END


def end_process(bot, pre_ans: str, student):
    interest = pre_ans.split(",")

    try:
        student.interest = interest
        bot.resp = TextResponse("Your process is finished! Now you are in our menu.\n" +
                                "You can say anything to start a function.\n" +
                                "eg: Hi bot, start a quiz for me\n" +
                                "Or you can type '/help' for more information")
        bot.main_status = StatusEnum.BEGIN
        bot.inner_status = None

    except:
        bot.inner_status = InnerStatus.ASK_FOR_INTEREST
        ask_for_interest(bot, pre_ans, student, loop_back=True)


class InnerStatus(Enum):
    BEGIN = 0
    ASK_FOR_GRADE = 1
    ASK_FOR_INTEREST = 2
    END = 3

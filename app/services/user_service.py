from app.dao import user_mapper
from app.models.message import Message
from enum import Enum
from app.config.variables import session
from app.core.chatbot import Bot
from app.enums.status_enum import StatusEnum
from app.utli.responses import TextResponse


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
                       inner_status=InnerStatus.BEGIN, resp=TextResponse(""), is_waiting=0)
        session[phone] = user_bot
    ans = user_msg.text
    if user_bot.inner_status == InnerStatus.BEGIN:
        # begin creating user
        if user_bot.is_waiting:
            # answer for previous question

            if ans == "1":
                user_bot.next_stage(InnerStatus.ASK_FOR_GRADE)
                user_bot.is_waiting = 1
                user_bot.set_txt_resp("Please give me your grade level")

        else:
            user_bot.set_txt_resp("You are new here, do you want to start a sign-up process?\n" +
                                  "1 for yes other for no")
            user_bot.is_waiting = 1

    elif user_bot.inner_status == InnerStatus.ASK_FOR_GRADE:
        if user_bot.is_waiting:
            if ans:
                # store and ask next
                user_bot.next_stage(InnerStatus.ASK_FOR_INTEREST)
    return user_bot.resp

    ...


class InnerStatus(Enum):
    BEGIN = 0
    ASK_FOR_GRADE = 1
    ASK_FOR_INTEREST = 2
    ASK_FOR_ROLE = 3

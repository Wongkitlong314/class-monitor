from app.models.message import Message
from app.core.filter import *
from app.config.config import FUNCTIONS
from app.dao.user_mapper import UserDAO
from typing import Callable
from logging import getLogger
from app.core.chatbot import Bot
from app.enums.status_enum import StatusEnum
from app.services.quiz_service import quiz_exit, start_quiz
from app.services.role_play import exit_role_play

logger = getLogger('app')
from app.services import user_service
from app.config.variables import session


def dispatch(user_msg: Message):
    text = user_msg.text
    user_no = user_msg.fromNo
    logger.debug("user_no={}".format(user_no))

    bot = session.get(user_no, None)
    if not bot or bot.main_status == StatusEnum.CREATE:
        user = UserDAO.get_user_by_phone(phone=user_no)
        # if this phone doesn't exist, create the user first

        if not user:
            # create user info for the user

            return user_service.create_user(user_msg)
        else:
            # first start of the server
            bot = Bot(user_no, StatusEnum.BEGIN)
            session[user_no] = bot

    status = bot.main_status
    if text == "/exit":
        # return to begin stage and execute exit functions of each current status
        if status == StatusEnum.QUIZ:
            quiz_exit(user_msg)
        elif status == StatusEnum.ROLE_PLAYING:
            exit_role_play(user_msg)
        elif status == StatusEnum.BEGIN:
            return TextResponse("You already in the menu.")
        bot.main_status = StatusEnum.BEGIN
        return TextResponse("You've returned to the menu.")
    if status != StatusEnum.BEGIN:
        # in other process
        # execute cont. function here
        if status == StatusEnum.QUIZ:
            return start_quiz(user_msg)
        elif status == StatusEnum.ROLE_PLAYING:
            return role_play(user_msg)

    function = dispatcher(FUNCTIONS, text)

    # we got a function from function list
    if match(function, "start_quiz"):
        bot.main_status = StatusEnum.QUIZ

        return function(user_msg)
    elif match(function, "start_role_play"):
        bot.main_status = StatusEnum.ROLE_PLAYING
        return function(user_msg)
    elif match(function, "start_writing"):
        ...
    return TextResponse(function.__name__)


def match(function: Callable, name: str):
    return function.__name__ == name

from app.models.message import Message
from app.core.filter import dispatcher
from app.util.responses import TextResponse
from app.config.config import FUNCTIONS, FUNCTIONS_WITH_INTRO
from app.dao.user_mapper import UserDAO
from typing import Callable
from logging import getLogger
from app.core.chatbot import Bot
from app.enums.status_enum import StatusEnum
from app.services.quiz_service import quiz_exit, start_quiz
from app.services.role_play import exit_role_play, start_role_play
from app.services.writing import start_writing
from app.core import GPT_request
import random

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
            print("create a bot")
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
            return start_role_play(user_msg)
        elif status == StatusEnum.WRITING:
            return start_writing(user_msg)

    function = dispatcher(FUNCTIONS_WITH_INTRO, text)
    if not callable(function):
        print("no match")
        prefix = ["Sorry, let's talk some english related topic. The following is my function list:",
                  "Let's only talk learning topic. Here is my function list: ",
                  "Sorry, let's do the following:"]
        return list_function(prefix)

    # we got a function from function list
    if match(function, "start_quiz"):
        bot.main_status = StatusEnum.QUIZ

        return function(user_msg)
    elif match(function, "start_role_play"):
        bot.main_status = StatusEnum.ROLE_PLAYING
        return function(user_msg)
    elif match(function, "start_writing"):
        bot.main_status = StatusEnum.WRITING
        return function(user_msg)

    elif match(function, "talk_english_learning_topic"):
        sys_pmt = "You are a english learning assistant and a expert in education. " \
                  "Given student's message, you will give kind reply." \
                  "And try your best to guide the topic back to english learning."
        prompt = "Student message: " + user_msg.text
        response = GPT_request.get_completion(prompt=prompt, sys_prompt=sys_pmt)
        return TextResponse(response)
    elif match(function, "introduce_function"):

        return list_function(prefix=["Here is the list:",
                                     "We have following function",
                                     "Our function is following"])
    return TextResponse(function.__name__)


def match(function: Callable, name: str):
    return function.__name__ == name


def list_function(prefix=None, function_list=FUNCTIONS):
    prompt = "List all you can do without parameters nor function name? Remember! Just only provide a list"
    response = dispatcher(function_list, prompt)
    if prefix:
        i = random.randint(0, len(prefix) - 1)
        response = prefix[i] + "\n" + response

    return TextResponse(response)

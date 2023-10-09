from app.models.message import Message
from app.core.filter import *
from app.config.config import FUNCTIONS
from app.dao.user_mapper import UserDAO
from typing import Callable
from app.services.candidate import *
from logging import getLogger

logger = getLogger('app')
from app.models.user import User
from app.services import user_service




def dispatch(user_msg: Message):
    text = user_msg.text
    user_no = user_msg.fromNo
    logger.debug("user_no={}".format(user_no))
    user = UserDAO.get_user_by_phone(phone=user_no)
    # if this phone doesn't exist, create the user first

    if not user:
        # create user info for the user

        return user_service.create_user(user_msg)

        ...

    status = user.status
    function = dispatcher(FUNCTIONS, text)

    # we got a function from function list
    if match(function, "start_quiz"):

        return function(user.id)
    elif match(function, "start_role_play"):
        ...
    elif match(function, "start_writing"):
        ...
    return TextResponse(function.__name__)


def match(function: Callable, name: str):
    return function.__name__ == name


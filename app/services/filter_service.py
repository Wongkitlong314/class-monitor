from app.models.UserMessage import UserMessage
from app.core.filter import *
from app.config.config import FUNCTIONS


def dispatch(user_msg: UserMessage):
    text = user_msg.text
    user_no = user_msg.fromNo
    dispatcher(FUNCTIONS, text)
    return 0

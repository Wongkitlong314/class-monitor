from app.models.UserMessage import UserMessage
from app.core.filter import *
from app.config.config import FUNCTIONS
from app.dao.user_mapper import UserDAO

def dispatch(user_msg: UserMessage):
    text = user_msg.text
    user_no = user_msg.fromNo
    print("user_no={}".format(user_no))
    result = UserDAO.get_user_by_phone(phone=user_no)
    print("result = {}".format(result))
    dispatcher(FUNCTIONS, text)
    return 0

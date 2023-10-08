from ..dao import user_mapper
def get_all_users():
    result = user_mapper.UserDAO.get_all_users()
    # handle the result here
    return result
    ...    
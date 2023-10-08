from app.dao import user_mapper
def get_all_users():
    result = user_mapper.UserDAO.get_all_users()
    # handle the result here
    return result
    ...    

def get_one_user(id=1):
    result = user_mapper.UserDAO.get_one_user(id=id)
    return result
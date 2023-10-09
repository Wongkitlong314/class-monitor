from app.dao import student_mapper
def get_all_student():
    result = student_mapper.StudentDAO.get_all_users()
    # handle the result here
    return result

def get_user_interest():
    pass

def get_user_grade():
    pass


def role_play(msg):
    stu_grade = get_user_grade()
    stu_interest = get_user_interest()
    # 查看用户是否在对话状态
    # 没有
        # while True:
            # 根据用户的level, grade, interest生成prompt，提交到chatgpt 生成对话场景
            # 场景包含 scenario, backgroud, them,roles
            # 询问学生是否满意
            # If 满意
                # 询问学生扮演的角色
                # break；
    # 记录 开始对话 =场景+学生角色+（你先开始，只说你扮演角色的台词，然后等待我的回复） send to chatgpt return to student
    # begin converstation
        # sent chatgpt_msg to student
        # sent student msg to chatgpt 开始对话+之前对话



if __name__=="__main__":
    print(get_all_student()[0])
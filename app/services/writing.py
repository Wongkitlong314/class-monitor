from app.dao import student_mapper
from app.dao import user_mapper
from app.util import prompt
from app.core.GPT_call_fun import get_completion
from app.util.responses import TextResponse
from app.config.variables import session

class Bot:
    def __init__(self, id, data=dict()):
        self.id = id
        self.data = data

# 退出role_play，删掉聊天记录，提示用户role-play结束
def exit_writing(user_msg):
    user_bot = session[user_msg.fromNo]
    del user_bot.data['writing_msg']
    return TextResponse('Writing ends. Thank you!')

# 传入用户消息类，用户bot，用户id（电话号码）
# 返回chatgpt的回复：response 类

def start_writing(user_msg):
    user_bot = session[user_msg.fromNo]
    user_phone = user_msg.fromNo
    if not user_bot:
        user_bot = Bot(id=user_phone)
        session[user_phone] = user_bot
    user_msg_txt = user_msg.text
    writing_task_description = prompt.PromptConstructor('app/prompt_templates/writing_prompt.txt').get()
    stu_id = user_mapper.UserDAO.get_user_by_phone(phone=user_phone).role_id
    stu = student_mapper.StudentDAO.get_student_by_id(id=stu_id)
    try:
        stu_edu_level = stu.education_level.value
    except:
        stu_edu_level = 'Secondary 4 - 6'
    if 'writing_msg' not in user_bot.data:
        messages = [
            {"role": "system", "content": writing_task_description},
            {"role": "user", "content": "My Education level is: %s " % (stu_edu_level)},
            {"role": "user", "content": "please start by introducing what you can do."}
        ]
        chat_response = get_completion(messages,temperature=0)
        # 存储chatgpt的回复
        messages.append({"role": "system", "content": chat_response})
        user_bot.data['writing_msg'] = messages
        return TextResponse(chat_response)

    else:
        # 获取user的之前role play的message
        messages = user_bot.data['writing_msg']

        # 存储用户的回复
        messages.append({"role": "user", "content": user_msg_txt})
        user_bot.data['writing_msg'] = messages

        # 存储用户回复后，发给chatgpt
        messages = user_bot.data['writing_msg']
        chat_response = get_completion(messages,temperature=0)

        # 存储chatgpt的回复
        messages.append({"role": "system", "content": chat_response})

        # 更新内存中的message
        user_bot.data['writing_msg'] = messages

        # 返回chatgpt对话：string
        return TextResponse(chat_response)

if __name__ == "__main__":
    # stu = student_mapper.StudentDAO.get_student_by_id(id=1)
    # stu_interest =', '.join(stu.interest)
    # stu_edu_level = stu.education_level.value
    # print(status_enum.StatusEnum.ROLE_PLAYING.value)
    stu_id = user_mapper.UserDAO.get_user_by_phone(phone='85253640135').role_id
    stu = student_mapper.StudentDAO.get_student_by_id(id=stu_id)
    stu_interest = ', '.join(stu.interest)
    stu_edu_level = stu.education_level.value
    writing_task_description = prompt.PromptConstructor('../prompt_templates/writing_prompt.txt').get()
    messages = [
        {"role": "system", "content": writing_task_description},
        {"role": "user", "content": "My Education level is: %s " % (stu_edu_level)},
        {"role": "user", "content": "please start by introducing what you can do."}
         ]

    chat_response = get_completion(messages, temperature=0)
    print(chat_response)
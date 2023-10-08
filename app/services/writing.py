import os 
import openai 
import time
import json

openai.api_key = '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'

def _get_student_profile(student_id):
    name = 'Peter'
    student_id = '123'
    grade = 'primary 6'
    level = 'medium'
    interest = 'football'
    return name, student_id, grade, level, interest

def _get_writing_qustion(grade, level, interest):
    question = 'A happy day'
    return question 

writing_comment_functions = [
    {
        "name": "grading_student_writing",
        "description": """You are an English teacher. 
        Generate fair feedback and reviews for student writing.
            Rate the writing in these aspects:
            - Content and Relevance
            - Organization and Structure
            - Grammar and Mechanics
            - Vocabulary and Word Choice
            - Clarity and Cohesion
            
            For each aspect, score it on a scale of 0 to 5. 
            The format should be "score/5". 
            Provide precise and concise explanations for your ratings. 
            Students may ask you to explain your ratings and comments.
            """,
            
        "parameters": {
            "type": "object",
            "description": "Comment and score for student writing.",
            "properties": {
                "comment": {
                    "type": "string",
                    "description": "Comment and score for student writing. Should have around 200 words"
                    
                }
            }
        },
        "required": ["comment"]
    }
]

writing_task_description = """you are a english teacher. student will ask you question related to the writing. 
    if it is not related to english, ask them to ask again. 
    if they have further question, please answer them. 
    Student will also submit their writing, please score them and give feedback base on their grade.
    No need call function unless student send you passage.
    student may update their writing submission. If they upload a new one, please rate and focus on the new one. 
    """

messages=[
        {"role": "system", "content": writing_task_description}, 
        {"role": "user", "content": "The grade of the student: %s " %(grade)},
        {"role": "user", "content": "please start by introducing what you can do."}]

while True:    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    max_tokens=1000,
    temperature = 0,
    functions=writing_comment_functions,
    function_call="auto"
    )
    
    if completion.choices[0].message.get("function_call"):
        chat_response = json.loads(completion.choices[0].message['function_call']['arguments'])['comment']
        print(f'ChatGPT: {chat_response}')
    else:
        chat_response = completion.choices[0].message.content
        print(f'ChatGPT: {chat_response}')
        
    messages.append({"role": "assistant", "content": chat_response})
    
    content = input("User: ")
    messages.append({"role": "user", "content": content})
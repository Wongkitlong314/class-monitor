import openai
import time
openai.api_key = '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'

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

def get_completion(messages, model="gpt-3.5-turbo", temperature=0):
    response = ''
    except_waiting_time = 0.1
    while response == '':
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature,
                request_timeout=50,
                functions = writing_comment_functions,
                function_call = "auto"
            )
        except Exception as e:
            time.sleep(except_waiting_time)
            if except_waiting_time < 2:
                except_waiting_time *= 2
    return response.choices[0].message["content"]
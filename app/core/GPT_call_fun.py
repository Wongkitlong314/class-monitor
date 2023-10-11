import openai
import time
openai.api_key = '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'

def get_completion(messages, model="gpt-3.5-turbo-0613", fun=None,temperature=0):
    response = ''
    except_waiting_time = 0.1
    while response == '':
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature,
                request_timeout=50,
                functions=fun,
                function_call="auto"
            )
        except Exception as e:
            time.sleep(except_waiting_time)
            if except_waiting_time < 2:
                except_waiting_time *= 2
    return response.choices[0].message["content"]
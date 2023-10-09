import openai
import json
from app.utli.responses import TextResponse
from app.services.quiz_service import start_quiz
import asyncio

openai.api_key = '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'
# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)



def start_role_play(studentId):
    return TextResponse("role play mode")

def start_writing(studentId):
    return TextResponse("writing mode")

def dashboard(studentId):
    return TextResponse("dashboard")

def recommend(studentId):
    return TextResponse("recommend")


def dispatcher(functions, prompt,):
    # Step 1: send the conversation and available functions to GPT
    messages = [{"role": "user", "content": prompt}]
    functions = functions
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]
    print(response_message)

    # Step 2: check if GPT wanted to call a function
    if response_message.get("function_call"):
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "start_quiz": start_quiz,
            "start_role_play": start_role_play,
            "start_writing": start_writing,
            "dashboard": dashboard,
            "recommend": recommend,
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]


        function_to_call = available_functions[function_name]
        print(function_to_call)
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = function_to_call(
            studentId=1,
            # userId="userId"
        )
        # print(function_response)
        # function_response.send()

        # # Step 4: send the info on the function call and function response to GPT

        return function_response
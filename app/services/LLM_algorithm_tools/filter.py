import openai
import json
from app.utli.responses import TextResponse
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


def start_quiz(studentId):
    return TextResponse("start quiz mode")

def start_role_play(studentId):
    return TextResponse("role play mode")

def start_writing(studentId):
    return TextResponse("writing mode")

def dashboard(studentId):
    return TextResponse("dashboard")

def recommend(studentId):
    return TextResponse("recommend")


functions = [
        {   
            "id":0,
            "name": "start_quiz",
            "parameters": {
                "type": "object",
                "properties": {
                    "studentId": {
                        "type": "string",
                        # "description": "The city and state, e.g. San Francisco, CA",
                    },
                    # "quiz_id": {
                    #     "type": "string",
                    # },

                    # "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                # "required": ["location"],
            },
            "description":"This is a functions that starts a quiz session for student with the student id in params"
        },
        {
            "id":1,
            "name": "start_role_play",
            "parameters": {
                "type": "object",
                "properties": {
                    "studentId": {
                        "type": "string",
                    },
                },
            },
            "description":"This is a functions that starts a role-play session for student"   
        },
        {
            "id":2,
            "name": "start_writing",
            "parameters": {
                "type": "object",
                "properties": {
                    "studentId": {
                        "type": "string",
                    },
                    # "quiz_id": {
                    #     "type": "string",
                    # },
                },
            },
            "description":"This is a functions that allows student to write with ai"

        },
        {
            "id":3,
            "name": "dashboard",
            "parameters": {
                "type": "object",
                "properties": {
                    "studentId": {
                        "type": "string",
                    },
                },
            },
            "description":"this function allows the user to check the data in dashboard"

        },
        {
            "id":4,
            "name": "recommend",
            "parameters": {
                "type": "object",
                "properties": {
                    "studentId": {
                        "type": "string",
                    },
                },
            },
            "description":"this function makes the system to recommend studying material for student, eg news, readings, listenings"

        }
]

def run_conversation(functions, prompt):
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
            studentId="123",
            # userId="userId"
        )
        # print(function_response)
        asyncio.run(function_response.send())

        # # Step 4: send the info on the function call and function response to GPT
        # messages.append(response_message)  # extend conversation with assistant's reply
        # messages.append(
        #     {
        #         "role": "function",
        #         "name": function_name,
        #         "content": function_response,
        #     }
        # )  # extend conversation with function response
        # second_response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo-0613",
        #     messages=messages,
        # )  # get a new response from GPT where it can see the function response
        return function_response
    
prompt = "i want do some quiz"
run_conversation(functions, prompt)
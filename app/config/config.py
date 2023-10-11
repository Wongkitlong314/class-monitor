DATABASE_URL = "sg-cdb-30q84dwv.sql.tencentcdb.com"
DATABASE_PORT = 63957
DATABASE_USER = "root"
DATABASE_PASSWORD = "classmonitor111"
ACCESSTOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJZCI6Ijg1N2VmM2RiLWQ3ZjAtNDJkZC1hZDIwLWFkZWUzMTMyNjBlNiIsImNvdW50cnlDb2RlIjoiIiwiZW1haWwiOiJUZWFtMTJAYWRhLWFzaWEuY29tIiwiZXhwIjoyMzI4MDAyNjE2LCJpYXQiOjE2OTY4NTA2MTYsIm5hbWUiOiJhZGEgMTIiLCJyb2xlQ29kZSI6Ik9XTkVSIiwicm9sZUlkIjoiT1dORVIiLCJzaWQiOiJhcGlrZXkiLCJzdHlwZSI6InVzZXIiLCJ1aWQiOiIwNWVkODY4Mi00YjQzLTQxMTItODc0Ni0wYTljZDFjMmQ1ZjMifQ.Uw2wZsdrM4JyRaxBs51jS4TqMn02zlkNzAMaxUsM-vg"
BASEURL = "https://bizmsgapi.ada-asia.com/prod"
BUSSINESS = "60136951322"
RECIPIENT = "6583869990"
OPENAI_API_KEY = "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"
DASHBOARD_MODEL= "gpt3.5-turbo-0613"
FUNCTIONS = [
    {
        "id": 0,
        "name": "start_quiz",
        "parameters": {
            "type": "object",
            "properties": {
                "studentId": {
                    "type": "number",
                    # "description": "The city and state, e.g. San Francisco, CA",
                },
                # "quiz_id": {
                #     "type": "string",
                # },

                # "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            # "required": ["location"],
        },
        "description": "This is a functions that starts a quiz session for student with the student id in params"
    },
    {
        "id": 1,
        "name": "start_role_play",
        "parameters": {
            "type": "object",
            "properties": {
                "studentId": {
                    "type": "string",
                },
            },
        },
        "description": "This is a functions that starts a role-play session for student"
    },
    {
        "id": 2,
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
        "description": "This is a functions that allows student to write with ai"

    },
    {
        "id": 3,
        "name": "dashboard",
        "parameters": {
            "type": "object",
            "properties": {
                "studentId": {
                    "type": "string",
                },
            },
        },
        "description": "this function allows the user to check the data in dashboard"

    },
    {
        "id": 4,
        "name": "recommend",
        "parameters": {
            "type": "object",
            "properties": {
                "studentId": {
                    "type": "string",
                },
            },
        },
        "description": "this function makes the system to recommend studying material for student, eg news, readings, listenings"

    },
    {
        "id": 5,
        "name": "talk_english_learning_topic",
        "parameters": {
            "type": "object",
            "properties": {
                "userMsg": {
                    "type": "string",
                },
            },
        },
        "description": "This function allow student to experience communication with our advanced AI, " +
                       "especially in english learning topic"

    },

]
FUNCTIONS_WITH_INTRO = FUNCTIONS + [{
    "id": 6,
    "name": "introduce_function",
    "parameters": {
        "type": "object",
        "properties": {
            "userMsg": {
                "type": "string",
            },
        },
    },
    "description": "This function will introduce all functions of the system"

}]

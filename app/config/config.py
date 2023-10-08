DATABASE_URL = "sg-cdb-30q84dwv.sql.tencentcdb.com"
DATABASE_PORT = 63957
DATABASE_USER = "root"
DATABASE_PASSWORD = "classmonitor111"
ACCESSTOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJZCI6Ijg1N2VmM2RiLWQ3ZjAtNDJkZC1hZDIwLWFkZWUzMTMyNjBlNiIsImNvdW50cnlDb2RlIjoiIiwiZW1haWwiOiJ0ZWFtMTJAYWRhLWFzaWEuY29tIiwiZXhwIjoyMzI3OTIwMjYwLCJpYXQiOjE2OTY3NjgyNjAsIm5hbWUiOiJBREEgMTIiLCJyb2xlQ29kZSI6Ik9XTkVSIiwicm9sZUlkIjoiT1dORVIiLCJzaWQiOiJhcGlrZXkiLCJzdHlwZSI6InVzZXIiLCJ1aWQiOiI2NmQ3YTIzMC00NzQ4LTQyMjMtYTNiYi1lNjE4ZGI2OGQ4Y2UifQ.r_8z7C6VdlE4xEXvSEOzZ1kzBqHFNgbxBDwlDG_pIkE"
BASEURL = "https://bizmsgapi.ada-asia.com/prod"
BUSSINESS = "60136951322"
RECIPIENT = "6583869990"
FUNCTIONS = [
        {
            "id":0,
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
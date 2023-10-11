DATABASE_URL = "sg-cdb-30q84dwv.sql.tencentcdb.com"
DATABASE_PORT = 63957
DATABASE_USER = "root"
DATABASE_PASSWORD = "classmonitor111"
ACCESSTOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJZCI6Ijg1N2VmM2RiLWQ3ZjAtNDJkZC1hZDIwLWFkZWUzMTMyNjBlNiIsImNvdW50cnlDb2RlIjoiIiwiZW1haWwiOiJUZWFtMTJAYWRhLWFzaWEuY29tIiwiZXhwIjoyMzI4MDAyNjE2LCJpYXQiOjE2OTY4NTA2MTYsIm5hbWUiOiJhZGEgMTIiLCJyb2xlQ29kZSI6Ik9XTkVSIiwicm9sZUlkIjoiT1dORVIiLCJzaWQiOiJhcGlrZXkiLCJzdHlwZSI6InVzZXIiLCJ1aWQiOiIwNWVkODY4Mi00YjQzLTQxMTItODc0Ni0wYTljZDFjMmQ1ZjMifQ.Uw2wZsdrM4JyRaxBs51jS4TqMn02zlkNzAMaxUsM-vg"
BASEURL = "https://bizmsgapi.ada-asia.com/prod"
BUSSINESS = "60136951322"
RECIPIENT = "6588298542"
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
CHARTS = [
        {
            "id":0,
            "name": "Bar_Chart",
            "parameters": {
                "type": "object",
                "properties": {
                    "labels": {
                        "type": "string",
                        "description": "A label for the dataset which appears in the legend and tooltips, mostly time related",
                    },
                    "datasets": {
                        "type": "array",
                        "type": "string",
                        "description": "An array of numbers representing the data values for the corresponding labels.",
                    },
                },
                "required": ["labels", "datasets"],
            },
            "description":"A bar chart provides a visual representation of categorical data with rectangular bars where the lengths are proportional to the values they represent. It can be used to compare different categories of data."
        },
        {
            "id": 1,
            "name": "Line_Chart",
            "parameters": {
                "type": "object",
                "properties": {
                    "labels": {
                        "type": "string",
                        "description": "A label for the dataset which appears in the legend and tooltips, typically time or categorical data points.",
                    },
                    "datasets": {
                        "type": "array",
                        "type": "string",
                        "description": "An array of numbers representing the data values plotted against the corresponding labels.",
                    }
                },
                "required": ["labels", "datasets"],
            },
            "description": "A line chart displays information as a series of data points connected by straight line segments. It's often used to visualize a trend in data over intervals of time."
        },
        {
            "id": 2,
            "name": "Pie_Chart",
            "parameters": {
                "type": "object",
                "properties": {
                    "labels": {
                        "type": "string",
                        "description": "A label for the dataset which appears in the legend and tooltips, representing distinct categories.",
                    },
                    "datasets": {
                        "type": "array",
                        "type": "string",
                        "description": "An array of numbers indicating the proportion of each segment in the pie."
                    }
                },
                "required": ["labels", "datasets"],
            },
            "description": "A pie chart is a circular statistical graphic divided into slices to illustrate numerical proportion. Each slice corresponds to a category and its size is proportional to its value."
        },
        {
            "id": 3,
            "name": "Radar_Chart",
            "parameters": {
                "type": "object",
                "properties": {
                    "labels": {
                        "type": "string",
                        "description": "A label for the dataset which appears in the legend and tooltips, representing different metrics or criteria.",
                    },
                    "datasets": {
                        "type": "string",
                        "description": "An array of numbers showing the performance or value for each criterion on the radar."
                    }
                },
                "required": ["labels", "datasets"],
            },
            "description": "A radar chart is a graphical method of displaying multivariate data in the form of a two-dimensional chart, representing three or more quantitative variables on axes starting from the same point."
        },
        {
            "id": 4,
            "name": "Scatter_Chart",
            "parameters": {
                "type": "object",
                "properties": {
                    "labels": {
                        "type": "string",
                        "description": "A label for the dataset which appears in the legend and tooltips, typically representing individual data points.",
                    },
                    "datasets": {
                        "type": "string",
                        "description": "An array of numbers which are plotted to represent the relationship between two variables."
                    }
                },
                "required": ["labels", "datasets"],
            },
            "description": "A scatter chart uses dots to represent values for two different variables. The position of each dot represents its value for those two variables."
        }

]

CHARTS_CONFIGS = [
    {
        "type": "bar",
        "data": {
            "labels": [],
            "datasets": []
        }
    },
    {
        "type": "line",
        "data": {
            "labels": [],
            "datasets": []
        }
    },
    {
        "type": "pie",
        "data": {
            "labels": [],
            "datasets": []
        }
    },
    {
        "type": "radar",
        "data": {
            "labels": [],
            "datasets": []
        }
    },
    {
        "type": "scatter",
        "data": {
            "datasets": []
        }
    }
]

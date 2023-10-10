from langchain.agents import AgentType, create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain.chat_models import ChatOpenAI
from sqlalchemy import create_engine
from app.config.database import engine
from app.config.config import DASHBOARD_MODEL, OPENAI_API_KEY
import os
# os.environ["OPENAI_API_TYPE"]="open_ai"
# os.environ["OPENAI_API_VERSION"]="2020-11-07"
# os.environ["OPENAI_API_BASE"]="https://api.openai.com/v1" # Your Azure OpenAI resource endpoint
os.environ["OPENAI_API_KEY"]=OPENAI_API_KEY # Your Azure OpenAI resource key
os.environ["OPENAI_CHAT_MODEL"]="gpt-3.5-turbo-16k-0613" # Use name of deployment

llm = ChatOpenAI(model=os.getenv("OPENAI_CHAT_MODEL"),
                      temperature=0)

db = SQLDatabase(engine)
from langchain.prompts.chat import ChatPromptTemplate

final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", 
         """
          You are a helpful AI assistant expert in querying SQL Database to find answers to user's question about Students, Teachers and Homeworks.
         """
         ),
        ("user", "{question}\n ai: "),
    ]
)
sql_toolkit = SQLDatabaseToolkit(db=db, llm=llm, handle_parsing_errors="Check your output and make sure it conforms!")
sql_toolkit.get_tools()

sqldb_agent = create_sql_agent(
    llm=llm,
    toolkit=sql_toolkit,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    agent_executor_kwargs={"handle_parsing_errors": True},
    verbose=True,
)

res = sqldb_agent.run(final_prompt.format(
        question="What were my students' interest recently?"
  ))
print(res)
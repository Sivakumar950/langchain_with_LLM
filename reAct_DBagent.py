from langchain_community.utilities import SQLDatabase
sql_db= SQLDatabase.from_uri("sqlite:///salesDB/sales.db")

from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)

from langchain_community.agent_toolkits import SQLDatabaseToolkit

toolkit=SQLDatabaseToolkit(db=sql_db, llm=llm)
toolkit.get_tools()

from langchain.agents import create_agent

agent= create_agent(llm, toolkit.get_tools())
graph = agent.get_graph()
graph.print_ascii()

question="What is the total sales of monitor?"

for step in agent.stream({"messages": ({"role":"user", "content": question})}, stream_mode="values"):
    step["messages"][-1].pretty_print()

response=llm.invoke(question)
print(response.content)
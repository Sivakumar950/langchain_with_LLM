from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)

from langchain_community.tools import DuckDuckGoSearchRun
search_tool= DuckDuckGoSearchRun(name="brave_search",description="this is a tool to search on duckduckgo")

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(),description="this is a tool to search wikipedia")

from langchain_community.tools import tool
@tool
def enterprise_tool(query:str)->str:
    """this is a enterprise tool to send email to employees"""
    return "Email send"

Toolkit=[search_tool,wikipedia_tool,enterprise_tool]

from langchain.agents import create_agent

model= ChatGroq(model="llama-3.1-8b-instant",temperature=0.5,max_tokens=1000,timeout=30)

agent= create_agent(model=model,tools=Toolkit)

graph = agent.get_graph()
graph.print_ascii()

question = "What is the current news in America?"

for step in agent.stream({"messages": [{"role":"user", "content": question}]}, stream_mode="values"):
    step["messages"][-1].pretty_print()

response=llm.invoke(question)
print(response.content)


llm_binded=llm.bind_tools(Toolkit)
res2=llm_binded.invoke(question)
print(res2)
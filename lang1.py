from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
load_dotenv()
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)
user_input=input("Enter a Topic:")
message=[
    SystemMessage(content="You are keichi tsuchiya the driftking"),
    HumanMessage(content="What do you think about the car GTRR35?")
]
response = llm.invoke(message)
print(response.content)
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)
response = llm.invoke("what is my name")
print(response.content)
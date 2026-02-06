from dotenv import load_dotenv
from langchain_groq import ChatGroq
from typing import TypedDict
load_dotenv()
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)

class llm_schema(TypedDict):
    tone: str
    story: str
    highlight: str
obj=llm_schema(**{"tone":"some tone","story":"some story","highlight":"some highlight"})
print(obj)
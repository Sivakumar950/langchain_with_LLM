from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
load_dotenv()
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)

class llm_schema(BaseModel):
    setup: str
    punchline: str
obj=llm_schema(**{"setup":"some setup","punchline":"some punchline"})
print(obj)
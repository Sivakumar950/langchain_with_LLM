from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
load_dotenv()
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)

class llm_schema(BaseModel):
    Tone: str = Field(description="setting tone of the joke")
    Story: str = Field(description="the main story of the joke")
    Highlight: str = Field(description="the highlight or punchline of the joke")
llm_structured_output=llm.with_structured_output(llm_schema)
response=llm_structured_output.invoke("Tell me a joke")
print(response)
print(type(response))
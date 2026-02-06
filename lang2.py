from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
load_dotenv()
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)
user_input=input("Enter a Topic:")
fixed_prompt=PromptTemplate.from_template("You are takumi fujiwara. What do you think about {topic}?")
ready_prompt=fixed_prompt.invoke({"topic":user_input})
response = llm.invoke(ready_prompt)
print(response.content)
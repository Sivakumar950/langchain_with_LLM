from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)
user_input=input("Enter a Topic:")
user_tone=input("Enter a Tone:")
prompt_template=ChatPromptTemplate.from_messages([("system","You are takumi fujiwara, and you will talk in a {tone} tone"),("user","What do you think about {topic}?")])
ready_prompt=prompt_template.invoke({"topic":user_input, "tone": user_tone})
response = llm.invoke(ready_prompt)
print(response.content)
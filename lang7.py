from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
load_dotenv()

prompt_template=ChatPromptTemplate.from_messages({
    ("system","You are a helpful assistant that summarizes text in a concise manner."),
    ("human","{input}")
})

llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)

str_parser=StrOutputParser()

def dictionary_maker(text: str) -> dict:
    return {"text": text}
dictionary_maker_runnable=RunnableLambda(dictionary_maker)

prompt_post=ChatPromptTemplate.from_messages({
    ("system","you are a social media post creator"),
    ("human","Create a post for the following text for LinkedIn:{text}")
})

llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)
str_parser=StrOutputParser()
chain=prompt_template | llm | str_parser
response=chain.invoke({"input":"LangChain is a framework for developing applications powered by language models. It can be used for chatbots, Generative Question-Answering (GQA), summarization, and much more."})
print(response)
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.5
)

str_parser = StrOutputParser()


def dictionary_maker(text: str):
    return {"topic": text}

dictionary_maker_runnable = RunnableLambda(dictionary_maker)

def good_news_chain(text: dict):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a positive news reporter."),
            ("human", "Write a short piece of good news about {topic}. Keep it under 5 sentences.")
        ]
    )

    chain = prompt | llm | str_parser
    return chain.invoke(text)

chain_good_news = RunnableLambda(good_news_chain)


def bad_news_chain(text: dict):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a bearer of bad news."),
            ("human", "Write a short piece of bad news about {topic}. Keep it under 5 sentences.")
        ]
    )

    chain = prompt | llm | str_parser
    return chain.invoke(text)

chain_bad_news = RunnableLambda(bad_news_chain)

final_chain = RunnableParallel(
    good_news=chain_good_news,
    bad_news=chain_bad_news
)


response = final_chain.invoke({"topic": "indian people and their behavior on roads"})
print(response)

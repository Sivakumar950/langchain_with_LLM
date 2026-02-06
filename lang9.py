from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel
)

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.5
)

str_parser = StrOutputParser()


def dictionary_maker(text: str):
    return {"topic": text}

dictionary_maker_runnable = RunnableLambda(dictionary_maker)

def linkedin_chain(text: dict):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a professional LinkedIn content writer."),
            ("human", "Write a thoughtful LinkedIn post about {topic}. Keep it under 5 sentences.")
        ]
    )

    chain = prompt | llm | str_parser
    return chain.invoke(text)

chain_linkedIn = RunnableLambda(linkedin_chain)


def insta_chain(text: dict):
    insta_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a concise horror storyteller."),
            ("human", "Tell me a horror story about {topic} in the most hilarious manner. Keep it under 10 sentences.")
        ]
    )

    chain_insta = insta_prompt | llm | str_parser
    return chain_insta.invoke(text)

insta_chain_runnable = RunnableLambda(insta_chain)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("human", "{topic}")
    ]
)

final_chain = (
    prompt_template
    | llm
    | str_parser
    | dictionary_maker_runnable
    | RunnableParallel(
        linkedin=chain_linkedIn,
        instagram=insta_chain_runnable
    )
)


if __name__ == "__main__":
    response = final_chain.invoke({"topic": "KGF"})
    print(response)
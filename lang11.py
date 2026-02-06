from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableBranch
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq

llm=ChatGroq(
    model="llama-3.1-8b-instant",temperature=0.5
)
str_parser = StrOutputParser()

classifier_prompt=ChatPromptTemplate.from_messages([
    ("system","Answer only POSITIVE OR NEGATIVE"),
    ("human","{text}")
])

classifier_chain=classifier_prompt | llm | str_parser

def classify(text:str):
    sentiment=classifier_chain.invoke({"text":text}).strip().upper()
    return{
        "text":text,
        "sentiment":sentiment
    }

classify_runnable=RunnableLambda(classify)

positive_chain=RunnableLambda(
    lambda x: f"POSITIVE REVIEW: {x['text']}"
)

negative_chain=RunnableLambda(
    lambda x: f"NEGATIVE REVIEW: {x['text']}"
)

conditional_chain=RunnableBranch(
    (lambda x: x["sentiment"]=="POSITIVE",positive_chain),
    (lambda x: x["sentiment"]=="NEGATIVE",negative_chain),
    RunnableLambda(lambda x: "Unknown Sentiment")
)

final_chain=classify_runnable | conditional_chain

print(final_chain.invoke("The product quality is excellent and I am very satisfied with my purchase."))
print(final_chain.invoke("The service was terrible and I will not be coming back."))
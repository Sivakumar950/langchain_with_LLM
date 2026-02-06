from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.5)

# Chain 1: Good News
prompt_good = ChatPromptTemplate.from_template("Tell me some good news about {topic}")
chain_good = prompt_good | llm | StrOutputParser()

# Chain 2: Bad News
prompt_bad = ChatPromptTemplate.from_template("Tell me some bad news about {topic}")
chain_bad = prompt_bad | llm | StrOutputParser()

# Runnable Parallel
parallel_chain = RunnableParallel(
    good_news=chain_good,
    bad_news=chain_bad
)

# Runnable Lambda to combine
def combine_results(inputs):
    return f"--- Good News ---\n{inputs['good_news']}\n\n--- Bad News ---\n{inputs['bad_news']}"

combine_lambda = RunnableLambda(combine_results)

# Runnable Sequence (using pipe operator | which creates a RunnableSequence)
final_chain = parallel_chain | combine_lambda

response = final_chain.invoke({"topic": "AI technology"})
print(response)

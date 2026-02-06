from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1/")

response = client.chat.completions.create(
    model="google/gemma-3-4b-it",
    messages=[
        {
            "role": "user",
            "content": "Tell me an inspirational quote.",
        }
    ],
    temperature=0.7,
)
print(response.choices[0].message.content)
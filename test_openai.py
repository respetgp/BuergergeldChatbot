import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Ты помощник."},
        {"role": "user", "content": "Привет, в чем моя проблема с письмом?"},
    ]
)

print(response.choices[0].message.content)
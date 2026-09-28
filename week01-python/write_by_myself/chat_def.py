import os
from openai import OpenAI

def chat(text):
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        return False

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com"
    )

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role":"user","content":text}
        ],
    )
    return response.choices[0].message.content


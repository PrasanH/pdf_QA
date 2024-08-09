import os
import openai
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

load_dotenv(r'.\project\.env')

my_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key = my_api_key)

messages = [
    {
        "role": "system",
        "content": "You are a Intelligent assistant who is good at explaining things in a simple way",
    },
]

models = ["gpt-3.5-turbo", "gpt-4-turbo", "gpt-4o", "gpt-4o-mini"]
model = models[3]
print('Interacting with', model)

while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = client.chat.completions.create(model=model, messages=messages)

    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})

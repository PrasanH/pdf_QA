import os
import openai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


messages = [
    {
        "role": "system",
        "content": "You are a Intelligent assistant who is good at explaining things in a simple way",
    },
]

models = ["gpt-3.5-turbo", "gpt-4-turbo", "gpt-4o"]
model = models[0]

while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(model=model, messages=messages)

    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})

import os
import openai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


st.set_page_config(page_title="Chat with JARVIS", page_icon=":robot_face:")

st.header(":robot_face: Chat with JARVIS")


pre_defined_content = [
    "You are an Intelligent assistant who is good at explaining things in a simple way",
    "You are an Intelligent assistant who is good at programming",
    "You are the most intelligent assistant who can solve anything",
]

my_content = st.selectbox(
    label=" :red[Content]",
    options=pre_defined_content,
)
with st.expander(label="Type your content if needed", expanded=False):
    typed_content = st.text_input("type your content")

if typed_content:
    my_content = typed_content

messages = [
    {
        "role": "system",
        "content": my_content,
    },
]
model = st.selectbox(
    label="Select model",
    options=["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo", "gpt-4-turbo"],
)


question = st.text_input(":red[Type your question]")
message = f"User : {question}"
if message:
    messages.append(
        {"role": "user", "content": message},
    )
chat = openai.ChatCompletion.create(model=model, messages=messages)
reply = chat.choices[0].message.content
if reply:
    st.write(f":robot_face:  {reply}")
print(f"JARVIS: {reply}")
messages.append({"role": "assistant", "content": reply})

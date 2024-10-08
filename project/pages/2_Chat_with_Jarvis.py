import os
import openai
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

load_dotenv()

my_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key = my_api_key)


st.set_page_config(page_title="Chat with JARVIS", page_icon=":robot_face:")

st.header(":robot_face: Chat with JARVIS")

if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


pre_defined_content = [
    "You are an Intelligent assistant who is good at explaining things in a simple way",
    "You are an Intelligent assistant who is good at programming",
    "You are the most intelligent assistant who can solve anything",
    "answer in minimum words as possible",
    "answer in minimum words as possible with reasoning",
]

my_content = st.selectbox(
    label=" :red[Content]",
    options=pre_defined_content,
)
with st.expander(label="Type your content if needed", expanded=False):
    typed_content = st.text_input("type your content")

if typed_content:
    my_content = typed_content


st.session_state.chat_history.append(
    {
        "role": "system",
        "content": my_content,
    },
)
model = st.selectbox(
    label="Select model",
    options=["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo", "gpt-4-turbo"],
    index = 1,
)


question = st.text_input(":red[Type your question]")
message = f"User : {question}"
if message:
    st.session_state.chat_history.append(
        {"role": "user", "content": message},
    )
    chat = client.chat.completions.create(model=model, messages=st.session_state.chat_history)

    reply = chat.choices[0].message.content

    if reply:
        st.write(f":robot_face:  {reply}")
    print(f"JARVIS: {reply}")
    st.session_state.chat_history.append({"role": "assistant", "content": reply})
    

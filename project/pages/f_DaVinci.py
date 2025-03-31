import os
import openai
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI
import base64
import requests
from PIL import Image


load_dotenv()

my_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key = my_api_key)

st.set_page_config(page_title="Chat with JARVIS", page_icon=":robot_face:")
st.header(":robot_face: DaVinci Image Generator (DALLE3) :frame_with_picture:")


st.write('Generate an Image........')
pre_text = 'Generate an Image'
input_prompt = st.text_input("continue the prompt here")

if input_prompt:
    my_prompt = pre_text + ' ' + input_prompt
    st.write(my_prompt)

    response = client.images.generate(
        model="dall-e-3",
        prompt= my_prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    st.write(response.data[0].url)
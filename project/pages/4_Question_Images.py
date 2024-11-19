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
st.header(":robot_face: Chat with JARVIS on Images :frame_with_picture:")

def encode_image(uploaded_image):
    """Encodes an uploaded image to base64

    Args:
        uploaded_image (UploadedFile): The uploaded image file from Streamlit.

    Returns:
        str: Base64 encoded string of the image
    """
    image_bytes = uploaded_image.read()
    return base64.b64encode(image_bytes).decode('utf-8')
    
def display_uploaded_image(uploaded_image):
    #image_bytes = uploaded_image.read()
    image = Image.open(uploaded_img)
    st.image(image)


uploaded_img = st.file_uploader(
        "Upload your image here",
        accept_multiple_files=False,
        type=["jpg",'png','JPG', 'PNG', 'jpeg'],
    )


    
pre_defined_content = [
    'Write this equation in latex equation mode',
    'Explain what is in the image with reasoning',
]
my_content = st.selectbox(
    label=" :red[Content]",
    options=pre_defined_content,
)

with st.expander(label="Type your content if needed", expanded=False):
    typed_content = st.text_input("type your content")

if typed_content:
    my_content = typed_content

model = st.selectbox(
    label="Select model",
    options=["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo", "gpt-4-turbo"],
    index = 1,
)

if uploaded_img:

    base64_image = encode_image(uploaded_img)
    display_uploaded_image(uploaded_img)

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {my_api_key}"
    }

    payload = {
    "model": model,
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text":  my_content
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    data = response.json()
    #st.write(data)
    choices = data.get("choices", [])

    if choices:
        short_response_text = choices[0].get("message", {}).get("content", "No content")
        #print("Completion:", completion_text)
        
    else:
        print(f"Error: {response.status_code}, {response.text}")

    st.write(short_response_text)
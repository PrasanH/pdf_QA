import streamlit as st

st.set_page_config(page_title="Hello Jarvis", page_icon=":robot_face:")

st.title("Hello Sir, How Can I Help You Today? :sunglasses:")
st.write('### :point_left: Please select app page from the left')

st.write(':blue[1. Question documents:] Ask questions on your multiple or single PDF/docx files.')
st.write(':blue[2. Chat with Jarvis:] Ask LLM direct questions. Select predefined content or customized content')
st.write(':blue[3. Question Images:] Ask questions on your images')
st.write(':blue[4. Reasoning AI:] Ask questions to the AI which requires reasoning capabilities. For example: Total R in the word "Strawberry".')

st.sidebar.success("Select a page")

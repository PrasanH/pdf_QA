import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings, OpenAIEmbeddings

# OpenAIEmbeddings,
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain  ### to chat with our text
from langchain.chat_models import ChatOpenAI
from langchain.llms import HuggingFaceHub

# from InstructorEmbedding import INSTRUCTOR
from docx import Document
import os

load_dotenv()


def get_text_from_documents(uploaded_docs):
    st.write(uploaded_docs)
    text = ""
    for uploaded_doc in uploaded_docs:

        if ".pdf" in uploaded_doc.name:
            pdf_reader = PdfReader(uploaded_doc.read())
            for page in pdf_reader.pages:
                text += page.extract_text()
        elif ".docx" in uploaded_doc.name:
            docx_text = extract_text_from_docx(uploaded_doc.read())
            text += docx_text
    return text


def extract_text_from_docx(docx_file):
    text = ""
    doc = Document(docx_file)
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text


def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,  # char size
        chunk_overlap=150,  # to keep a bit of history so that to make sense, 200
        length_function=len,  # len function of python
    )
    chunks = text_splitter.split_text(raw_text)

    return chunks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)

    return vectorstore


def get_convo_chain(vectorstore):
    llm = ChatOpenAI()
    """
    llm = HuggingFaceHub(
        repo_id="google/flan-t5-xxl",
        model_kwargs={"temperature": 0.5, "max_length": 512},
    )
    """
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    convo_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=vectorstore.as_retriever(), memory=memory
    )
    return convo_chain


def handle_user_input(user_question, conversation):
    # response = st.session_state.conversation({"question": user_question})
    response = conversation({"question": user_question})
    st.session_state.chat_history = response["chat_history"]

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(message.content)
        else:
            st.write(message.content)

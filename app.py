import streamlit as st
import llm_utils
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings

# OpenAIEmbeddings,
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain  ### to chat with our text
from langchain.chat_models import ChatOpenAI
from langchain.llms import HuggingFaceHub

# from InstructorEmbedding import INSTRUCTOR


def main():

    load_dotenv()  #### to read the .env file where you have stored the api keys

    st.set_page_config(page_title="Chat with PDFs", page_icon=":books:")

    # if "conversation" not in st.session_state:
    # st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Your documents")
    uploaded_docs = st.file_uploader(
        "Upload your pdfs/docx and click on process",
        accept_multiple_files=True,
        type=["pdf"],
    )

    user_question = st.text_input("Type your question")

    if st.button("Process"):

        ####get pdf text

        raw_text = llm_utils.get_text_from_documents(uploaded_docs)
        # st.write(raw_text)

        ####get  text chunks

        text_chunks = llm_utils.get_text_chunks(raw_text)
        # st.write(text_chunks)

        ####create vector store
        vectorstore = llm_utils.get_vectorstore(text_chunks)

        #### create conversation chain

        # st.session_state.conversation = get_convo_chain(vectorstore)
        conversation = llm_utils.get_convo_chain(vectorstore)
        # session state so that even if streamlit refreshes this variable should not be reintialized.
        # we can also use it outside loops

        if user_question:
            llm_utils.handle_user_input(user_question, conversation)


if __name__ == "__main__":
    main()

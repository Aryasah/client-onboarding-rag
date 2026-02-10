import os
from data.employees import generate_employee_data
import json
from dotenv import load_dotenv
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from assistant import Assistant
from gui import AssistantGUI
from prompts import SYSTEM_PROMPT, WELCOME_MESSAGE
import logging
from langchain_ollama import OllamaEmbeddings

if __name__ == "__main__":
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    logging.basicConfig(level=logging.INFO)
    st.set_page_config(
        page_title="Umbrella Corp Onboarding", page_icon=":guardsman:", layout="wide"
    )

    @st.cache_data(ttl=3600, show_spinner="Loading...")
    def get_user_data():
        return generate_employee_data(1)[0]

    @st.cache_resource(ttl=3600, show_spinner="Initializing vector store...")
    def init_vector_store(pdf_path):
        try:
            loader = PyPDFLoader(pdf_path)
            docs = loader.load()
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=2000, chunk_overlap=200
            )
            splits = text_splitter.split_documents(docs)

            embedding_function = OllamaEmbeddings(model="nomic-embed-text")
            persistent_path = "./data/vectorstore"
            vectorstore = Chroma.from_documents(
                documents=splits,
                embedding=embedding_function,
                persist_directory=persistent_path,
            )

            return vectorstore
        except Exception as e:
            st.error(f"Vector store client not available. :{str(e)}")
            return None

    customer_data = get_user_data()
    vector_store = init_vector_store("data/umbrella_corp_policies.pdf")

    if "customer" not in st.session_state:
        st.session_state.customer = customer_data
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "ai", "content": WELCOME_MESSAGE}]

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=GOOGLE_API_KEY)
    assistant = Assistant(
        system_prompt=SYSTEM_PROMPT,
        llm=llm,
        message_history=st.session_state.messages,
        vector_store=vector_store,
        employee_information=st.session_state.customer,
    )

    gui = AssistantGUI(assistant)
    gui.render()

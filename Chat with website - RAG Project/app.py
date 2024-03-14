import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever
import pinecone 
from langchain.vectorstores import Pinecone as PineconeVectorStore
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
import os

load_dotenv()

pinecone.init(
        api_key=os.getenv('PINECONE_API_KEY'), environment=os.getenv('PINECONE_ENV'))
index_name = os.getenv('PINECONE_INDEX')   

def get_vectorstore_from_url(url):

    loader = WebBaseLoader(url)
    document = loader.load()
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)
    vector_store = PineconeVectorStore.from_texts((d.page_content for d in document_chunks), OpenAIEmbeddings(openai_api_key = os.getenv('OPENAI_API_KEY')), index_name = index_name)

    return vector_store 

def get_context_retriever_chain(vector_store):
    llm = ChatOpenAI()
    retriever = vector_store.as_retriever()
    prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="chat_history"),
        ('user', "{input}"),
        ('user',"Given the above conversation, generate a search query to look up in order to get information relevant to conversation")

    ])
    retriever_chain = create_history_aware_retriever(llm, retriever, prompt)
    return retriever_chain


def get_conversational_rag_chain(retriever_chain):

    llm = ChatOpenAI()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Answer the user's questions based on the below context:\n\n{context}"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user","{input}"),
    ])
    stuff_documents_chain = create_stuff_documents_chain(llm,prompt)

    return create_retrieval_chain(retriever_chain, stuff_documents_chain)


def get_response(user_input):
    retriever_chain = get_context_retriever_chain(st.session_state.vector_store)
    conversation_rag_chain = get_conversational_rag_chain(retriever_chain)
    response = conversation_rag_chain.invoke({
        "chat_history":st.session_state.chat_history, "input": user_input})
    return response['answer']


st.set_page_config(page_title="RAG Project - Chat with websites", page_icon="💬")
st.title("RAG Project - Chat with websites")


with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")

if website_url is None or website_url =="":
    st.info("Please enter a website URL")

else:

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
        AIMessage(content="Hello, I am a Chat bot based on RAG. How can I help you?")]

    if "vector_store" not in st.session_state:
        st.session_state.vector_store = get_vectorstore_from_url(website_url)
        
    vector_store = get_vectorstore_from_url(website_url)

    user_input = st.chat_input("Type your message")

    if user_input is not None and user_input !="":
        response = get_response(user_input)
        st.session_state.chat_history.append(HumanMessage(content=user_input))
        st.session_state.chat_history.append(AIMessage(content=response))
        
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)
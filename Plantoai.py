'''import streamlit as st
import os
from groq import Groq

from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.groq import ChatGroq
from langchain.prompts import PromptTemplate

load_dotenv()  # Load environment variables from .env file

def main():
    # Get Groq API key
    groq_api_key = os.environ['GROQ_API_KEY']  # Ensure this matches the key name in your .env file

    # Display the Groq logo
    spacer, col = st.columns([5, 1])
    with col:
        st.image('groqcloud_darkmode.png')

    # The title and greeting message of the Streamlit application
    st.title("Chat with Planto.ai!")
    st.write("Hello! I'm your coding copilot Planto.ai. How can I help you?")

    # Add customization options to the sidebar
    st.sidebar.title('Customization')
    model = st.sidebar.selectbox(
        'Choose a model',
        ['mixtral-8x7b-32768', 'llama2-70b-4096']
    )
    conversational_memory_length = st.sidebar.slider('Conversational memory length:', 1, 10, value=5)

    memory = ConversationBufferWindowMemory(k=conversational_memory_length)
    
    user_question = st.text_input("Ask a question:")

    # Initialize chat history if it doesn't exist
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    else:
        for message in st.session_state.chat_history:
            memory.save_context({'input': message['human']}, {'output': message['AI']})

    # Initialize Groq Langchain chat object and conversation
    groq_chat = ChatGroq(
        groq_api_key=groq_api_key,
        model_name=model
    )
    conversation = ConversationChain(
        llm=groq_chat,
        memory=memory
    )
    
    # If the user has asked a question,
    if user_question:
        # Generate the chatbot's answer by sending the full prompt to the Groq API
        response = conversation(user_question)
        message = {'human': user_question, 'AI': response['response']}
        st.session_state.chat_history.append(message)
        st.write("Chatbot:", response['response'])

if __name__ == "__main__":
    main()
'''
import streamlit as st
import os
from groq import Groq
import random

from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv() # take environment variables from .env.
# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv') as if they came from the actual environment.

def main():
    # Get Groq API key
    groq_api_key = os.environ['grok-1' ]

    # Display the Groq logo
    spacer, col = st.columns([5, 1])
    with col:
        st.image('groqcloud_darkmode.png')
    # The title and greeting message of the Streamlit application
    st.title("Chat with Planto.ai!")
    st.write("Hello! I'm your coding copilot Planto.ai. How can I help you?")
    
    # Add customization options to the sidebar
    st.sidebar.title('Customization')
    model = st.sidebar.selectbox(
        'Choose a model',
        ['mixtral-8x7b-32768', 'llama2-70b-4096']
    )
    conversational_memory_length = st.sidebar.slider('Conversational memory length:', 1, 10, value = 5)

    memory=ConversationBufferWindowMemory(k=conversational_memory_length)
    
    user_question = st.text_input("Ask a question:")

    # session state variable
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history=[]
    else:
        for message in st.session_state.chat_history:
            memory.save_context({'input': message ['human']}, {'output': message ['Planto.ai']})
    
    # Initialize Groq Langchain chat object and conversation
    groq_chat = ChatGroq(
            groq_api_key=groq_api_key,
            model_name=model
    )
    conversation = ConversationChain(
            llm=groq_chat,
            memory=memory
    )
    
    # If the user has asked a question,
    if user_question:
        
        # The chatbot's answer is generated by sending the full prompt to the Groq API.
        response = conversation (user_question)
        message={'human':user_question, 'Planto.ai': response['response']}
        st.session_state.chat_history.append(message)
        st.write("Chatbot:", response['response'])
    if __name__ =="__main__":
        main()
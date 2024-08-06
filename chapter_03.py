import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (SystemMessage, HumanMessage, AIMessage)

# Load OpenAI API key
# import openai
# openai.api_key = st.secrets['OPENAI_API_KEY']

import openai
OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']
# Load Gemini API key
# import os
# import google.generativeai as genai
# gemini_apikey = st.secrets['GOOGLE_API_KEY']
# genai.configure(api_key=gemini_apikey)



def main():
    llm = ChatOpenAI(temperature=0)

    st.set_page_config(
        page_title="My Great ChatGPT",
        page_icon="🤗"
    )
    st.header("My Great ChatGPT 🤗")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant.")
        ]

    # Monitor user input
    if user_input := st.chat_input("Input your question here:"):
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner("ChatGPT is typing ..."):
            response = llm(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))

    # Display chat history
    messages = st.session_state.get('messages', [])
    for message in messages:
        if isinstance(message, AIMessage):
            with st.chat_message('assistant'):
                st.markdown(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message('user'):
                st.markdown(message.content)
        else:  # isinstance(message, SystemMessage):
            st.write(f"System message: {message.content}")


if __name__ == '__main__':
    main()
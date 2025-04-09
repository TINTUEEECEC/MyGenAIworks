import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os
import pandas as pd
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("models/gemini-1.5-pro")

chat = model.start_chat(history=[])


def get_gemini_response(question):
    response = chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

# Initialise session state for chat history if it doesnt exist

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input:",key="input")
submit=st.button("Ask a question")

if submit and input:
    response=get_gemini_response(input)
    # Add user query and response to session chat histoty
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))


st.subheader("The chat history is")
for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
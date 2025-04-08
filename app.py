import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os
import pandas as pd
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("models/gemini-1.5-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text




#initialise our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input = st.text_input("Input:", key="input")
submit=st.button("Ask the question")

# when submit is clicled
if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is:")
    st.write(response)
# from google.generativeai import list_models

# for m in list_models():
#     print(m.name)
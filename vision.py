import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai
from PIL import Image
import pandas as pd


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("models/gemini-1.5-flash")




def get_gemini_response(input,image):
    if input != "":
        response=model.generate_content(input,image)
    else:
        response=model.generate_content(image)
    return response.text


st.set_page_config(page_title="Gemini Image  Demo")
st.header("Gemini Application")
input = st.text_input("Input prompt:", key="input")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# If file is uploaded
if uploaded_file is not None:
    # Open and display the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_container_width=True)

submit=st.button("Tell me about image")

if submit:
    response=get_gemini_response(input,image)
    st.header("The Response is")
    st.write(response)


from dotenv import load_dotenv
load_dotenv() #Load the .env file

import os
import streamlit as st
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini Pro Vision model
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemeini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text


def input_image_setup(uploaded_file):
    if uploaded_file is not None:

        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No image file uploaded. Please upload an image file.")
    

##initialize streamlit app

st.set_page_config(page_title="Multilanguage Invoice Extractor", page_icon="🔮", layout="wide")
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice", type=["jpg", "jpeg", "png"], key="image")

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

submit = st.button("Tell me about the invoice")

input_prompt = """
You are an expert in understanding invoices. We will upload an image of an invoice and you will answer any questions based on the uploaded image.
"""

# If submit button is clicked
if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemeini_response(input_prompt, image_data, input)
    st.subheader("Invoice Information: ")
    st.write(response)
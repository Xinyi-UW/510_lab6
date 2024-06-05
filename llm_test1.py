import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import psycopg2

# Load environment variables
load_dotenv()

# Configure the API
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Define the model
model = genai.GenerativeModel('gemini-pro')

# Function to generate content
def generate_content(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit UI setup
st.title("Architect Inspiration Playground")
st.image("images/architectural image1.png")  # Make sure the image path is correct

# Set up session state for maintaining chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# UI for chat interaction
with st.form(key='my_form'):
    prompt = st.text_input("Enter your design question or need:", key="query")
    submit_button = st.form_submit_button("Ask AI")

if submit_button:
    if prompt:  # Only process if prompt is not empty
        reply = generate_content(prompt)  # Generate response from AI
        # Append both user input and AI response to the chat history
        st.session_state.chat_history.append("You: " + prompt)
        st.session_state.chat_history.append("AI: " + reply)

# Display chat history
for message in st.session_state.chat_history:
    st.text_area("", value=message, height=75, disabled=True)



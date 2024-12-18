import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat()

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

st.set_page_config("QnA_Application")
st.header("Gemini LLM Application")

if "history" not in st.session_state:
    st.session_state["history"] = []

user_input = st.text_input("INPUT", key="input")
submit = st.button("Ask the Question")

if submit:
    response = get_gemini_response(user_input)
    st.session_state["history"].append(("YOU", user_input))
    st.subheader("The response is ...")
    for chunk in response:
        st.write(chunk.text)
        st.session_state["history"].append(("BOT", chunk.text))
        

st.subheader("The chat history is ...")
for role, text in st.session_state["history"]:
    st.write(f"{role}: {text}")
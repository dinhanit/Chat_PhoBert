from Pho_Chat import Chat
import streamlit as st

st.title("FPTU Chat")
input_text = st.text_input("Enter your question", key="user_input")
response = Chat(input_text)
st.write(response)

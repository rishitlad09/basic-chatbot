import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# Initialize a model
model = ChatGroq(
    model = "qwen/qwen3.8-27b"
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

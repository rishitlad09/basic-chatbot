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
    with st.chat_message(name=message["role"]):
        st.write(message["content"])


# Get user input 
user_input = st.chat_input("Ask me anything....")

if user_input:
    # Display and store message
    st.session_state.messages.append(
        {"role":"user" , "content":user_input}
    )
    
    with st.chat_message("user"):
        st.write(user_input)
        
    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking......"):
            try:
                chat_history = st.session_state.get("messages")
                result = model.invoke(str(chat_history))
                response = result.content
                st.write(response)
                
                st.session_state.messages.append(
                    {"role":"assistant","content":response}
                )
            except Exception as e:
                st.error(f"Error : {e}")
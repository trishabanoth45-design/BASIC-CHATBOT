import streamlit as st
import ollama
st.set_page_config(
    page_title="AI Chartbot",
    page_icon="✨"
)
st.title(" ✨ My AI chatbot")

if "message" not in st.session_state:
    st.session_state.messages = []
for message in  st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt=st.chat_input("Ask AI something...")

if prompt:

    st.session_state.messages.append({ 
            "role":"user",
            "content":prompt})
    with st.chat_message("user"):
        st.write(prompt)

    response=ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages
        
    )
    AI=response["message"]["content"]

    st.write("AI:", AI)
    st.session_state.message.append({
            "role":"assistant",
            "content":AI
        })
    with st.chat_message("Assistant"):
        st.write(AI)
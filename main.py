import streamlit as st

st.session_state

if "messages" not in st.session_state:
    st.session_state.messages=[]
st.set_page_config(page_title="Chatbot Powered by Groq",page_icon=":robot:")
    
def start_bot():
    st.title("Welcome to the Chatbot powered by Groq :smiley: how can I help you today?")
    st.chat_input("Ask me Anything...")
    

with st.sidebar:
    st.header("Settings :rocket:")
    Api_key=st.text_input("Enter the Groq API key",type="password")
    Model=st.selectbox("Select the model to use", options=["deepseek-r1-distill-llama-70b","llama-3.1-8b-instant","qwen/qwen3-32b","gemma2-9b-it"],placeholder=None)
    
    st.button("Clear Chat", on_click=st.session_state.messages.clear)
    st.button("Start Chat",on_click=start_bot)
    

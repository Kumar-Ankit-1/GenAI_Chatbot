import streamlit as st
import bot as b 

st.set_page_config(page_title="Chatbot Powered by Groq", page_icon=":robot:", layout="wide")

# 1. Session State Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

def start_bot():
    st.title("Welcome to the Chatbot powered by Groq :smiley: \nhow can I help you today?")
    
def handle_user_input(prompt):
    """Adds user message, calls the backend, and updates chat history."""
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.spinner("Thinking..."):
        try:
            # CORRECT CALL: Using b.send_prompt (no 't')
            bot_response = b.send_prompt(prompt)
        except Exception as e:
            # Displays the error message, which will now be more informative
            bot_response = f"An error occurred: module 'bot' has no attribute 'sent_prompt' was resolved. However, a new error occurred: {e}"

    st.session_state.messages.append({"role": "assistant", "content": bot_response})

# 2. Sidebar Configuration
with st.sidebar:
    st.header("Settings :rocket:")
    
    st.selectbox(
        "Select the model to use", 
        options=["llama-3.1-8b-instant", "deepseek-r1-distill-llama-70b", "qwen/qwen3-32b", "gemma2-9b-it"], 
        index=None,
        placeholder="Select a model"
    )
    
    st.button("Clear Chat", on_click=st.session_state.messages.clear)
    st.button("Start Chat", on_click=start_bot)


# Display all previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle new user input
prompt = st.chat_input("Ask me Anything...")

if prompt:
    handle_user_input(prompt)
    st.rerun()
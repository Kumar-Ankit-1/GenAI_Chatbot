import streamlit as st
from langchain_groq import ChatGroq

st.set_page_config(page_title="Chatbot Powered by Groq", page_icon=":robot:", layout="wide")

# 2. Session State Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []


def start_bot():
    # This function is used to set the title in the main panel when the button is clicked.
    st.title("Welcome to the Chatbot powered by Groq :smiley: \n\t\thow can I help you today?")
    # Note: st.chat_input should be placed in the main execution flow to actively listen for input.
    

def handle_user_input(prompt):
    """Adds the user's message to the chat history and simulates a bot response."""
    # 1. Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 2. Add a simple bot response (you will replace this with your Groq API call)
    st.session_state.messages.append({"role": "assistant", "content": f"I received your message: '{prompt}' (Groq API logic goes here!)"})

# --- Sidebar Configuration ---

with st.sidebar:
    st.header("Settings :rocket:")
    
    # Using snake_case for consistency
    api_key = st.text_input("Enter the Groq API key", type="password")
    
    model = st.selectbox(
        "Select the model to use", 
        options=["deepseek-r1-distill-llama-70b", "llama-3.1-8b-instant", "qwen/qwen3-32b", "gemma2-9b-it"], 
        index=None,
        placeholder="Select a model"
    )
    
    # Buttons for control
    st.button("Clear Chat", on_click=st.session_state.messages.clear)
    st.button("Start Chat", on_click=start_bot)

# --- Main Application Pane (Right Side) ---


# 1. Display Chat History
# This loop iterates through the session state and displays all past messages.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 2. Add the Input Box and Process New Messages
# st.chat_input should be placed at the bottom of the main section to capture input.
# The key for making the input and chat window appear in the main pane is keeping this code OUTSIDE the 'with st.sidebar:' block.
prompt = st.chat_input("Ask me Anything...")

if prompt:
    # Handle the user's input when they press Enter or click the send button
    handle_user_input(prompt)
    
    # Rerun the app to display the new messages
    st.rerun()
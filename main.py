import streamlit as st
import bot as b 
import time

st.set_page_config(page_title="Chatbot Powered by Groq", page_icon=":robot:", layout="wide")

# === 1. Core Functions ===

def create_new_chat():
    """
    Creates a new, blank chat session and sets it as active.
    """
    new_chat_id = int(time.time())
    st.session_state.chat_sessions[new_chat_id] = {
        "name": "Current Chat",
        "messages": []
    }
    st.session_state.active_chat_id = new_chat_id
    return new_chat_id

def handle_user_input(prompt):
    """
    Handles a new user prompt for the active chat.
    """
    active_chat_messages = st.session_state.chat_sessions[st.session_state.active_chat_id]["messages"]

    if not active_chat_messages:
        new_name = prompt[:30] + "..." if len(prompt) > 30 else prompt
        st.session_state.chat_sessions[st.session_state.active_chat_id]["name"] = new_name

    active_chat_messages.append({"role": "user", "content": prompt})
    
    # Get the selected model from session state, with a default
    selected_model = st.session_state.get("model_selection", "llama-3.1-8b-instant")
    if not selected_model:
        selected_model = "llama-3.1-8b-instant" # Handle empty selection

    with st.spinner("Thinking..."):
        try:
            # Pass both history and model name to the backend
            bot_response = b.send_prompt(active_chat_messages, selected_model)
        except Exception as e:
            bot_response = f"An error occurred: {e}"

    active_chat_messages.append({"role": "assistant", "content": bot_response})

# === 2. Session State Initialization ===

if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = {}

if "active_chat_id" not in st.session_state or st.session_state.active_chat_id not in st.session_state.chat_sessions:
    create_new_chat()

try:
    active_chat_messages = st.session_state.chat_sessions[st.session_state.active_chat_id]["messages"]
except KeyError:
    create_new_chat()
    active_chat_messages = st.session_state.chat_sessions[st.session_state.active_chat_id]["messages"]


# === 3. Sidebar UI ===

with st.sidebar:
    st.header("Chatbot Controls")
    
    if st.button("➕ New Chat", use_container_width=True, type="primary"):
        create_new_chat()
        st.rerun()

    st.header("Chat History")
    
    sorted_chat_ids = sorted(st.session_state.chat_sessions.keys(), reverse=True)
    
    for chat_id in sorted_chat_ids:
        chat = st.session_state.chat_sessions[chat_id]
        button_type = "primary" if chat_id == st.session_state.active_chat_id else "secondary"

        if st.button(chat["name"], key=f"chat_{chat_id}", type=button_type, use_container_width=True):
            if st.session_state.active_chat_id != chat_id:
                st.session_state.active_chat_id = chat_id
                st.rerun()

    st.header("Settings")
    st.selectbox(
        "Select the model to use", 
        options=["qwen/qwen3-32b", "openai/gpt-oss-20b", "llama-3.1-70b-versatile"], 
        index=None, # Set a default selected index
        placeholder="Default: llama-3.1-8b-instant",
        key="model_selection" # Key to read the value from
    )
    
    def delete_all_chats():
        st.session_state.chat_sessions = {}
        st.session_state.active_chat_id = None
    
    st.button("Delete All Chats", on_click=delete_all_chats, use_container_width=True)


# === 4. Main Chat Interface ===

st.title(f"Chatbot powered by Groq :robot:")
st.caption(f"Active Chat: **{st.session_state.chat_sessions[st.session_state.active_chat_id]['name']}**")

for message in active_chat_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask me Anything...")

if prompt:
    handle_user_input(prompt)
    st.rerun()
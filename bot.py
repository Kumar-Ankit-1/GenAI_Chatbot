import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

# 1. Load environment variables from .env file
load_dotenv()

# --- Auto-Configure Environment ---
# The LANGCHAIN_TRACING_V2, LANGCHAIN_API_KEY, and LANGCHAIN_PROJECT 
# variables are automatically loaded by LangChain/LangSmith when they are set 
# in the environment (which load_dotenv() does).

# --- Get the Groq API Key ---
# Retrieve the Groq API Key from the environment
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")

# 2. Initialize the ChatGroq model (LangChain integration)
# LangChain's ChatGroq automatically picks up the key from the environment
# if you omit the 'groq_api_key' argument, but explicitly passing it is also fine.
model = ChatGroq(
    temperature=0.7,
    model_name="llama-3.1-8b-instant",  # Replace with your desired Groq model
    groq_api_key=groq_api_key      # Use the key loaded from .env
)

# 3. Example of calling the model with LangSmith tracing enabled
def get_groq_response(user_prompt: str):
    """
    Sends a prompt to Groq and returns the response.
    This call will be automatically traced and logged to LangSmith.
    """
    messages = [
        SystemMessage(content="You are a helpful assistant for coding and GitHub workflows."),
        HumanMessage(content=user_prompt),
    ]

    # The model call is the part that LangSmith traces.
    response = model.invoke(messages)
    return response.content

# --- Test the function ---
if __name__ == "__main__":
    test_prompt = "Explain the difference between git fork and git branch in one paragraph."
    print(f"User Prompt: {test_prompt}\n")
    
    response_text = get_groq_response(test_prompt)
    
    print("--- Groq Response ---")
    print(response_text)
    
    print("\nThe response is saved already")
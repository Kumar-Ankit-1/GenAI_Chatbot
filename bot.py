import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Configuration
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")

# 2. Define Core Components
model = ChatGroq(
    temperature=0.7,
    model_name="llama-3.1-8b-instant",
    groq_api_key=groq_api_key
)

parser = StrOutputParser()

# 3. Chain Definition
def get_chatbot_chain(model_instance, parser_instance):
    """Creates and returns the LangChain chain."""
    prompt = ChatPromptTemplate.from_messages([
        SystemMessage(content="Act as a senior AI Engineer at google and reply to the user query in a clean and concise manner."),
        ("human", "{user_prompt}"),
    ])
    chain = prompt | model_instance | parser_instance
    return chain

# 4. Initialize the Chain
BOT_CHAIN = get_chatbot_chain(model, parser)

# 5. Core Function
def send_prompt(msg):
    """
    Invokes the chain with the user's message. 
    NOTE: The function name is 'send_prompt'.
    """
    response = BOT_CHAIN.invoke({"user_prompt": msg})
    return response

if __name__ == "__main__":
    test_prompt = "Crack a joke"
    response = send_prompt(test_prompt)
    print(f"--- Groq Response ---\n{response}")
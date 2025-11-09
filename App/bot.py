import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")

def send_prompt(message_history, model_name):
    """
    Invokes the chain with the message history and the specified model.
    """
    
    # Instantiate the selected model
    model = ChatGroq(
        temperature=0.7,
        model_name=model_name,
        groq_api_key=groq_api_key
    )
    
    # Define the prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that replies to the user query in a clean and concise manner."),
        MessagesPlaceholder(variable_name="chat_history"),
    ])
    
    #  Define the parser and chain
    parser = StrOutputParser()
    chain = prompt | model | parser
    
    #  Convert history to LangChain message objects
    lc_messages = []
    for msg in message_history:
        if msg['role'] == 'user':
            lc_messages.append(HumanMessage(content=msg['content']))
        elif msg['role'] == 'assistant':
            lc_messages.append(AIMessage(content=msg['content']))
    
    #  Invoke the chain
    response = chain.invoke({"chat_history": lc_messages})
    return response

if __name__ == "__main__":
    # Test the updated function
    print("--- Testing Stateful Chat ---")
    history = [{"role": "user", "content": "What is the capital of France?"}]
    model_to_test = "llama-3.1-8b-instant"
    
    response = send_prompt(history, model_to_test)
    print(f"User: What is the capital of France?\nBot: {response}")
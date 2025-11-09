# 🤖 Chatbot Powered by Groq

![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red)
![LangChain](https://img.shields.io/badge/LangChain-blueviolet)

![Chatbot UI Screenshot](https://github.com/user-attachments/assets/ec4c249e-61f0-4760-854f-f17074c387c4)

A dynamic, multi-session chatbot interface built with Streamlit and powered by the blazing-fast Groq API using LangChain.

✨ Features

``Multi-Chat Management: Create, switch between, and manage multiple, independent chat sessions.``

``Chat History: All conversations are saved within your browser session.``

``Dynamic Model Selection: Choose from a list of available Groq models (e.g., Llama 3.1, Qwen).``

``Custom System Prompt: Set a custom system prompt from the “Settings” menu to define the bot’s personality and role.``

``Individual Chat Deletion: Easily delete specific chat sessions with a dedicated “🗑️” button.``

``Delete All: Quickly clear all chat history with a single button.``

``Markdown Support: Renders the chatbot’s responses in formatted Markdown.``

🚀 Setup & Installation

Follow these steps to run the chatbot locally.

### 1. Clone the Repository
```bash
git clone https://github.com/Kumar-Ankit-1/groq-chatbot.git
cd groq-chatbot
```

### 2. Create a Virtual Environment

It’s highly recommended to use a virtual environment to manage dependencies.

For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```


For Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

Install all the required Python packages from the requirements.txt file.
```bash
pip install -r requirements.txt
```

### 4. Set Up Your API Key

This project requires a Groq API key to function.

`Get your free API key from the Groq Console.`

`Create a file named .env in the root of the project directory.`

`Add your API key to the .env file:`

```bash
GROQ_API_KEY="your_api_key_here"
```

`The .gitignore file is already configured to exclude .env, ensuring your API key remains private.`

🏃‍♂️ How to Run

Once you’ve installed the dependencies and set your API key, launch the app using Streamlit:

```bash
streamlit run main.py
```

The app will automatically open in your web browser.

## 📁 Project Structure

    groq-chatbot/
    ├── main.py             # Streamlit frontend and session management
    ├── bot.py              # Backend logic and Groq API integration (via LangChain)
    ├── requirements.txt    # List of Python dependencies
    ├── .gitignore          # Files and folders ignored by Git
    └── .env                # Your Groq API key (not tracked by Git)


💡 Notes

Ensure your Groq API key is valid before running the app.

The chatbot’s state and chat history are stored locally in your browser session.

You can easily extend or modify bot.py to integrate additional models or custom logic.

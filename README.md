# 🤖 Chatbot powered by Groq

![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red)
![langchain](https://img.shields.io/badge/LangChain-blueviolet)

![Chatbot UI Screenshot](<img width="1914" height="913" alt="image" src="https://github.com/user-attachments/assets/ec4c249e-61f0-4760-854f-f17074c387c4" />)
A dynamic, multi-session chatbot interface built with **Streamlit** and powered by the blazing-fast **Groq API** using **LangChain**.

---

## ✨ Features

* **Multi-Chat Management:** Create, switch between, and manage multiple, independent chat sessions.
* **Chat History:** All conversations are saved within your browser session.
* **Dynamic Model Selection:** Choose from a list of available Groq models (e.g., Llama 3.1, Qwen).
* **Custom System Prompt:** Set a custom system prompt from the "Settings" menu to define the bot's personality and role.
* **Individual Chat Deletion:** Easily delete specific chat sessions with a dedicated "🗑️" button.
* **Delete All:** Quickly clear all chat history with a single button.
* **Markdown Support:** Renders the chatbot's responses in formatted Markdown.

---

## 🚀 Setup & Installation

Follow these steps to get the chatbot running locally.

**1. Clone the Repository**
```bash
git clone [https://github.com/Kumar-Ankit-1/groq-chatbot.git](https://github.com/Kumar-Ankit-1/groq-chatbot.git)
cd groq-chatbot

2. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies.

Bash

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
3. Install Dependencies

Install all the required Python packages from the requirements.txt file.

Bash

pip install -r requirements.txt
4. Set Up Your API Key

This project requires a Groq API key to function.

a. Get your free API key from the Groq Console. b. Create a file named .env in the root of the project directory. c. Add your API key to this .env file:

Ini, TOML

GROQ_API_KEY="your_api_key_here"
The .gitignore file is already set up to ignore .env, so your API key will remain private and won't be committed to Git.

🏃‍♂️ How to Run
Once you have installed the dependencies and set your API key, run the app using Streamlit:

Bash

streamlit run main.py
The app will open automatically in your web browser.

📁 Project Structure
main.py: Contains all the Streamlit frontend code for the UI, sidebar, and session state management.

bot.py: Handles the backend logic for connecting to the Groq API using langchain_groq.

requirements.txt: A list of all Python libraries needed for the project.

.gitignore: Specifies files and folders to be ignored by Git (like venv/, .env, and __pycache__/).

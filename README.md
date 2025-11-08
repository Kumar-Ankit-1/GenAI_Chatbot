# Chatbot powered by Groq
A simple, multi-session chatbot interface built with **Streamlit** and powered by the blazing-fast **Groq API** using **LangChain**.

## ✨ Features

* **Multi-Chat Management:** Create, switch between, and manage multiple chat sessions.
* **Chat History:** Conversations are saved within your browser session.
* **Dynamic Model Selection:** Choose from a list of available Groq models (e.g., Llama 3.1, Qwen) for your conversation.
* **Delete All:** Quickly clear all chat history.
* **Markdown Support:** Renders the chatbot's responses in formatted Markdown.

## 🚀 Setup & Installation

Follow these steps to get the chatbot running locally.

### 1. Clone the Repository

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

Get your free API key from the Groq Console.

Create a file named .env in the root of the project directory.

Add your API key to this .env file:

Ini, TOML

GROQ_API_KEY="your_api_key_here"
The .gitignore file is already set up to ignore .env, so your API key will remain private and won't be committed to Git.

🏃‍♂️ How to Run
Once you have installed the dependencies and set your API key, run the app using Streamlit:

Bash

streamlit run main.py
The app will open automatically in your web browser.

Project Structure
main.py: Contains all the Streamlit frontend code for the UI, sidebar, and session state management.

bot.py: Contains the backend logic for connecting to the Groq API using langchain_groq and handling the prompt/response.

requirements.txt: A list of all Python libraries needed for the project.

.gitignore: Specifies files and folders to be ignored by Git (like venv/, .env, and __pycache__/).

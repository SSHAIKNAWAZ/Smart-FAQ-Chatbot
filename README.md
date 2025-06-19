# 🤖 Mr. HelpMate - Smart FAQ Chatbot

## Project Overview

"Mr. HelpMate" is an intelligent FAQ Chatbot designed to provide quick and accurate answers to user questions based on content extracted from a PDF document. This application is built using Streamlit for the user interface, Langchain for orchestrating the LLM workflow, and OpenAI's GPT-3.5 Turbo for generating responses. It's ideal for businesses or individuals who want to create a searchable knowledge base from their existing FAQ documents.

The core idea is to allow users to upload their FAQ PDF, and then instantly get answers to their questions, mimicking a natural conversation.

<div align="center">
  <img src="https://github.com/user-attachments/assets/6e57444a-e9e1-4abe-a4ef-e5121fd20388" alt="Description of Image 1" width="500"/>
  <img src="https://github.com/user-attachments/assets/9398bb51-7f0b-438f-8237-62395fbe8ccc" alt="Description of Image 2" width="500"/>
</div>
<img src="https://github.com/user-attachments/assets/61dbe820-be12-49d7-906d-3635321105f1" />

## Features

* **PDF Document Ingestion:** Upload any PDF file containing your FAQs directly through the intuitive Streamlit interface.

* **Intelligent Question Answering:** Ask questions in natural language, and the chatbot will provide relevant answers by referencing the uploaded PDF content.

* **Semantic Search & Retrieval:** Utilizes vector embeddings (powered by OpenAI Embeddings) and FAISS to find the most semantically similar and relevant sections of the PDF to your query.

* **Optimized Chunking:** Documents are automatically split into manageable chunks (500 characters with 100 character overlap) to ensure efficient processing by the Language Model and improved contextual understanding.

* **GPT-3.5 Turbo Powered:** Leverages `gpt-3.5-turbo` for advanced natural language understanding and generation of concise answers.

* **Session-based Question Limit:** Implements a simple limit of 3 questions per session to manage API token usage and demonstrate session management.

## Technologies Used

* **Python:** The primary programming language.

* **Streamlit:** For building the interactive web-based user interface.

* **Langchain:** A framework for developing applications powered by language models. It helps in chaining different components like PDF loaders, text splitters, embeddings, vector stores, and LLMs.

* **`fitz` (PyMuPDF):** Used for efficiently reading and extracting text content from PDF files.

* **OpenAI API:**

    * `gpt-3.5-turbo`: The Large Language Model (LLM) used for generating answers.

    * `OpenAIEmbeddings`: For converting text chunks and user queries into numerical vector representations.

* **FAISS (Facebook AI Similarity Search):** An open-source library for efficient similarity search and clustering of dense vectors. It acts as the local, in-memory vector store for the document embeddings.

* **`python-dotenv`:** For securely loading environment variables (like your OpenAI API key) from a `.env` file.

## Setup and Installation

Follow these steps to get "Mr. HelpMate" up and running on your local machine:

1.  **Clone the Repository:**

    ```
    git clone <your-repository-url>
    cd FAQs\ Chabot # Or simply cd "FAQs Chabot" if your shell supports spaces better
    ```

    (Replace `<your-repository-url>` with the actual URL of your Git repository.)

2.  **Create a Virtual Environment (Recommended):**
    It's good practice to use a virtual environment to manage project dependencies.

    ```
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**

    * **On Windows:**

        ```
        .\venv\Scripts\activate
        ```

    * **On macOS/Linux:**

        ```
        source venv/bin/activate
        ```

4.  **Install Dependencies:**
    Create a `requirements.txt` file in the root of your project directory (`FAQs Chabot/`) with the following content:

    ```
    streamlit
    langchain
    langchain-openai
    langchain-community
    faiss-cpu
    PyMuPDF # This installs 'fitz'
    python-dotenv
    ```

    Then, install them using pip:

    ```
    pip install -r requirements.txt
    ```

5.  **Set Up OpenAI API Key:**
    You'll need an OpenAI API key to use the LLM and embeddings.

    * Create a file named `.env` in the root directory of your project (`FAQs Chabot/`).

    * Add your OpenAI API key to this file in the following format:

        ```
        OPENAI_API_KEY="your_openai_api_key_here"
        ```

        Replace `"your_openai_api_key_here"` with your actual API key. **Do not commit your `.env` file to public repositories.** Add `.env` to your `.gitignore` file.

## Usage

1.  **Ensure you are in the project's root directory** (`FAQs Chabot/`) in your terminal and your virtual environment is activated.

2.  **Run the Streamlit application:**

    ```
    streamlit run app.py
    ```

    This command will open a new tab in your default web browser (usually at `http://localhost:8501`) displaying the chatbot interface.

3.  **Interact with the Chatbot:**

    * **Upload your PDF:** Use the "Upload Your FAQs Pdf" button to select your document.

    * **Ask Questions:** Once the PDF is processed (a success message will appear), type your questions in the "Ask a question from a faq" input box.

    * **View Answers:** The chatbot will display its answer below your question.

    * **Session Limit:** Remember there's a limit of 3 questions per session to manage token usage. To ask more questions, simply refresh the page and re-upload your PDF.

## Project Structure

The project is structured as follows:
- FAQs_Chatbot/
  - ├── app.py # Streamlit web app
  - ├── qa_bot.py # Core QA logic and LangChain pipeline
  - ├── utils.py # PDF reading helper
  - ├── requirements.txt # All dependencies
  - └── .env (optional) # Your OpenAI API Key

## Code Breakdown

### `app.py`

* Sets up the Streamlit page configuration and title.

* Handles PDF file uploads.

* Calls `read_pdf` to extract text from the uploaded PDF.

* Calls `create_vector_store` to build the FAISS index from the PDF text.

* Manages the question-answering interaction using `ask_question`.

* Implements a session-based question limit.

### `utils.py` (Assumed)

* `read_pdf(file)`: A function that takes a file-like object (from Streamlit's file uploader) and extracts all text content from the PDF using PyMuPDF (`fitz`).

### `qa_bot.py` (Assumed)

* **Environment Setup:** Loads `OPENAI_API_KEY` from the `.env` file.

* **Embeddings Initialization:** Initializes `OpenAIEmbeddings` using the loaded API key.

* `create_vector_store(text)`:

    * Splits the input `text` into smaller chunks using `CharacterTextSplitter` (chunk size: 500, overlap: 100).

    * Converts these chunks into Langchain `Document` objects.

    * Creates and returns a FAISS vector store from these documents and embeddings.

* `ask_question(vectorstore, query)`:

    * Performs a similarity search on the `vectorstore` to retrieve relevant document chunks based on the `query`.

    * Initializes `ChatOpenAI` (using `gpt-3.5-turbo`).

    * Loads a question-answering chain (`stuff` type).

    * Invokes the chain with the retrieved documents and the user's question to get the generated answer.

## Limitations

* **Question Limit:** Currently, only 3 questions are allowed per PDF upload session to manage API token consumption. To reset, refresh the page.

* **In-memory Vector Store:** The FAISS vector store is created in memory each time a PDF is uploaded. This means the PDF needs to be re-processed if the app is restarted or the page is refreshed.

* **Single PDF Support:** Designed for one PDF at a time.

* **No Chat History Persistence:** Conversation history is not saved beyond the current session.

## Future Enhancements

* **Persistent FAISS Index:** Implement saving and loading the FAISS index to disk to avoid re-processing PDFs on subsequent runs.

* **Customizable Question Limit:** Allow users to set their own question limit or remove it for local development.

* **Multiple Document Support:** Extend functionality to support querying across multiple PDFs or other document types.

* **Chat History:** Implement saving and displaying the full conversation history within a session or persistently.

* **User Feedback Mechanism:** Add a way for users to rate answers, which could be used to fine-tune or improve the system over time.

* **Advanced UI:** Enhance the Streamlit interface with better styling, loading indicators, and user experience features.


 


## 🧑‍💻 Author
 - Shaik Nawaz

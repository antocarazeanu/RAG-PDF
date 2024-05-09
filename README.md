# Teacher At-Home #

# Carazeanu Antonio and Craciun Alexandru #

This Python script uses the Streamlit library to create a web application that allows students to upload a PDF document of their homework or lesson and ask questions about its content. The application uses OpenAI's GPT-3 model to generate responses to the user's questions, effectively providing a self-correction mechanism.

# Code Explanation #

Importing Necessary Libraries
The script begins by importing necessary libraries and modules:

# Streamlit for creating the web application #

openai for interacting with the OpenAI API
langchain.text_splitter, langchain.vectorstores, langchain.embeddings, langchain.document_loaders for processing the PDF document
warnings for handling warnings
tempfile and os for handling temporary files
Setting Up the Application
The OpenAI API key is set, and the title of the application is defined. A function set_bg_hack_url() is defined and called to set the background image of the application.

# Processing the PDF #

The process_pdf(file) function is defined to process the uploaded PDF file. It creates a temporary file, loads the PDF content, splits the document into chunks, generates embeddings for each chunk using OpenAI, and returns a retriever object that can find relevant chunks based on a query.

# User Interaction #

A file uploader is created for the student to upload a PDF document of their homework or lesson. If a file is uploaded, a chat input is created for the student to ask questions about their work. The student's questions and the bot's responses are stored in st.session_state.messages and displayed in the chat.

When the student asks a question, the script uses the retriever to find relevant chunks from the document, adds the relevant chunks to the student's question as context, and sends the augmented question to the OpenAI API. The API's response is added to the chat history and displayed in the chat, providing the student with feedback on their work.

If no file is uploaded, the script displays a message asking the student to upload a PDF document.

# Usage #

To use this script, you need to install the required libraries, replace "YOUR_OPENAI_API_KEY" with your actual OpenAI API key, and run the script. You can then access the application in your web browser at the URL provided by Streamlit.

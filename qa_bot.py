import os
from dotenv import load_dotenv
from langchain_openai import  OpenAIEmbeddings,ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import  CharacterTextSplitter
from langchain.docstore.document import Document

# load the api key from .env file
load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')

# Set Up Embeddings
embeddings=OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

def create_vector_store(text):
    text_splitter=CharacterTextSplitter(separator='\n',chunk_size=500,chunk_overlap=100)
    chunks=text_splitter.split_text(text)
    docs=[Document(page_content=chunk) for chunk in chunks]
    return  FAISS.from_documents(docs,embeddings)

def ask_question(vectorstore,query):
    docs=vectorstore.similarity_search(query)
    llm=ChatOpenAI(api_key=OPENAI_API_KEY,model='gpt-3.5-turbo')
    chain =load_qa_chain(llm,chain_type='stuff')
    result = chain.invoke({'input_documents': docs, 'question': query})
    return result['output_text']

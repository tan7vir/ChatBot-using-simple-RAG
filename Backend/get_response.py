
#  Air

import requests 
import json
import chromadb
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.embeddings.ollama import OllamaEmbeddings

from load_pdf_and_get_chunk import get_chunk  
from feed_vectordb import feed_vector_db  


PROMPT_TEMPLATE = """
    Answer the question based only on the following context:

    {context}

    ---

    Answer the question based on the above context: {question}
    Please do proper formatting and grammar and If the prompt is empty answer like normal. dont tell according to your 
    knowledge or something like that. sometimes tell according to your book.
"""

# Define the API endpoint
url = "http://localhost:11434/api/generate"
text = "../Data/o-level-physics-formula-sheet-2.pdf"

def load_books(data: object):
    
    chunked_pages = get_chunk(text)
    print ( "<<--Pages chunked-->>" )
    feed_vector_db(chunked_pages)
    print ( "<<--Pages fed to vector db-->>" )

# Define the main function
def get_response(data: object) -> dict:

    print ( data.get('model') )
    # Load the books
    # load_books(data)

    # print ( "<<--Books loaded-->>" )

    emb_fn = OllamaEmbeddings(model = "nomic-embed-text")

    collection_name = "PhysicsBook"

    # preparing the vector database
    collection = Chroma(
        collection_name=collection_name,
        embedding_function=emb_fn,
        persist_directory="../Data/vectorDB",  # Where to save data locally, remove if not necessary
    )

    result = collection.similarity_search_with_score(data.get('prompt'), k=5)
    print ( "Similarity search done" )

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in result])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=data.get('prompt'))

    # Define the data payload with the user's prompt
    data = {
        "model": data.get('model'),
        "prompt": prompt,
        "stream": False
    }


    # Send a POST request
    response = requests.post(url, json=data)
    print ( "Response received" )
    sources = [doc.metadata.get("id", None) for doc, _score in result]


    # Check if the request was successful
    if response.status_code == 200:
        response_data = response.json()
        response_text = response_data.get('response', '')

        # Clean up the response text
        response_text = response_text.replace('\n\n', ' ').replace('\n', ' ').strip()

        return {
            "response": response_text,
            "sources": sources
        }
    else:
        return {"response": "Opps! Something went wrong!"}



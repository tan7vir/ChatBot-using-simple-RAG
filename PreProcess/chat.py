import requests
import json
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

from get_Embeddings import get_embeddings
from LoadPdfAndChunk import get_chunk  
from uploadingVectorDatabase import add_to_vectorDatabase  

PROMPT_TEMPLATE = """
    Answer the question based only on the following context:

    {context}

    ---

    Answer the question based on the above context: {question}
"""

# Define the API endpoint
url = "http://localhost:11434/api/generate"
text = "./Data/Important-Links-and-AI.pdf"

def load_books( ):
    
    chunked_pages = get_chunk(text)
    add_to_vectorDatabase(chunked_pages)

# Define the main function
def main( ) :

    # Load the books
    print("1st")
    load_books()
    print("2nd")

    # preparing the vector database
    embedding_function = get_embeddings()
    db = Chroma (
        persist_directory="chroma", 
        embedding_function = embedding_function
    )

    while True:
        # Ask the user for the prompt
        user_prompt = input("Enter your prompt (or type 'exit' to quit): ")

        if user_prompt.lower() == 'exit':
            print("Exiting...")
            break

        result = db.similarity_search_with_score ( user_prompt, k = 3 )

        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in result])
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context = context_text, question = user_prompt)

        # Define the data payload with the user's prompt
        data = {
            "model": "gemma2",
            "prompt": prompt,
            "stream": False
        }

        # Send a POST request
        response = requests.post(url, json=data)
        sources = [doc.metadata.get("id", None) for doc, _score in result]

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response into a Python dictionary
            response_data = response.json()

            if "response" in response_data:
                print(f"Response: {response_data['response']}\nSources: {sources}")
            else:
                print("No 'response' field found in the response.")
        
        else:
            print(f"Failed to get a response. Status code: {response.status_code}")

        # Ask for another input prompt
        print("\n---\n")

if __name__ == "__main__":
    main()  # Air
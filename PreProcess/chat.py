
# Air

import argparse
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

def main( ) :
    # For intereactive chat
    # Using the python module argparse to get the input from the user

    # Air
    print ("Alpha to Mike, aplha to mike, over and out. Operations completed successfully.")

    text = "../Data/Important-Links-and-AI.pdf"
    chunked_pages = get_chunk(text)

    add_to_vectorDatabase(chunked_pages)
    print ("Alpha to Mike, aplha to mike, over and out. Operations completed successfully.")



    parser = argparse.ArgumentParser(description='Chat with the model')
    parser.add_argument("Question", type=str, help="Enter the question you want to ask: ")
    args = parser.parse_args()
    Question = args.Question

    # Heading towards the model
    interecting_with_the_model ( Question )
    

def interecting_with_the_model (Question: str) : 

    # Air

    # preparing the vector database
    embedding_function = get_embeddings()
    db = Chroma (
        persist_directory="chroma", 
        embedding_function = embedding_function
    )

    # searching in the database
    result = db.similarity_search_with_score ( Question, k = 5 )


    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in result])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context = context_text, question = Question)

    model = Ollama ( model = "gemma2" )
    response_text = model.invoke( prompt )

    sources = [doc.metadata.get("id", None) for doc, _score in result]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)
    return response_text



if __name__ == "__main__":
    main()  # Air

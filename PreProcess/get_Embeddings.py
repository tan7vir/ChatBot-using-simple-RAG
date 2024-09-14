
# Air

from langchain_community.embeddings.ollama import OllamaEmbeddings

def get_embeddings( ):      # documents: list[Document]
    # Extract the page content (text) from each Document
    # contents = [doc.page_content for doc in documents]

    embeddings = OllamaEmbeddings(model = "gemma2")
    return embeddings 
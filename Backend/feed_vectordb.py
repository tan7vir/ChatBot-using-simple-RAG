
# Air 

import chromadb
from langchain.schema.document import Document
from langchain_community.embeddings.ollama import OllamaEmbeddings

client = chromadb.PersistentClient(path="../Data/vectorDB")

# To run the Chroma server, use the following command:
# chroma run --path /db_path

chroma_client = chromadb.HttpClient(host='localhost', port=8000)

def feed_vector_db (chunks: list[Document]): 

    emb_fn = OllamaEmbeddings(model="gemma2:2b")

    from langchain_chroma import Chroma

    collection = Chroma(
        collection_name="PhysicsBook",
        embedding_function=emb_fn,
        persist_directory="../Data/vectorDB",  # Where to save data locally, remove if not necessary
    )

    chunks_with_ids = calculate_chunk_ids(chunks)
    chunk_ids = [chunk.metadata["id"] for chunk in chunks_with_ids]

    print ("<")
    print ("<")
    print ("<")
    print ("<")
    print ("<")
    print ("<")
    print ("<")
    print ("<")
    print ("<")
    print ("<")
    print ("<")
    print ("<")
    print ("<") 

    collection.add_documents (
        documents= chunks_with_ids,
        ids= chunk_ids
    )

def calculate_chunk_ids(chunks):

    # This will create IDs like "data/monopoly.pdf:6:2"
    # Page Source : Page Number : Chunk Index

    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        # If the page ID is the same as the last one, increment the index.
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        # Calculate the chunk ID.
        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        # Add it to the page meta-data.
        chunk.metadata["id"] = chunk_id

    return chunks



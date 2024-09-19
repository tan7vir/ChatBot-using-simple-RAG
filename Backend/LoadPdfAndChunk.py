from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document


def get_chunk(file_path: str) -> list[Document]:
    
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()  # Load and split the PDF into pages

    # Define the function to split documents into chunks
    def split_documents(documents: list[Document]):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=80,
            length_function=len,
            is_separator_regex=False,
        )
        return text_splitter.split_documents(documents)

    # Split the loaded pages into chunks
    print (len(pages))
    return split_documents(pages)
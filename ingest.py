from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

FAISS_INDEX_PATH = "faiss_index" 

def build_vector_database():
    print("=== Step 2: Building Vector Database ===\n")

    print("Loading PDF file...")
    loader = PyPDFLoader("Pakistan_Scholarship_Handbook.pdf")
    all_documents = loader.load()
    print(f"Total pages loaded from PDF: {len(all_documents)}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,       
        chunk_overlap=50      
    )
    chunks = splitter.split_documents(all_documents)
    print(f"Total chunks created: {len(chunks)}")

    print("\nLoading embedding model (first time may download ~90MB)...")
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"  
    )
    print("Creating FAISS index...")
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(FAISS_INDEX_PATH)

    print(f"\n=== Done! FAISS index saved to '{FAISS_INDEX_PATH}' folder ===")
    print("Now run app.py to start the chatbot!")

if __name__ == "__main__":
    build_vector_database()
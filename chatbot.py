import google.generativeai as genai
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

import streamlit as st
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

FAISS_INDEX_PATH = "faiss_index"


genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel("gemini-2.5-flash-lite")  


print("Loading embedding model...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

print("Loading FAISS index...")
vector_store = FAISS.load_local(
    FAISS_INDEX_PATH,
    embeddings,
    allow_dangerous_deserialization=True  # needed for local FAISS files
)

def ask_question(user_question):
    """
    Main RAG function:
    1. Search FAISS for relevant chunks
    2. Build a prompt with those chunks
    3. Send to Gemini and return the answer
    """

    relevant_docs = vector_store.similarity_search(user_question, k=4)

    if not relevant_docs:
        return "Sorry, I could not find any relevant information about that."


    context = "\n\n".join([doc.page_content for doc in relevant_docs])

    prompt = f"""You are a helpful scholarship guidance assistant for Pakistani students.
You ONLY answer questions about HEC scholarships and Sindh Government scholarships.
Only use the information provided in the context below to answer.
If someone asks anything other than scholarships (like cricket, cooking, general knowledge),
reply with: "Sorry, I can only answer questions about HEC and Sindh Government scholarships."
If the answer is not found in the context, say: "I don't have that information. Please visit hec.gov.pk or seef.edu.pk."

--- CONTEXT ---
{context}
--- END CONTEXT ---

Student Question: {user_question}

Answer:"""

    response = gemini_model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("=== Scholarship Chatbot Test ===")
    test_questions = [
        "What is HEC Need Based Scholarship?",
        "What is the income limit for Ehsaas scholarship?",
        "What documents are needed for SEEF scholarship?",
        "Can private university students apply for HEC scholarship?",
    ]
    for q in test_questions:
        print(f"\nQ: {q}")
        print(f"A: {ask_question(q)}")
        print("-" * 50)

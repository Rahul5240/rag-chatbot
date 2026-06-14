# 🎓 Pakistan Scholarship Chatbot (HEC + Government + University Scholarships)

### RAG-based AI Chatbot | PDC Semester Project

---

## 📌 Project Overview

This project is an AI-powered chatbot that helps students in Pakistan find and understand scholarship opportunities, including:

- HEC Scholarships  
- Sindh Government Scholarships  
- Need-based & merit-based programs  
- National & international scholarship guidance  

It uses **Retrieval Augmented Generation (RAG)** to provide accurate answers based on real documents instead of general AI guesses.

---

## 🧠 What is RAG?

**RAG = Retrieval Augmented Generation**

Instead of training a model from scratch:

1. We collect scholarship-related documents (PDFs, websites, policies)
2. Convert them into embeddings and store them in a vector database (FAISS)
3. When a user asks a question:
   - The system retrieves the most relevant information
   - That information is sent to Gemini AI
4. Gemini generates a final, context-aware answer

---

## ⚙️ Tech Stack

- Python  
- Streamlit (Frontend UI)  
- FAISS (Vector Database for similarity search)  
- HuggingFace Embeddings (`all-MiniLM-L6-v2`)  
- Google Gemini API  
- Web Scraping (BeautifulSoup)  
- RAG Architecture  

---

## 🚀 Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt
import streamlit as st
import os

# ---- Auto build FAISS index if not exists ----
if not os.path.exists("faiss_index"):
    st.info("Building knowledge base from PDF... Please wait 1-2 minutes on first load.")
    from ingest import build_vector_database
    build_vector_database()

from chatbot import ask_question

# ---- Page Settings ----
st.set_page_config(
    page_title="Pakistan University Scholarship Chatbot",
    page_icon="🎓",
    layout="centered"
)

# ---- Header ----
st.title("🎓 Pakistan Scholarship Guidance Chatbot")
st.markdown("""
Ask me anything about HEC and Sindh Government Scholarships!
- Eligibility criteria
- Scholarship amounts
- Required documents
- How to apply step by step
""")

st.divider()

# ---- Chat History ----
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---- Show previous messages ----
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ---- User Input ----
user_input = st.chat_input("Ask about HEC or Sindh scholarships...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        with st.spinner("Searching scholarship database..."):
            answer = ask_question(user_input)
        st.write(answer)
    st.session_state.chat_history.append({"role": "assistant", "content": answer})

# ---- Sidebar ----
with st.sidebar:
    st.header("📚 Scholarships Covered")
    st.markdown("""
    1. **HEC Need-Based Scholarship**
    2. **Ehsaas Undergraduate Scholarship**
    3. **HEC Overseas Scholarship** (MS/PhD)
    4. **Benazir Undergraduate Scholarship**
    5. **PM Laptop Scheme**
    6. **SEEF Sindh Scholarship**
    7. **Sindh Merit Scholarship**
    8. **Pakistan Baitul Maal**
    9. **NAVTTC Scholarship**
    """)
    st.divider()
    st.caption("Data Source: HEC Pakistan & Sindh Government")
    st.caption("Built with LangChain + FAISS + Gemini API")

    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

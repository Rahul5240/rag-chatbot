import streamlit as st
from chatbot import ask_question

st.set_page_config(
    page_title="Pakistan Scholarship Chatbot",
    page_icon="🎓",
    layout="centered"
)
st.title("🎓 Pakistan Scholarship Guidance Chatbot")

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
""")

st.divider()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Ask about HEC or Sindh scholarships...")

if user_input:
    
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        with st.spinner("Searching university database..."):
            answer = ask_question(user_input)
        st.write(answer)
    st.session_state.chat_history.append({"role": "assistant", "content": answer})

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
""")
    st.divider()
    st.caption("Built with LangChain + FAISS + Gemini API")

    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

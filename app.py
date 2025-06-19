# from utils import read_pdf
# from qa_bot import create_vector_store, ask_question
#
# # 📂 Load the FAQ PDF file
# with open("features_of_internet_tickets.pdf", "rb") as f:
#     text = read_pdf(f)
#
# # 🧠 Create vector store from text
# vectorstore = create_vector_store(text)
#
# # 🗣️ Ask a question
# question = "What is the Booking Hours?"
# answer = ask_question(vectorstore, question)
#
# # 📤 Output
# print("Q:", question)
# print("A:", answer)
# #--------------------------------------------------------
# import streamlit as st
# from utils import  read_pdf
# from qa_bot import create_vector_store,ask_question
#
# st.set_page_config(page_title="Mr. HelpMate - FAQ Chatbot",layout='centered')
# st.title("🤖 Mr. HelpMate - Smart FAQ Chatbot")
# st.markdown("Upload your business FAQ PDF and ask questions like a customer!")
#
# upload_file=st.file_uploader('Upload Your FAQs Pdf',type='pdf')
#
# if upload_file is not None:
#     text=read_pdf(upload_file)
#     vectorstore=create_vector_store(text)
#
#     st.success('PDF Processed Succesfully. Now You Can ask upto 3 question')
#
#     if 'question_count' not in st.session_state:
#         st.session_state.question_count=0
#
#     if st.session_state.question_count<3:
#         question=st.text_input('Ask a question from a faq')
#
#         if question:
#             answer = ask_question(vectorstore, question)
#             st.session_state.question_count += 1
#
#             st.markdown(f"**Q:** {question}")
#             st.markdown(f"**A:** {answer}")
#     else:
#         st.warning("⚠️ Limit reached: Only 3 questions allowed per session to save tokens.")

import streamlit as st
from utils import read_pdf
from qa_bot import create_vector_store, ask_question

# 🖼️ Page Config
st.set_page_config(page_title="Mr. HelpMate - Smart FAQ Bot", layout="centered")

# 🎨 Custom Styling
st.markdown("""
    <style>
        .main {
            background-color: #f4f4f4;
            padding: 20px;
            border-radius: 10px;
        }
        .stButton>button {
            color: white;
            background: #4CAF50;
        }
        .stTextInput>div>div>input {
            border: 2px solid #4CAF50;
        }
    </style>
""", unsafe_allow_html=True)

# 🧠 App Title
st.title("🤖 Mr. HelpMate – Smart FAQ Chatbot")
st.markdown("Welcome! Upload your **FAQ PDF** and ask questions to get instant answers using AI. ⚡")

# 📄 File Upload
uploaded_file = st.file_uploader("📎 Upload your business FAQ PDF", type=["pdf"])

# 🧠 Chatbot Workflow
if uploaded_file:
    with st.spinner("🔍 Reading and indexing your PDF..."):
        text = read_pdf(uploaded_file)
        vectorstore = create_vector_store(text)

    st.success("✅ PDF processed! Ask up to 3 questions.")

    # 🧮 Session tracking
    if "question_count" not in st.session_state:
        st.session_state.question_count = 0

    if st.session_state.question_count < 3:
        question = st.text_input("💬 Type your question below:")

        if st.button("Ask"):
            if question:
                with st.spinner("🤖 Thinking..."):
                    answer = ask_question(vectorstore, question)
                    st.session_state.question_count += 1
                    st.markdown(f"**🧑‍💼 You asked:** `{question}`")
                    st.markdown(f"**🤖 Mr. HelpMate says:** {answer}")
            else:
                st.warning("Please type a question.")
    else:
        st.error("⚠️ You've reached your 3-question limit for this session.")
        st.markdown("🔄 Refresh the page to start a new session.")
else:
    st.info("👆 Upload a FAQ PDF to begin.")











                                               


import streamlit as st
from utils import parse_pdf, embed_text, get_answer

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st.set_page_config(page_title="ChatDoc", page_icon=":smiley:", layout="wide")
st.header("ChatDoc - The AI Bot Answering Your Questions based on a Document")
uploaded_file = st.file_uploader("Upload a PDF file, then you can ask questions, our ChatGPT will answer questions based on the document", type=["pdf"])

if uploaded_file is not None:
    index = embed_text(parse_pdf(uploaded_file))
    query = st.text_area("Ask a question about the document")
    button = st.button("Submit")
    if button:
        st.write(get_answer(index, query))

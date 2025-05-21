import streamlit as st

st.set_page_config(page_title="English Lesson Analyzer", layout="wide")

st.title("🎙️ English Lesson Analyzer")

uploaded_file = st.file_uploader("Upload your lesson audio", type=["mp3", "wav", "m4a"])

if uploaded_file:
    st.success("✅ File uploaded. Ready to analyze!")
    st.write("Analysis will appear here after processing.")

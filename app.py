import streamlit as st
from analyzer import analyze_code
from refactor import refactor_code

st.title("🤖 AI Code Refactoring Tool")

uploaded_file = st.file_uploader("Upload your Python file", type=["py"])

if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")

    st.subheader("📌 Original Code")
    st.code(code, language='python')

    issues = analyze_code(code)
    st.write("🔍 Issues Found:", issues)

    if st.button("Refactor Code"):
        new_code = refactor_code(code, issues)

        st.subheader("✅ Refactored Code")
        st.code(new_code, language='python')
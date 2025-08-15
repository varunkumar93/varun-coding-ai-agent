import streamlit as st
from modules.groq_agent import GroqAgent
from modules.code_assistant import CodeAssistant
from modules.code_generator import generate_code
from modules.file_handler import FileHandler

file_handler = FileHandler()
summary = file_handler.summarize(uploaded_file)

# Initialize modules
groq_agent = GroqAgent()
assistant = CodeAssistant()
code = generate_code(prompt)
file_handler = FileHandler()

st.set_page_config(page_title="Groq-Powered Dev+QA Agent", layout="wide")

st.title("🧠 Groq-Powered Dev+QA Agent")
st.markdown("Upload code, generate new scripts, debug errors, or explain logic — all in one place.")

# Sidebar: Mode selection
mode = st.sidebar.radio("Choose Mode", ["Explain Code", "Generate Code", "Debug Code", "Upload File"])

# Main logic
if mode == "Upload File":
    uploaded_file = st.file_uploader("Upload your code file", type=["py", "txt", "js", "java", "cpp"])
    if uploaded_file:
        code = file_handler.read_file(uploaded_file)
        st.code(code, language="python")
        st.success("File uploaded and displayed.")
elif mode == "Explain Code":
    code_input = st.text_area("Paste your code below", height=300)
    if st.button("Explain"):
        explanation = assistant.explain_code(code_input)
        st.markdown("### 🧾 Explanation")
        st.write(explanation)
elif mode == "Generate Code":
    prompt = st.text_area("Describe what you want to build", height=200)
    if st.button("Generate"):
        code = generator.generate_code(prompt)
        st.markdown("### 🛠️ Generated Code")
        st.code(code, language="python")
elif mode == "Debug Code":
    buggy_code = st.text_area("Paste your buggy code", height=300)
    if st.button("Debug"):
        debugged = assistant.debug_code(buggy_code)
        st.markdown("### 🐞 Debugged Code")
        st.code(debugged, language="python")

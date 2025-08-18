import streamlit as st
import os
import version_checker

# Load Groq API key from Streamlit secrets
os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]

# Core modules
from modules.memory_agent import MemoryAgent
from modules.learning_path import LearningPath
from modules.code_runner import CodeRunner

# Expanded modules
from modules.prompt_lab import PromptLab
from modules.quiz_engine import QuizEngine
from modules.agent_flow import AgentFlow
from modules.code_generator import generate_code
from modules.code_assistant import CodeAssistant
from modules.file_handler import FileHandler
from modules.groq_agent import GroqAgent
from modules.unified_course_manager import UnifiedCourseManager

# Session state setup
if "progress" not in st.session_state:
    st.session_state.progress = set()

if "groq_agent" not in st.session_state:
    st.session_state.groq_agent = GroqAgent()

if "memory_agent" not in st.session_state:
    st.session_state.memory_agent = MemoryAgent()

if "learning_path" not in st.session_state:
    st.session_state.learning_path = LearningPath()

if "code_runner" not in st.session_state:
    st.session_state.code_runner = CodeRunner()

if "prompt_lab" not in st.session_state:
    st.session_state.prompt_lab = PromptLab(st.session_state.groq_agent)

if "quiz_engine" not in st.session_state:
    st.session_state.quiz_engine = QuizEngine()

if "code_generator" not in st.session_state:
    st.session_state.code_generator = lambda spec: generate_code(spec)

if "code_assistant" not in st.session_state:
    st.session_state.code_assistant = CodeAssistant()

if "agent_flow" not in st.session_state:
    st.session_state.agent_flow = AgentFlow(
        st.session_state.code_assistant,
        st.session_state.code_generator
    )

if "file_handler" not in st.session_state:
    st.session_state.file_handler = FileHandler()

# Sidebar mode selection
st.sidebar.title("Varun Coding AI Agent")
mode = st.sidebar.radio("Choose Mode", [
    "Memory Chat",
    "Learning Path",
    "Run Code",
    "Prompt Lab",
    "Quiz Engine",
    "Agent Flow",
    "Code Generator",
    "Code Assistant",
    "File Handler"
])
st.success(f"✅ Current mode: {mode}")

# Sidebar topic selector for Learning Path
topic = st.sidebar.selectbox("Select Topic", [
    "Python", "C", "C++", "Rust", "Java", "Go", "Swift", "C#", "Kotlin",
    "JavaScript", "TypeScript", "PHP", "Ruby", "R", "Julia", "MATLAB",
    "Fortran", "COBOL", "Solidity", "VHDL", "Verilog",
    "HTML", "XML", "Markdown", "LaTeX", "CSS", "SQL", "GraphQL", "JSON", "YAML",
    "Dockerfile", "Terraform (HCL)", "Regex", "GLSL", "UML",
    "Gherkin", "JUnit", "TestNG", "PyTest", "Selenium", "Cucumber", "Robot Framework",
    "Machine Learning", "Agentic AI"
])

# Mode: Memory Chat
if mode == "Memory Chat":
    st.title("🧠 Memory Chat")
    user_input = st.text_area("Ask your assistant anything")
    if st.button("Send"):
        response = st.session_state.memory_agent.chat(user_input)
        st.markdown("#### 💬 Response")
        st.write(response)

# Mode: Learning Path
elif mode == "Learning Path":
    st.title("🧭 Learn Any Topic")

    course_manager = UnifiedCourseManager()
    quiz_engine = st.session_state.quiz_engine

    st.subheader(f"📘 {topic} Lesson")
    lesson_content = course_manager.get_lesson_content("Custom", topic)
    st.markdown(lesson_content)

    st.session_state.progress.add(topic)

    quiz = quiz_engine.get_quiz(topic)
    st.markdown("### 🧪 Quiz Time")
    st.write(quiz)

# Mode: Run Code
elif mode == "Run Code":
    st.title("🧪 Code Execution Sandbox")
    code = st.text_area("Paste Python code below", height=300)
    if st.button("Execute"):
        output = st.session_state.code_runner.run_code(code)
        st.markdown("### 🖥️ Output")
        st.code(output)

# Mode: Prompt Lab
elif mode == "Prompt Lab":
    st.title("🧠 Prompt Lab")
    prompt = st.text_area("Enter your custom prompt")
    if st.button("Test Prompt"):
        response = st.session_state.prompt_lab.run(prompt)
        st.markdown("### 🔍 Response")
        st.write(response)

# Mode: Quiz Engine
elif mode == "Quiz Engine":
    st.title("🧠 Quiz Engine")
    quiz_topic = st.text_input("Enter quiz topic")
    if st.button("Generate Quiz"):
        quiz = st.session_state.quiz_engine.get_quiz(quiz_topic)
        st.markdown("### 📝 Quiz")
        st.write(quiz)

# Mode: Agent Flow
elif mode == "Agent Flow":
    st.title("🔗 LangChain Agent Flow")
    query = st.text_area("Enter task for agent")
    if st.button("Run Agent"):
        result = st.session_state.agent_flow.run(query)
        st.markdown("### 🤖 Agent Response")
        st.write(result)

# Mode: Code Generator
elif mode == "Code Generator":
    st.title("⚙️ Code Generator")
    spec = st.text_area("Describe the code you want")
    if st.button("Generate Code"):
        code = st.session_state.code_generator(spec)
        st.markdown("### 🧾 Generated Code")
        st.code(code)

# Mode: Code Assistant
elif mode == "Code Assistant":
    st.title("🛠️ Code Assistant")
    code_input = st.text_area("Paste code for explanation or debugging", height=300)
    if st.button("Assist"):
        result = st.session_state.code_assistant.assist(code_input)
        st.markdown("### 🧠 Assistant Output")
        st.write(result)

# Mode: File Handler
elif mode == "File Handler":
    st.title("📁 File Handler")
    uploaded_file = st.file_uploader("Upload a file")
    if uploaded_file:
        result = st.session_state.file_handler.handle(uploaded_file)
        st.markdown("### 📄 File Output")
        st.write(result)

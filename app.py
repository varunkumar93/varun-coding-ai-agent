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
from modules.course_manager import ProgramizCourseManager
if "code_generator" not in st.session_state:
    st.session_state.code_generator = lambda spec: generate_code(spec)

# Dummy course manager (replace with real one later)
class DummyCourseManager:
    def get_lesson_content(self, path, lesson):
        return f"### Lesson: {lesson}\nThis is placeholder content for {path} → {lesson}."

course_manager = DummyCourseManager()

# Session state setup
if "progress" not in st.session_state:
    st.session_state.progress = {}

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
    st.session_state.code_generator = CodeGenerator()

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
st.sidebar.title("🧠 VarunAI Agent Suite")
mode = st.sidebar.radio("Choose Mode", [
    "🧠 Memory Chat",
    "🧭 Learning Path",
    "🧪 Run Code",
    "🧠 Prompt Lab",
    "🧠 Quiz Engine",
    "🔗 Agent Flow",
    "⚙️ Code Generator",
    "🛠️ Code Assistant",
    "📁 File Handler"
])

# Mode: Memory Chat
if mode == "🧠 Memory Chat":
    st.title("🧠 Memory Chat")
    user_input = st.text_area("Ask your assistant anything")
    if st.button("Send"):
        response = st.session_state.memory_agent.chat(user_input)
        st.markdown("#### 💬 Response")
        st.write(response)

# Mode: Learning Pathfrom modules.learning_path import LearningPath
elif selected_mode == "🧠 Learning Path":
    from modules.learning_path import LearningPath
    from modules.course_manager import ProgramizCourseManager
    from modules.quiz_engine import QuizEngine

    learning_path = LearningPath()
    course_manager = ProgramizCourseManager()
    quiz_engine = QuizEngine()

    # ✅ FIX: Ensure progress is a set
    if "progress" not in st.session_state or not isinstance(st.session_state.progress, set):
        st.session_state.progress = set()

    # Recommend next lesson
    path, lesson = learning_path.recommend(st.session_state.progress)

    if path and lesson:
        st.subheader(f"📘 {path} → {lesson}")

        # Fetch lesson content
        lesson_content = course_manager.get_lesson_content(path, lesson)
        st.markdown(lesson_content)

        # ✅ Track progress
        st.session_state.progress.add((path, lesson))

        # Generate quiz
        quiz = quiz_engine.generate(path, lesson)
        st.markdown("### 🧪 Quiz Time")
        st.write(quiz)
    else:
        st.success("🎉 You've completed all lessons!")
# Mode: Run Code
elif mode == "🧪 Run Code":
    st.title("🧪 Code Execution Sandbox")
    code = st.text_area("Paste Python code below", height=300)
    if st.button("Execute"):
        output = st.session_state.code_runner.run_code(code)
        st.markdown("### 🖥️ Output")
        st.code(output)

# Mode: Prompt Lab
elif mode == "🧠 Prompt Lab":
    st.title("🧠 Prompt Lab")
    prompt = st.text_area("Enter your custom prompt")
    if st.button("Test Prompt"):
        response = st.session_state.prompt_lab.run(prompt)
        st.markdown("### 🔍 Response")
        st.write(response)

# Mode: Quiz Engine
elif mode == "🧠 Quiz Engine":
    st.title("🧠 Quiz Engine")
    topic = st.text_input("Enter quiz topic")
    if st.button("Generate Quiz"):
        quiz = st.session_state.quiz_engine.generate(topic)
        st.markdown("### 📝 Quiz")
        st.write(quiz)

# Mode: Agent Flow
elif mode == "🔗 Agent Flow":
    st.title("🔗 LangChain Agent Flow")
    query = st.text_area("Enter task for agent")
    if st.button("Run Agent"):
        result = st.session_state.agent_flow.run(query)
        st.markdown("### 🤖 Agent Response")
        st.write(result)

# Mode: Code Generator
elif mode == "⚙️ Code Generator":
    st.title("⚙️ Code Generator")
    spec = st.text_area("Describe the code you want")
    if st.button("Generate Code"):
        code = st.session_state.code_generator.generate(spec)
        st.markdown("### 🧾 Generated Code")
        st.code(code)

# Mode: Code Assistant
elif mode == "🛠️ Code Assistant":
    st.title("🛠️ Code Assistant")
    code_input = st.text_area("Paste code for explanation or debugging", height=300)
    if st.button("Assist"):
        result = st.session_state.code_assistant.assist(code_input)
        st.markdown("### 🧠 Assistant Output")
        st.write(result)

# Mode: File Handler
elif mode == "📁 File Handler":
    st.title("📁 File Handler")
    uploaded_file = st.file_uploader("Upload a file")
    if uploaded_file:
        result = st.session_state.file_handler.handle(uploaded_file)
        st.markdown("### 📄 File Output")
        st.write(result)

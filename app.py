import streamlit as st
from modules.course_manager import CourseManager
from modules.code_assistant import CodeAssistant
from modules.code_generator import generate_code
from modules.file_handler import FileHandler
from modules.groq_agent import GroqAgent
from modules.agent_flow import AgentFlow
from modules.prompt_lab import PromptLab
from modules.quiz_engine import QuizEngine

# Page config
st.set_page_config(page_title="VarunAI Coding Agent", layout="wide")
st.title("🧠 VarunAI Coding Agent")

# Initialize modules
course_manager = CourseManager()
assistant = CodeAssistant()
file_handler = FileHandler()
groq_agent = GroqAgent()
agent_flow = AgentFlow(assistant, generate_code)
prompt_lab = PromptLab(groq_agent)
quiz_engine = QuizEngine()

# Session state
if "progress" not in st.session_state:
    st.session_state.progress = {}
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = {}

# Sidebar
mode = st.sidebar.radio("Choose Mode", [
    "📚 Course Training", "🧪 Practice Lab", "📁 Upload File",
    "🧠 Ask AI", "🧠 Prompt Lab", "🔗 Agent Flow", "🧠 Quiz Engine"
])
st.sidebar.markdown("### 📈 Progress")
for c, l in st.session_state.progress.items():
    st.sidebar.write(f"{c}: {l}")

# Mode logic
if mode == "📚 Course Training":
    course = st.selectbox("Choose a course", list(course_manager.courses.keys()))
    lesson = st.selectbox("Choose a lesson", course_manager.get_lessons(course))
    content = course_manager.get_lesson_content(course, lesson)
    st.markdown(content)
    st.session_state.progress[course] = lesson
    st.success(f"Progress saved: {course} → {lesson}")

elif mode == "🧪 Practice Lab":
    code_input = st.text_area("Paste your code", height=300)
    action = st.radio("Choose Action", ["Explain", "Debug", "Generate"])
    if st.button("Run"):
        if action == "Explain":
            st.markdown("### 🧾 Explanation")
            st.write(assistant.explain_code(code_input))
        elif action == "Debug":
            st.markdown("### 🐞 Debugged Code")
            st.code(assistant.debug_code(code_input), language="python")
        elif action == "Generate":
            st.markdown("### 🛠️ Generated Code")
            st.code(generate_code(code_input), language="python")

elif mode == "📁 Upload File":
    uploaded_file = st.file_uploader("Upload your code file", type=["py", "txt", "js", "java", "cpp"])
    if uploaded_file:
        code = file_handler.read_file(uploaded_file)
        ext = uploaded_file.name.split('.')[-1]
        lang_map = {"py": "python", "js": "javascript", "java": "java", "cpp": "cpp", "txt": "text"}
        st.code(code, language=lang_map.get(ext, "text"))
        st.success("File uploaded and displayed.")

elif mode == "🧠 Ask AI":
    query = st.text_area("Ask anything about coding or training")
    if st.button("Ask"):
        response = groq_agent.generate(query)
        st.markdown("### 💬 Response")
        st.write(response)

elif mode == "🧠 Prompt Lab":
    prompt = st.text_area("Enter your prompt")
    style = st.selectbox("Choose style", ["default", "verbose", "minimal"])
    if st.button("Run Prompt"):
        response = prompt_lab.run_prompt(prompt, style)
        st.markdown("### 🧠 Response")
        st.write(response)

elif mode == "🔗 Agent Flow":
    code_input = st.text_area("Paste code for chaining", height=300)
    flow_type = st.radio("Choose Flow", ["Explain → Debug", "Generate → Explain"])
    if st.button("Run Flow"):
        if flow_type == "Explain → Debug":
            explanation, debugged = agent_flow.explain_then_debug(code_input)
            st.markdown("### 🧾 Explanation")
            st.write(explanation)
            st.markdown("### 🐞 Debugged Code")
            st.code(debugged, language="python")
        else:
            code, explanation = agent_flow.generate_then_explain(code_input)
            st.markdown("### 🛠️ Generated Code")
            st.code(code, language="python")
            st.markdown("### 🧾 Explanation")
            st.write(explanation)

elif mode == "🧠 Quiz Engine":
    topic = st.selectbox("Choose quiz topic", ["Python Basics", "Debugging 101"])
    quiz = quiz_engine.get_quiz(topic)
    st.markdown(f"### ❓ {quiz['question']}")
    answer = st.radio("Choose your answer", quiz["options"])
    if st.button("Submit Answer"):
        correct = quiz_engine.check_answer(answer, quiz["answer"])
        if correct:
            st.success("✅ Correct!")
            st.session_state.quiz_score[topic] = st.session_state.quiz_score.get(topic, 0) + 1
        else:
            st.error("❌ Incorrect.")
        st.markdown(f"**Your Score for {topic}:** {st.session_state.quiz_score.get(topic, 0)}")

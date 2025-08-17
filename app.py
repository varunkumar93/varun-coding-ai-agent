import streamlit as st
from modules.memory_agent import MemoryAgent
from modules.learning_path import LearningPath
from modules.code_runner import CodeRunner

# Optional: Dummy course manager
class DummyCourseManager:
    def get_lesson_content(self, path, lesson):
        return f"### Lesson: {lesson}\nThis is placeholder content for {path} → {lesson}."

course_manager = DummyCourseManager()

# Session state setup
if "progress" not in st.session_state:
    st.session_state.progress = {}

if "memory_agent" not in st.session_state:
    st.session_state.memory_agent = MemoryAgent()

if "learning_path" not in st.session_state:
    st.session_state.learning_path = LearningPath()

if "code_runner" not in st.session_state:
    st.session_state.code_runner = CodeRunner()

# Sidebar mode selection
mode = st.sidebar.radio("Choose Mode", [
    "🧠 Memory Chat", "🧭 Learning Path", "🧪 Run Code"
])

# Mode logic
if mode == "🧠 Memory Chat":
    st.markdown("### 🧠 Memory Chat")
    user_input = st.text_area("Ask your assistant anything")
    if st.button("Send"):
        response = st.session_state.memory_agent.chat(user_input)
        st.markdown("#### 💬 Response")
        st.write(response)

elif mode == "🧭 Learning Path":
    st.markdown("### 🧭 Personalized Learning Path")
    path, lesson = st.session_state.learning_path.recommend(st.session_state.progress)
    if lesson:
        st.markdown(f"**Path:** {path}")
        st.markdown(f"**Next Lesson:** {lesson}")
        content = course_manager.get_lesson_content(path, lesson)
        st.markdown(content)
    else:
        st.success("🎉 All lessons completed!")

elif mode == "🧪 Run Code":
    st.markdown("### 🧪 Code Execution Sandbox")
    code = st.text_area("Paste Python code below", height=300)
    if st.button("Execute"):
        output = st.session_state.code_runner.run_code(code)
        st.code(output)

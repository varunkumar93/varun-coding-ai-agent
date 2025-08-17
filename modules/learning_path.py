elif mode == "🧭 Learning Path":
    st.title("🧭 Personalized Learning Journey")

    # Initialize course manager if not already
    if "course_manager" not in st.session_state:
        from modules.course_manager import ProgramizCourseManager
        st.session_state.course_manager = ProgramizCourseManager()

    # Initialize learning path if not already
    if "learning_path" not in st.session_state:
        from modules.learning_path import LearningPath
        st.session_state.learning_path = LearningPath()

    # Initialize progress if not already
    if "progress" not in st.session_state:
        st.session_state.progress = {}

    # Get next recommended lesson
    try:
        path, lesson = st.session_state.learning_path.recommend(st.session_state.progress)
    except Exception as e:
        st.error(f"⚠️ Error recommending lesson: {e}")
        st.stop()

    if lesson:
        formatted_topic = lesson.lower().replace(" ", "-")
        content = st.session_state.course_manager.get_lesson_content("Python", formatted_topic)

        st.markdown(f"### 📘 {path} → {lesson}")
        st.write(content)

        # Mark lesson as completed
        if st.button("Mark as Completed"):
            if path not in st.session_state.progress:
                st.session_state.progress[path] = []
            st.session_state.progress[path].append(lesson)
            st.success(f"✅ Marked '{lesson}' as completed.")

        # Optional: Generate quiz
        if st.button("Generate Quiz"):
            quiz = st.session_state.quiz_engine.generate(lesson)
            st.markdown("### 📝 Quiz")
            st.write(quiz)
    else:
        st.success("🎉 All lessons completed!")

import requests
from bs4 import BeautifulSoup

class ProgramizCourseManager:
    def get_lesson_content(self, language, topic_slug):
        # ✅ Static lesson for Python
        if topic_slug == "variables-data-types":
            return """### 📘 Variables and Data Types (Python)
Variables store data. Data types define the kind of data.

📘 Read: [freeCodeCamp Python Guide](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/)
📺 Watch: [Python Full Course](https://www.youtube.com/watch?v=rfscVS0vtbw)
"""

        # ✅ Dynamic lesson for Java, JavaScript, and other languages
        try:
            url = f"https://www.freecodecamp.org/news/tag/{topic_slug}/"
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
            articles = soup.select("article h2 a")

            if not articles:
                raise ValueError("No articles found")

            lesson = f"### 📚 Learn {topic_slug.title()} (freeCodeCamp)\n"
            for a in articles[:3]:
                title = a.text.strip()
                link = a["href"]
                lesson += f"- [{title}]({link})\n"

            lesson += f"\n📺 Watch: [YouTube Tutorials for {topic_slug.title()}](https://www.youtube.com/results?search_query=learn+{topic_slug})"
            return lesson

        except Exception:
            return f"""### 🚧 Lesson Not Found
We couldn’t fetch a lesson for **{topic_slug}** right now.

📘 Browse articles: [freeCodeCamp {topic_slug.title()}](https://www.freecodecamp.org/news/tag/{topic_slug}/)
📺 Watch: [YouTube Tutorials](https://www.youtube.com/results?search_query=learn+{topic_slug})
"""

        return None

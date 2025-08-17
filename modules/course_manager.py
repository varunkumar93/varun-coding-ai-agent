import requests
from bs4 import BeautifulSoup

class ProgramizCourseManager:
    def get_lesson_content(self, language, topic_slug):
        if topic_slug == "variables-data-types":
            return "### 📘 Variables and Data Types (Python)\n\n📘 Read: [freeCodeCamp Python Guide](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/)\n📺 Watch: [Python Full Course](https://www.youtube.com/watch?v=rfscVS0vtbw)"

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
            return f"### 🚧 Lesson Not Found\nWe couldn’t fetch a lesson for **{topic_slug}** right now.\n\n📘 Browse articles: [freeCodeCamp {topic_slug.title()}](https://www.freecodecamp.org/news/tag/{topic_slug}/)\n📺 Watch: [YouTube Tutorials](https://www.youtube.com/results?search_query=learn+{topic_slug})"

    def get_practice_block(self, topic_slug):
        if topic_slug == "variables-data-types":
            return {
                "prompt": "### 🧪 Practice: Variables and Data Types\n\n**Task:** Create a variable `name` with your name and print it.\n\n```python\n# Your code here\n```",
                "expected_output": "Varun"
            }

        elif topic_slug == "java":
            return {
                "prompt": "### 🧪 Practice: Java Basics\n\n**Task:** Print \"Hello, Java!\" using System.out.println.\n\n```java\n// Your code here\n```",
                "expected_output": "Hello, Java!"
            }

        elif topic_slug == "javascript":
            return {
                "prompt": "### 🧪 Practice: JavaScript Basics\n\n**Task:** Log \"Hello, JS!\" to the console.\n\n```javascript\n// Your code here\n```",
                "expected_output": "Hello, JS!"
            }

        else:
            return {
                "prompt": "🧪 Practice block not available for this topic yet.",
                "expected_output": None
            }

    def evaluate_code(self, user_output, expected_output):
        return "✅ Correct!" if user_output.strip() == expected_output else "❌ Wrong. Try again."

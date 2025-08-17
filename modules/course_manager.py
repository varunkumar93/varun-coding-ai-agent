import requests
from bs4 import BeautifulSoup

class ProgramizCourseManager:
    def get_lesson_content(self, language, topic_slug):
        # ✅ Try predefined lessons first
        if topic_slug == "variables-data-types":
            return """### 📘 Variables and Data Types (freeCodeCamp)
Variables store data. Data types define the kind of data.

**Examples:**
    x = 5        # Integer
    name = "AI"  # String

📺 Watch: Learn Python Full Course
https://www.youtube.com/watch?v=rfscVS0vtbw

📘 Read: freeCodeCamp Python Guide
https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/
"""

        # ✅ Fallback: Scrape freeCodeCamp tag page
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

            # ✅ Embed YouTube search link
            lesson += f"\n📺 Watch: [YouTube Tutorials for {topic_slug.title()}](https://www.youtube.com/results?search_query=learn+{topic_slug})"
            return lesson

        except Exception:
            # ✅ Final fallback: just link to tag page
            return f"""### 🚧 Lesson Not Found
We don’t have a custom lesson for **{topic_slug}** yet.

📘 Explore freeCodeCamp’s articles:
https://www.freecodecamp.org/news/tag/{topic_slug}/

📺 Watch: [YouTube Tutorials for {topic_slug.title()}](https://www.youtube.com/results?search_query=learn+{topic_slug})
"""

        return None

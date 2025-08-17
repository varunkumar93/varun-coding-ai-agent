import requests
from bs4 import BeautifulSoup

class ProgramizCourseManager:
    BASE_URL = "https://www.programiz.com"

    def get_lesson_content(self, language, topic):
        url_map = {
            "Python": f"{self.BASE_URL}/python-programming/{topic}",
            "C": f"{self.BASE_URL}/c-programming/{topic}",
            "Java": f"{self.BASE_URL}/java-programming/{topic}",
            "JavaScript": f"{self.BASE_URL}/javascript/{topic}"
        }

        url = url_map.get(language)
        if not url:
            return "❌ Language not supported yet."

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            content = soup.find("div", class_="content")
            if content:
                return content.get_text(strip=True)[:2000]
            else:
                return "⚠️ Lesson content not found on Programiz. Try another topic or check the URL."
        except Exception as e:
            return f"⚠️ Error fetching lesson: {e}"

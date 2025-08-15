import pandas as pd

class FileHandler:
    def summarize(self, file):
        if file.type == "text/plain":
            content = file.read().decode("utf-8")
            return f"Text file preview:\n{content[:300]}"
        elif file.type == "text/csv":
            df = pd.read_csv(file)
            return f"CSV with {len(df)} rows and columns: {', '.join(df.columns)}"
        else:
            return "Unsupported file type."

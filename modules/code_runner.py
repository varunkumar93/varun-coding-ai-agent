import io
import contextlib

class CodeRunner:
    def run_code(self, code):
        output = io.StringIO()
        try:
            with contextlib.redirect_stdout(output):
                exec(code, {})
            return output.getvalue()
        except Exception as e:
            return f"Error: {str(e)}"

import importlib
import pkg_resources
import streamlit as st

# Define expected versions
EXPECTED = {
    "langchain": "0.1.16",
    "langchain_community": "0.0.17",
    "langchain_core": "0.1.35",
    "groq": None,  # Optional: add version if needed
}

def check_versions():
    mismatches = []
    for pkg, expected in EXPECTED.items():
        try:
            module = importlib.import_module(pkg.replace("-", "_"))
            installed = pkg_resources.get_distribution(pkg).version
            if expected and installed != expected:
                mismatches.append(f"❌ {pkg}: expected {expected}, found {installed}")
            else:
                st.sidebar.success(f"✅ {pkg}: {installed}")
        except Exception as e:
            mismatches.append(f"⚠️ {pkg}: not found or error - {str(e)}")

    if mismatches:
        st.sidebar.warning("⚠️ Version mismatches detected:")
        for msg in mismatches:
            st.sidebar.text(msg)
    else:
        st.sidebar.success("✅ All critical versions match expected values.")

# Run check on app startup
check_versions()

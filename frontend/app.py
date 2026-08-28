import streamlit as st

st.set_page_config(page_title="Food Bank Dashboard", layout="wide")

navigation = st.navigation(
    [
        st.Page("pages/dashboard.py", title="Dashboard", default=True),
        st.Page("pages/centers.py", title="Distribution Centers"),
        st.Page("pages/history.py", title="Distribution History"),
    ]
)
navigation.run()

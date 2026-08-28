import streamlit as st
def dashboard_page():
    st.title("Dashboard")
    if st.button("Go to page 2"):
        st.switch_page(page2)

def page2_page():
    st.title("Page 2")
    if st.button("Go to dashboard"):
        st.switch_page(dashboard)

dashboard = st.Page(dashboard_page, title="Dashboard", default=True)
page2 = st.Page(page2_page, title="Page 2")
st.navigation([dashboard, page2]).run()

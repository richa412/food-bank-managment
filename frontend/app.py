import streamlit as st

from components.product_form import product_form
from components.product_list import product_list


st.title("Inventory Management")

product_form()

st.divider()

product_list()
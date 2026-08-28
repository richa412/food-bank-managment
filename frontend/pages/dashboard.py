import streamlit as st

from components.distribution_form import distribution_form
from components.food_inventory import add_food_form, current_inventory

st.title("Food Bank Inventory & Distribution")
st.caption("Add donated food and record distributions from one workspace.")

add_column, distribute_column = st.columns(2, gap="large")
with add_column:
    add_food_form()
with distribute_column:
    distribution_form()

st.divider()
current_inventory()

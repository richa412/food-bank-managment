import streamlit as st
from services.api import get_all_products, delete_product


def set_edit_product(product):
    # Streamlit keeps widget values in session state. Update those values in
    # the button callback so the form is prefilled before its widgets render.
    st.session_state.edit_product = product.copy()
    st.session_state.name_input = product["name"]
    st.session_state.desc_input = product["description"]
    st.session_state.price_input = float(product["price"])
    st.session_state.qty_input = int(product["quantity"])

def product_list():

    st.header("Product List")

    products = get_all_products()

    # Search
    search = st.text_input("Search Product", key="search_box")

    if search:
        products = [
            product
            for product in products
            if search.lower() in product["name"].lower()
        ]

    # Header
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    col1.write("ID")
    col2.write("Name")
    col3.write("Description")
    col4.write("Price")
    col5.write("Quantity")
    col6.write("Edit")
    col7.write("Delete")

    # Products
    for serial_number, product in enumerate(products, start=1):

        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

        # This is the display serial number. An edit changes only the selected
        # product's details, so its position and serial stay the same.
        col1.write(serial_number)
        col2.write(product["name"])
        col3.write(product["description"])
        col4.write(product["price"])
        col5.write(product["quantity"])

        col6.button(
            "Edit", 
            key=f"edit_{product['id']}",
            on_click=set_edit_product,
            args=(product,)
        )
        col7.button(
            "Delete", 
            key=f"delete_{product['id']}", 
            on_click=delete_product, 
            args=(product['id'],)
        )

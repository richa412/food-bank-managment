import streamlit as st
from services.api import add_product, get_all_products, update_product

def clear_form_data():
    st.session_state.edit_product = None
    for key in ['name_input', 'desc_input', 'price_input', 'qty_input']:
        if key in st.session_state:
            del st.session_state[key]

def product_form():
    if st.session_state.pop("clear_product_form", False):
        clear_form_data()

    edit_mode = "edit_product" in st.session_state and st.session_state.edit_product is not None
    
    if edit_mode:
        st.header("Update Product")
        prod = st.session_state.edit_product
    else:
        st.header("Add Product")
        prod = {"name": "", "description": "", "price": None, "quantity": None}

    # Give new widgets their initial values. When Edit is clicked,
    # set_edit_product has already replaced these values with the selected
    # product before this form is rendered.
    st.session_state.setdefault("name_input", prod["name"])
    st.session_state.setdefault("desc_input", prod["description"])
    st.session_state.setdefault(
        "price_input", float(prod["price"]) if prod["price"] is not None else 0.0
    )
    st.session_state.setdefault(
        "qty_input", int(prod["quantity"]) if prod["quantity"] is not None else 0
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        name = st.text_input("Product Name", key="name_input")

    with col2:
        description = st.text_input("Description", key="desc_input")

    with col3:
        price = st.number_input(
            "Price",
            min_value=0.0,
            step=1.0,
            key="price_input"
        )

    with col4:
        quantity = st.number_input(
            "Quantity",
            min_value=0,
            step=1,
            key="qty_input"
        )

    with col5:
        st.write("")
        if edit_mode:
            submit_button = st.button("Update Product")
        else:
            submit_button = st.button("Add Product")

    if submit_button:
        if edit_mode:
            updated_data = {
                "id": prod["id"],
                "name": name,
                "description": description,
                "price": price if price is not None else 0.0,
                "quantity": quantity if quantity is not None else 0
            }
            if update_product(prod["id"], updated_data):
                st.success("Product updated successfully!")
                st.session_state.clear_product_form = True
                st.rerun()
            else:
                st.error("Failed to update product.")
        else:
            current_products = get_all_products()
            new_id = max([p.get("id", 0) for p in current_products], default=0) + 1
            new_product = {
                "id": new_id,
                "name": name,
                "description": description,
                "price": price if price is not None else 0.0,
                "quantity": quantity if quantity is not None else 0
            }

            if add_product(new_product):
                st.success("Product added successfully!")
                st.session_state.clear_product_form = True
                st.rerun()
            else:
                st.error("Failed to add product.")

from datetime import date, timedelta

import streamlit as st

from services.api import add_food, delete_food, get_all_foods, update_food


def _food_payload(name, category, quantity, unit, expiry_date, donor):
    return {
        "name": name.strip(),
        "category": category.strip(),
        "quantity": quantity,
        "unit": unit.strip(),
        "expiry_date": expiry_date,
        "donor": donor.strip(),
    }


def _clear_food_form():
    st.session_state.pop("edit_food_id", None)
    for key in (
        "food_name",
        "food_category",
        "food_quantity",
        "food_unit",
        "food_expiry_date",
        "food_donor",
    ):
        st.session_state.pop(key, None)


def _start_edit(food):
    st.session_state.edit_food_id = food["id"]
    st.session_state.food_name = food["name"]
    st.session_state.food_category = food["category"]
    st.session_state.food_quantity = food["quantity"]
    st.session_state.food_unit = food["unit"]
    st.session_state.food_expiry_date = food["expiry_date"]
    st.session_state.food_donor = food["donor"]


def _delete_food(food_id):
    success, error_message = delete_food(food_id)
    if success:
        if st.session_state.get("edit_food_id") == food_id:
            st.session_state.clear_food_form = True
        st.session_state.inventory_message = "Food deleted successfully!"
    else:
        st.session_state.inventory_error = error_message


def add_food_form():
    if st.session_state.pop("clear_food_form", False):
        _clear_food_form()

    if message := st.session_state.pop("food_success", None):
        st.success(message)

    edit_food_id = st.session_state.get("edit_food_id")
    form_title = "Update Food" if edit_food_id is not None else "Add Food"

    st.subheader(form_title)
    with st.form("food_form", clear_on_submit=False):
        name = st.text_input("Food Name", key="food_name")
        category = st.text_input("Category", key="food_category")
        quantity = st.number_input("Quantity", min_value=0, step=1, key="food_quantity")
        unit = st.text_input("Unit", placeholder="e.g. kg, packets, cans", key="food_unit")
        expiry_date = st.text_input("Expiry Date", placeholder="YYYY-MM-DD", key="food_expiry_date")
        donor = st.text_input("Donor", key="food_donor")
        submitted = st.form_submit_button(form_title)

    if submitted:
        if not all([name.strip(), category.strip(), unit.strip(), expiry_date.strip(), donor.strip()]):
            st.error("Please complete all food fields.")
        else:
            try:
                date.fromisoformat(expiry_date)
            except ValueError:
                st.error("Expiry Date must use YYYY-MM-DD format.")
            else:
                payload = _food_payload(name, category, quantity, unit, expiry_date, donor)
                if edit_food_id is None:
                    success, error_message = add_food(payload)
                    success_message = "Food added successfully!"
                else:
                    success, error_message = update_food(edit_food_id, payload)
                    success_message = "Food updated successfully!"
                if success:
                    st.session_state.food_success = success_message
                    st.session_state.clear_food_form = True
                    st.rerun()
                else:
                    st.error(error_message)



def current_inventory():
    if message := st.session_state.pop("inventory_message", None):
        st.success(message)
    if error_message := st.session_state.pop("inventory_error", None):
        st.error(error_message)

    st.subheader("Current Inventory")
    today = date.today()
    expiry_window_end = today + timedelta(days=7)
    foods = get_all_foods()
    inventory = []
    expiring_soon = []

    for food in foods:
        expiry_date = date.fromisoformat(food["expiry_date"])

        inventory.append(
            {
                "Food": food["name"],
                "Category": food["category"],
                "Quantity": food["quantity"],
                "Unit": food["unit"],
            }
        )

        if today <= expiry_date <= expiry_window_end:
            expiring_soon.append(
                {
                    "Food": food["name"],
                    "Quantity": food["quantity"],
                    "Unit": food["unit"],
                    "Expiry Date": expiry_date.isoformat(),
                }
            )

    if inventory:
        food_column, category_column, quantity_column, unit_column, edit_column, delete_column = st.columns(6)
        food_column.write("**Food**")
        category_column.write("**Category**")
        quantity_column.write("**Quantity**")
        unit_column.write("**Unit**")
        edit_column.write("**Edit**")
        delete_column.write("**Delete**")

        for food in foods:
            food_column, category_column, quantity_column, unit_column, edit_column, delete_column = st.columns(6)
            food_column.write(food["name"])
            category_column.write(food["category"])
            quantity_column.write(food["quantity"])
            unit_column.write(food["unit"])
            edit_column.button(
                "Edit",
                key=f"edit_food_{food['id']}",
                on_click=_start_edit,
                args=(food,),
            )
            delete_column.button(
                "Delete",
                key=f"delete_food_{food['id']}",
                on_click=_delete_food,
                args=(food["id"],),
            )
    else:
        st.info("No food items found.")

    with st.container(border=True):
        st.subheader("Expiring Soon")
        if expiring_soon:
            st.dataframe(expiring_soon, width="stretch", hide_index=True)
        else:
            st.info("No food expiring soon.")

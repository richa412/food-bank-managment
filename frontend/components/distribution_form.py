import streamlit as st

from services.api import create_distribution, get_all_centers, get_all_foods


def _clear_distribution_form():
    for key in ("dist_food", "dist_center", "dist_quantity"):
        st.session_state.pop(key, None)


def distribution_form():
    if st.session_state.pop("clear_dist_form", False):
        _clear_distribution_form()

    if st.session_state.pop("distribution_success", False):
        st.success("Distribution recorded successfully!")

    st.subheader("Distribute Food")

    foods = get_all_foods()
    centers = get_all_centers()

    if not foods or not centers:
        st.info("Add at least one food item and distribution center before recording a distribution.")
        return

    food = st.selectbox("Food", foods, format_func=lambda item: item["name"], key="dist_food")
    st.caption(f"Available quantity: {food['quantity']} {food['unit']}")
    center = st.selectbox(
        "Distribution Center", centers, format_func=lambda item: item["name"], key="dist_center"
    )

    with st.form("distribution_form"):
        quantity = st.number_input("Quantity", min_value=1, step=1, key="dist_quantity")
        submit_button = st.form_submit_button("Distribute")

    if submit_button:
        success, error_message = create_distribution(
            {
                "food_id": food["id"],
                "center_id": center["id"],
                "quantity": quantity,
            }
        )
        if success:
            st.session_state.distribution_success = True
            st.session_state.clear_dist_form = True
            st.rerun()
        else:
            st.error(error_message)

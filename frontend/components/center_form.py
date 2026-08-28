import streamlit as st

from services.api import add_center, delete_center, get_all_centers


def center_form():
    st.title("Distribution Centers")
    st.caption("Add and review partner locations for food distribution.")

    with st.form("add_center_form", clear_on_submit=True):
        center_name = st.text_input("Center Name")
        submit_button = st.form_submit_button("Add Center")

    if submit_button:
        if not center_name.strip():
            st.error("Center name is required.")
        else:
            success, error_message = add_center({"name": center_name.strip()})
            if success:
                st.toast("Center added successfully!")
                st.switch_page("pages/dashboard.py")
            else:
                st.error(error_message)

    st.subheader("Existing Centers")
    centers = get_all_centers()
    if centers:
        name_column, action_column = st.columns([5, 1])
        name_column.write("**Center Name**")
        action_column.write("**Action**")

        for center in centers:
            name_column, action_column = st.columns([5, 1])
            name_column.write(center["name"])
            if action_column.button("Delete", key=f"delete_center_{center['id']}"):
                success, error_message = delete_center(center["id"])
                if success:
                    st.rerun()
                else:
                    st.error(error_message)
    else:
        st.info("No distribution centers found.")

import streamlit as st

from services.api import get_all_centers, get_all_distributions, get_all_foods


def distribution_history_page():
    st.title("Distribution History")
    st.caption("Review all recorded food distributions.")

    foods = {food["id"]: food["name"] for food in get_all_foods()}
    centers = {center["id"]: center["name"] for center in get_all_centers()}
    distributions = get_all_distributions()

    history = [
        {
            "Food": foods.get(item["food_id"], "Unknown food"),
            "Distribution Center": centers.get(item["center_id"], "Unknown center"),
            "Quantity": item["quantity"],
            "Distributed At": item["distributed_at"],
        }
        for item in distributions
    ]

    if history:
        st.dataframe(history, width="stretch", hide_index=True)
    else:
        st.info("No distributions have been recorded yet.")

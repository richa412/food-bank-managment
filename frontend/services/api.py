import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("API_URL", "http://localhost:8000")

@st.cache_data(show_spinner=False)
def get_all_centers():
    response = requests.get(f"{BASE_URL}/centers")
    if response.status_code == 200:
        return response.json()
    return []


def add_center(center_data):
    response = requests.post(f"{BASE_URL}/centers", json=center_data)
    if response.status_code == 201:
        get_all_centers.clear()
        return True, None
    return False, _error_detail(response)


def delete_center(center_id):
    response = requests.delete(f"{BASE_URL}/centers/{center_id}")
    if response.status_code == 204:
        get_all_centers.clear()
        return True, None
    return False, _error_detail(response)


def get_all_foods():
    response = requests.get(f"{BASE_URL}/foods")
    if response.status_code == 200:
        return response.json()
    return []


def add_food(food_data):
    response = requests.post(f"{BASE_URL}/foods", json=food_data)
    if response.status_code == 201:
        return True, None
    return False, _error_detail(response)


def update_food(food_id, food_data):
    response = requests.put(f"{BASE_URL}/foods/{food_id}", json=food_data)
    if response.status_code == 200:
        return True, None
    return False, _error_detail(response)


def delete_food(food_id):
    response = requests.delete(f"{BASE_URL}/foods/{food_id}")
    if response.status_code == 204:
        return True, None
    return False, _error_detail(response)


def create_distribution(distribution_data):
    response = requests.post(f"{BASE_URL}/distributions", json=distribution_data)
    if response.status_code == 201:
        get_all_distributions.clear()
        return True, None

    return False, _error_detail(response)


@st.cache_data(show_spinner=False)
def get_all_distributions():
    response = requests.get(f"{BASE_URL}/distributions")
    if response.status_code == 200:
        return response.json()
    return []


def _error_detail(response):
    try:
        detail = response.json().get("detail", "Failed to record distribution.")
    except ValueError:
        detail = "The request could not be completed."
    return str(detail)

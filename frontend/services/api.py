import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("API_URL", "http://localhost:8000")

@st.cache_data(show_spinner=False)
def get_all_products():
    response = requests.get(f"{BASE_URL}/products")
    if response.status_code == 200:
        return response.json()
    return []

def add_product(product_data):
    response = requests.post(f"{BASE_URL}/product", json=product_data)
    if response.status_code == 200:
        get_all_products.clear() # Clear cache so new product shows up
        return True
    return False

def update_product(product_id, product_data):
    response = requests.put(f"{BASE_URL}/product", params={"id": product_id}, json=product_data)
    if response.status_code == 200:
        get_all_products.clear() # Clear cache so updated product shows up
        return True
    return False

def delete_product(product_id):
    response = requests.delete(f"{BASE_URL}/product", params={"id": product_id})
    if response.status_code == 200:
        get_all_products.clear() # Clear cache so deleted product is removed
        return True
    return False

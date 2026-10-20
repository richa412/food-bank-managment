# Inventory Management System

A full-stack Inventory Management application built with **FastAPI** (Backend) and **Streamlit** (Frontend), using a **PostgreSQL** database.

## Features
- **Add Products:** Quickly add new products to your inventory.
- **View Products:** See all your products in a clean, sequential table.
- **Update Products:** Edit existing product details (Name, Description, Price, Quantity).
- **Delete Products:** Remove products from the inventory.
- **Search:** Search for specific products by name.
- **Real-time Sync:** The frontend connects to the backend API seamlessly.

## Tech Stack
- **Frontend:** Streamlit (Python)
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Environment Management:** python-dotenv

## Setup Instructions

### 1. Prerequisites
- Python 3.8+
- PostgreSQL installed and running locally

### 2. Environment Variables
Create a `.env` file in the root of the project and add your database and API URLs:
```env
DATABASE_URL="postgresql://username:password@localhost:5432/inventory_db"
API_URL="http://localhost:8000"
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Backend (FastAPI)
```bash
cd backend
uvicorn main:app --reload
```
The backend API will be available at `http://localhost:8000`

### 5. Run the Frontend (Streamlit)
Open a new terminal and run:
```bash
cd frontend
streamlit run app.py
```
The frontend UI will be available at `http://localhost:8501`

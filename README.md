# Food Bank Management System

A full-stack Food Bank Management application built with **FastAPI** (Backend) and **Streamlit** (Frontend), utilizing a **PostgreSQL** database with **SQLAlchemy** ORM and **Alembic** for migrations.

## Features

### Food Inventory Management
- **Add Food:** Add donated food to the inventory tracking Name, Category, Quantity, Unit (e.g., kg, packets), Expiry Date, and Donor.
- **View Inventory:** See all current food items in the dashboard.
- **Edit/Delete Food:** Inline options to update food details or remove them completely from the inventory.
- **Expiring Soon Alert:** Automatically calculates and displays food items that will expire within the next 7 days in a dedicated table.

### Distribution Management
- **Distribution Centers:** Add and delete distribution centers from the system.
- **Distribute Food:** Record food distributions by selecting from available inventory and registered distribution centers. The system automatically validates available quantity and deducts distributed amounts from the inventory.
- **Distribution History:** View a complete log of all past food distributions.

## Tech Stack
- **Frontend:** Streamlit (Python)
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Database Migrations:** Alembic
- **Environment Management:** python-dotenv

## Project Structure
- `backend/`: FastAPI application containing routing (`routes/`), database models (`database_models.py`), schemas (`schemas.py`), and Alembic configurations.
- `frontend/`: Streamlit application containing the main entry point (`app.py`), individual pages (`pages/`), components (`components/`), and API service interactions.

## Application Workflow
The frontend Streamlit app is divided into three main pages:
1. **Dashboard:** The central workspace. Includes the "Add Food" form, "Distribute Food" form, "Current Inventory" list, and the "Expiring Soon" alert table. 
   *(Note: Food and center dropdowns in the distribution form are dynamically populated from real backend data).*
2. **Distribution Centers:** A dedicated page to manage (view, add, delete) the distribution centers.
3. **Distribution History:** A read-only page to view all recorded food distributions.

## Database Models
- `Product`: Tracks food items (`id`, `name`, `category`, `quantity`, `unit`, `expiry_date`, `donor`).
- `DistributionCenter`: Tracks centers (`id`, `name`).
- `Distribution`: Tracks distribution records (`id`, `food_id`, `center_id`, `quantity`, `distributed_at`).

## API Endpoints
The backend provides the following RESTful endpoints:
- **Foods (`/foods`)**
  - `GET /foods`: Get all food items.
  - `POST /foods`: Add a new food item.
  - `PUT /foods/{id}`: Update an existing food item.
  - `DELETE /foods/{id}`: Delete a food item.
- **Centers (`/centers`)**
  - `GET /centers`: Get all distribution centers.
  - `POST /centers`: Add a new distribution center.
  - `DELETE /centers/{id}`: Delete a distribution center.
- **Distributions (`/distributions`)**
  - `GET /distributions`: Get all distribution history.
  - `POST /distributions`: Record a new distribution (updates food quantity automatically).

## Setup Instructions

### 1. Prerequisites
- Python 3.8+
- PostgreSQL installed and running locally.

### 2. Environment Variables
Create a `.env` file in the root of the project with the following keys:
```env
DATABASE_URL="postgresql://username:password@localhost:5432/foodbank_db"
API_URL="http://localhost:8000"
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
Ensure your PostgreSQL server is running and the database specified in `.env` exists. Apply the Alembic migrations to create tables:
```bash
cd backend
alembic upgrade head
cd ..
```

### 5. Run the Backend (FastAPI)
Open a terminal and start the FastAPI server:
```bash
cd backend
uvicorn main:app --reload
```
The backend API will be available at `http://localhost:8000`.

### 6. Run the Frontend (Streamlit)
Open a new terminal and start the Streamlit app:
```bash
cd frontend
streamlit run app.py
```
The frontend UI will be available at `http://localhost:8501`.

# 🏢 Leave Management System

A full-stack **Leave Management System** developed using **FastAPI, PostgreSQL, SQLAlchemy, Pydantic, and Streamlit**. The application allows employees to submit leave requests and supports managing leave status through backend APIs.

## 📌 Problem Statement

In organizations, managing employee leave requests manually can be difficult and time-consuming. This project provides a simple digital system where employee details and leave requests can be stored, viewed, and managed efficiently.

## 🛠️ Technologies Used

* **Python** – Core programming language
* **FastAPI** – Backend REST API development
* **PostgreSQL** – Database for storing users and leave requests
* **SQLAlchemy** – ORM for interacting with PostgreSQL using Python
* **Pydantic** – Request data validation
* **Streamlit** – User-friendly frontend interface
* **Swagger UI** – API testing and documentation

## ⚙️ Project Workflow

1. User information is created and stored in PostgreSQL.
2. Employees can submit leave requests.
3. Leave information is stored in the database.
4. Leave requests can be retrieved through FastAPI endpoints.
5. Leave status can be updated to **Approved** or **Rejected**.
6. Streamlit provides a simple frontend for interacting with the system.

## 🚀 Features

* Create and view users
* Submit employee leave requests
* View all leave requests
* Update leave status
* PostgreSQL database integration
* REST API implementation using FastAPI
* Interactive Streamlit frontend

## 🔗 API Endpoints

| Method | Endpoint            | Purpose                |
| ------ | ------------------- | ---------------------- |
| GET    | `/users/`           | View all users         |
| POST   | `/users/`           | Create a new user      |
| POST   | `/leave/`           | Submit a leave request |
| GET    | `/leaves/`          | View leave requests    |
| PUT    | `/leave/{leave_id}` | Update leave status    |

## 📂 Project Structure

```text
Leave_Management_1/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── streamlit_app.py
├── requirements.txt
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/shanigalanikitha/Leave_Management_1.git
cd Leave_Management_1
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure PostgreSQL

Create a PostgreSQL database:

```text
leave_db
```

Configure your database connection in the backend configuration.

### 6. Run FastAPI backend

```bash
uvicorn main:app --reload
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

### 7. Run Streamlit frontend

```bash
streamlit run streamlit_app.py
```

## 🔄 Leave Workflow

```text
Employee
   ↓
Apply for Leave
   ↓
FastAPI
   ↓
Pydantic Validation
   ↓
SQLAlchemy
   ↓
PostgreSQL
   ↓
Pending → Approved / Rejected
```

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

* Building REST APIs using FastAPI
* Integrating PostgreSQL with Python
* Using SQLAlchemy ORM for database operations
* Validating API requests using Pydantic
* Implementing CRUD operations
* Connecting frontend and backend applications
* Testing REST APIs using Swagger UI

## 👩‍💻 Author

**Shanigala Nikitha Yadav**

B.Tech Computer Science Engineering

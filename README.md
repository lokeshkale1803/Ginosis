# 🎓 Student Management System — Ginosis Training Project

A simple full-stack **Student Management System** developed during the **Ginosis College Training Program**.

The project demonstrates how a frontend application communicates with a backend REST API and how the backend performs database operations using **Supabase**.

The system allows users to **add, view, update, and delete student records**.

---

## 📌 Project Overview

This project was created as part of our college Ginosis training to understand the practical implementation of:

* Python Programming
* FastAPI
* REST APIs
* CRUD Operations
* Supabase Database
* Frontend & Backend Integration
* API Testing using Swagger UI
* Deployment using Railway

The application stores student information such as:

* Student Name
* Course
* Marks

---

## ✨ Features

### ➕ Add Student

Add a new student by entering:

* Name
* Course
* Marks

### 👀 View Students

Display all student records stored in the Supabase database.

### ✏️ Update Student

Update the course and marks of an existing student.

### 🗑️ Delete Student

Delete a student record from the database.

### ☁️ Cloud Database

Student information is stored using **Supabase PostgreSQL Database**.

### 🔗 REST API

Frontend communicates with the backend through FastAPI REST endpoints.

---

## 🛠️ Technologies Used

| Technology   | Purpose                     |
| ------------ | --------------------------- |
| Python       | Backend Programming         |
| FastAPI      | REST API Development        |
| Supabase     | Cloud Database              |
| PostgreSQL   | Database                    |
| HTML         | Web Structure               |
| CSS          | Frontend Styling            |
| JavaScript   | Frontend Logic & API Calls  |
| Gradio       | Python-based User Interface |
| Uvicorn      | FastAPI Server              |
| Swagger UI   | API Testing                 |
| Railway      | Backend Deployment          |
| Git & GitHub | Version Control             |

---

## 📂 Project Structure

```text
Ginosis/
│
├── backend/
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── index.html
├── styles.css
├── script.js
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

### Backend

`backend/main.py`

Contains the FastAPI application and CRUD API endpoints.

### Web Frontend

```text
index.html
styles.css
script.js
```

Provides a browser-based user interface for managing students.

### Gradio Frontend

`frontend/app.py`

Provides an alternative Python-based graphical interface using Gradio.

---

## 🔄 CRUD Operations

The application supports four basic database operations:

| Operation      | Method | Endpoint                   |
| -------------- | ------ | -------------------------- |
| Create Student | POST   | `/students`                |
| Get Students   | GET    | `/students`                |
| Update Student | PUT    | `/students/{student_name}` |
| Delete Student | DELETE | `/students/{student_name}` |

---

## 🔌 API Endpoints

### Create Student

```http
POST /students
```

Parameters:

```text
name
course
marks
```

---

### Get All Students

```http
GET /students
```

Returns all students stored in the database.

---

### Update Student

```http
PUT /students/{student_name}
```

Updates:

```text
course
marks
```

---

### Delete Student

```http
DELETE /students/{student_name}
```

Deletes the selected student from the database.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/lokeshkale1803/Ginosis.git
```

Move inside the project:

```bash
cd Ginosis
```

---

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The project uses packages including:

```text
fastapi
uvicorn
supabase
python-dotenv
gradio
requests
```

---

## 🔐 Environment Variables

Create a `.env` file in the project directory.

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_key
```

> Never upload your real `.env` file or private API keys to GitHub.

Use `.env.example` to show which environment variables are required.

---

## ▶️ Run FastAPI Backend

Run:

```bash
python -m uvicorn backend.main:app --reload
```

Backend will normally start at:

```text
http://127.0.0.1:8000
```

---

## 📚 Swagger UI

FastAPI automatically provides interactive API documentation.

After starting the backend, open:

```text
http://127.0.0.1:8000/docs
```

From Swagger UI you can test:

* POST
* GET
* PUT
* DELETE

API endpoints directly from the browser.

---

## 🖥️ Run Gradio Frontend

Run:

```bash
python frontend/app.py
```

The Gradio application normally runs at:

```text
http://127.0.0.1:7860
```

---

## 🌐 Architecture

```text
User
  │
  ▼
Frontend
HTML / CSS / JavaScript / Gradio
  │
  │ HTTP Requests
  ▼
FastAPI Backend
  │
  │ Supabase Client
  ▼
Supabase PostgreSQL Database
```

---

## 🚀 Deployment

The FastAPI backend can be deployed using **Railway**.

The web frontend communicates with the deployed FastAPI API using HTTP requests.

This demonstrates a basic real-world full-stack architecture where the frontend, backend, and database work together.

---

## 🎯 Learning Outcomes

Through this project, we learned:

* Python fundamentals
* Backend development using FastAPI
* REST API concepts
* GET, POST, PUT and DELETE methods
* CRUD operations
* Connecting Python with Supabase
* Working with environment variables
* Testing APIs using Swagger UI
* Connecting frontend with backend APIs
* Using Git and GitHub
* Deploying backend applications

---

## 👨‍💻 Developer

**Lokesh Kale**

B.Tech Computer Science & Engineering

GitHub: **@lokeshkale1803**

---

## 📖 Training

This project was developed during the **Ginosis College Training Program** as a practical implementation of Python, FastAPI, database integration, frontend-backend communication and deployment.

---

## 📄 License

This project is created for **educational and learning purposes**.

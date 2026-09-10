from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# ROOT
@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Ginosis</title>
        </head>
        <body>
            <h1>Welcome to Ginosis</h1>
            <p>This is the API backend for Ginosis. Everything is up and running.</p>
        </body>
    </html>
    """


# CREATE
@app.post("/students")
def create_student(name: str, course: str, marks: int):
    student = {
        "name": name,
        "course": course,
        "marks": marks
    }

    response = (
        supabase.table("students")
        .insert(student)
        .execute()
    )

    return {
        "message": "Student created successfully",
        "data": response.data
    }


# READ
@app.get("/students")
def get_students():
    response = (
        supabase.table("students")
        .select("*")
        .execute()
    )

    return {
        "data": response.data
    }


# UPDATE
@app.put("/students/{student_name}")
def update_student(student_name: str, course: str, marks: int):
    updated_data = {
        "course": course,
        "marks": marks
    }

    response = (
        supabase.table("students")
        .update(updated_data)
        .eq("name", student_name)
        .execute()
    )

    if response.data:
        return {
            "message": "Student updated successfully",
            "data": response.data
        }

    return {"message": "Student not found"}


# DELETE
@app.delete("/students/{student_name}")
def delete_student(student_name: str):
    response = (
        supabase.table("students")
        .delete()
        .eq("name", student_name)
        .execute()
    )

    if response.data:
        return {
            "message": "Student deleted successfully",
            "data": response.data
        }

    return {"message": "Student not found"}
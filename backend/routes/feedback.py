# Inside your FastAPI backend (main.py or feedback.py)

from fastapi import FastAPI, Form
from pydantic import BaseModel
import psycopg2  # PostgreSQL connection

app = FastAPI()

# PostgreSQL connection details (change according to your DB)
conn = psycopg2.connect(
    database="your_db_name",
    user="your_db_user",
    password="your_db_password",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Create feedback table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS feedback (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    message TEXT NOT NULL
)
""")
conn.commit()

@app.post("/submit-feedback")
async def submit_feedback(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    cur.execute("INSERT INTO feedback (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
    conn.commit()
    return {"message": "Feedback submitted successfully!"}

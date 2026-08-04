import os

import psycopg2
from flask import Flask, jsonify, request


app = Flask(__name__)


def database_config():
    return {
        "host": os.environ["DATABASE_HOST"],
        "port": os.environ.get("DATABASE_PORT", "5432"),
        "dbname": os.environ["POSTGRES_DB"],
        "user": os.environ["POSTGRES_USER"],
        "password": os.environ["POSTGRES_PASSWORD"],
    }


def get_connection():
    return psycopg2.connect(**database_config())


def initialize_database():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS tasks (
                    id SERIAL PRIMARY KEY,
                    title TEXT NOT NULL,
                    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
                );
                """
            )


@app.get("/health")
def health():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            cur.fetchone()
    return jsonify(status="ok")


@app.get("/tasks")
def list_tasks():
    initialize_database()
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, title, created_at FROM tasks ORDER BY id;")
            rows = cur.fetchall()

    return jsonify(
        tasks=[
            {"id": row[0], "title": row[1], "created_at": row[2].isoformat()}
            for row in rows
        ]
    )


@app.post("/tasks")
def create_task():
    initialize_database()
    payload = request.get_json(silent=True) or {}
    title = payload.get("title")

    if not title:
        return jsonify(error="title is required"), 400

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO tasks (title) VALUES (%s) RETURNING id, title, created_at;",
                (title,),
            )
            row = cur.fetchone()

    return (
        jsonify(id=row[0], title=row[1], created_at=row[2].isoformat()),
        201,
    )


initialize_database()



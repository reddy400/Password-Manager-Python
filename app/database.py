import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "password_manager.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vault (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT NOT NULL,
            username TEXT NOT NULL,
            encrypted_password TEXT NOT NULL,
            category TEXT,
            url TEXT,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def add_password(website, username, encrypted_password,
                 category="", url="", notes=""):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO vault
        (website, username, encrypted_password, category, url, notes)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        website,
        username,
        encrypted_password,
        category,
        url,
        notes
    ))

    connection.commit()
    connection.close()


def get_passwords(search=""):
    connection = get_connection()
    cursor = connection.cursor()

    if search:
        cursor.execute("""
            SELECT * FROM vault
            WHERE website LIKE ?
            OR username LIKE ?
            OR category LIKE ?
        """, (
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        ))
    else:
        cursor.execute("SELECT * FROM vault")

    results = cursor.fetchall()

    connection.close()

    return results


def delete_password(password_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM vault WHERE id = ?",
        (password_id,)
    )

    connection.commit()
    connection.close()
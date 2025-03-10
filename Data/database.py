import sqlite3

DB_NAME = "StudentRegistration.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

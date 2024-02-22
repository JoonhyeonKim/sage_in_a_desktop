# src/backend/db/db_utils.py
import sqlite3
from sqlite3 import Error

def create_connection(db_file="src/backend/db/sage_tasks.db"):
    """Create and return a database connection."""
    try:
        conn = sqlite3.connect(db_file)  # Adjust path as needed
        return conn
    except Error as e:
        print(e)

def execute_query(conn, query, args=()):
    """Execute a single query."""
    try:
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except Error as e:
        print(e)

def execute_read_query(conn, query, args=()):
    """Execute a read query, returning fetched results."""
    try:
        cursor = conn.cursor()
        cursor.execute(query, args)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(e)
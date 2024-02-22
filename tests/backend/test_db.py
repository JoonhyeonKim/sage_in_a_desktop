# tests/backend/test_db.py
import sqlite3
from src.backend.db.db_utils import create_connection

def test_create_connection():
    test_db = "./test_sage_tasks.db"
    conn = create_connection(test_db)
    assert conn is not None
    conn.close()


# def test_create_table():
#     test_db = "./test_sage_tasks.db"
#     conn = create_connection(test_db)
#     # Assuming create_table function is defined similarly to create_connection
#     create_table(conn, """CREATE TABLE IF NOT EXISTS tasks (
#                           id integer PRIMARY KEY,
#                           title text NOT NULL,
#                           description text,
#                           due_date text,
#                           completed boolean NOT NULL);""")
#     cur = conn.cursor()
#     cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks';")
#     assert cur.fetchone() is not None
#     conn.close()

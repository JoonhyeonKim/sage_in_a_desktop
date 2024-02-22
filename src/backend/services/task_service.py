# src/backend/services/task_service.py
from ..db import db_utils

def add_task(title, description, due_date, completed=False):
    """Add a new task to the database."""
    query = """
    INSERT INTO
      tasks (title, description, due_date, completed)
    VALUES
      (?, ?, ?, ?);
    """
    conn = db_utils.create_connection()
    db_utils.execute_query(conn, query, (title, description, due_date, completed))
    conn.close()

def get_tasks():
    """Retrieve all tasks from the database."""
    query = "SELECT * FROM tasks;"
    conn = db_utils.create_connection()
    tasks = db_utils.execute_read_query(conn, query)
    conn.close()
    return tasks

def update_task(task_id, **kwargs):
    """Update task attributes based on task_id."""
    conn = db_utils.create_connection()
    for key, value in kwargs.items():
        query = f"UPDATE tasks SET {key} = ? WHERE id = ?"
        db_utils.execute_query(conn, query, (value, task_id))
    conn.close()

def delete_task(task_id):
    """Delete a task from the database."""
    query = "DELETE FROM tasks WHERE id = ?;"
    conn = db_utils.create_connection()
    db_utils.execute_query(conn, query, (task_id,))
    conn.close()

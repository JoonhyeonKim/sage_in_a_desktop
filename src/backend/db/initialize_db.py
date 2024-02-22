import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to an SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"SQLite version: {sqlite3.version}")
        return conn
    except Error as e:
        print(e)

def create_table(conn, create_table_sql):
    """Create a table from the create_table_sql statement"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = "src/backend/db/sage_tasks.db"

    sql_create_tasks_table = """ CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY,
                                        title text NOT NULL,
                                        description text,
                                        due_date text,
                                        completed boolean NOT NULL
                                    ); """

    # Create a database connection
    conn = create_connection(database)

    # Create tasks table
    if conn is not None:
        create_table(conn, sql_create_tasks_table)
        conn.close()
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
# import sqlite3
# This statement loads Python's built-in SQLite module.
# SQLite is a lightweight database engine stored in a local file,
# so you can create and manage databases without installing anything extra.

import sqlite3

# Example:
# sqlite3.connect("students.db") opens or creates a SQLite database file.
# A cursor is used to run SQL commands like CREATE TABLE, INSERT, SELECT.
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT)")
conn.commit()
conn.close()

# In short: import sqlite3 gives your Python program access to SQLite database tools.

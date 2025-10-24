import os
import sqlite3

# Hardcoded password (vulnerability)
ADMIN_PASSWORD = "admin123"

def login(user, password):
    if password == ADMIN_PASSWORD:
        print("Login successful")
    else:
        print("Invalid credentials")

# Command Injection vulnerability
def execute_command(cmd):
    os.system("echo " + cmd)

# SQL Injection vulnerability
def search_user(db_path, username):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cur.execute(query)
    conn.close()

if __name__ == "__main__":
    login("user", "admin123")
    execute_command("Hello")
    search_user(":memory:", "bob")

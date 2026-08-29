import sqlite3

def username_in_db(username):
    con = sqlite3.connect("C:\\Users\miran\PycharmProjects\IM-NEA\database\database.db")
    c = con.cursor()
    c.execute("SELECT * FROM account WHERE username = ?;", (username,))
    user_exists = bool(c.fetchone())
    con.close()
    return user_exists

def get_user(username):
    con = sqlite3.connect("C:\\Users\miran\PycharmProjects\IM-NEA\database\database.db")
    c = con.cursor()
    c.execute("SELECT * FROM account WHERE username = ?;", (username,))
    data = c.fetchone()
    con.close()
    return data

def add_user(username, email, hashed_password, salt):
    con = sqlite3.connect("C:\\Users\miran\PycharmProjects\IM-NEA\database\database.db")
    c = con.cursor()
    c.execute("INSERT INTO account (username, email, hashed_password, salt, locked) VALUES (?, ?, ?, ?, False);",
              (username, email, hashed_password, salt))
    con.commit()
    con.close()
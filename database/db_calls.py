import sqlite3

def username_in_db(username):
    con = sqlite3.connect("C:\\Users\miran\PycharmProjects\IM-NEA\database\database.db")
    c = con.cursor()
    c.execute("SELECT * FROM account WHERE username = ?;", (username,))
    user_exists = bool(c.fetchone())
    con.close()
    return user_exists

def get_details(username, data):
    con = sqlite3.connect("C:\\Users\miran\PycharmProjects\IM-NEA\database\database.db")
    c = con.cursor()
    c.execute("SELECT ? FROM account WHERE username = ?;", (data, username))
    data = c.fetchone()
    con.close()
    return data
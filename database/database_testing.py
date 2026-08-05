import sqlite3
import db_calls

con = sqlite3.connect("database.db")
c = con.cursor()

c.execute("SELECT * FROM account;", )
print(c.fetchall())
print(db_calls.username_in_db("existinguser1"))

con.close()
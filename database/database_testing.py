import sqlite3

con = sqlite3.connect('database.db')
c = con.cursor()

c.execute("SELECT * FROM account;", )
print(c.fetchall())

con.close()
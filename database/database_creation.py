import sqlite3

# define connection and cursor
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# create tables

# ACCOUNT TABLE
create_account = """
CREATE TABLE IF NOT EXISTS account(
account_id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
hashed_password TEXT,
salt TEXT,
locked INTEGER
)"""
cursor.execute(create_account)

# close connection
connection.commit()
connection.close()


# fill database (test data)

con = sqlite3.connect('database.db')
c = con.cursor()

add_accounts = [
    ("existinguser1", "2adab35acedea9f643c441921a70156c1280860ab22db8d85a9a2f5dc1f07776",
                             "31975e6429893d51f4eeecd793dc4235", False),
    ("janeSmith123", "61dbb73c56a7b89c7eda3fc7a71f5ebb6d3962b4450da2bcfb3c51807cf70c9a",
                            "a2597646e630b7905301ed9495f55796", True),
    ("marsjdriver", "f611bf33a30e39a21d3cd46bfe1e0bbde2179769f9c79d97a776520b86553e0b",
                           "eff83ac16979a3737bc1d0501a9b6a73", False),
    ("admin", "", "", False)
]
c.executemany("INSERT INTO account (username, hashed_password, salt, locked) VALUES(?, ?, ?, ?)", add_accounts)

con.commit()
con.close()
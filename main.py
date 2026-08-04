from GUI import gui

# CONSTANTS
homehost = "192.168.1.122"
schoolhost = "10.56.80.136"
localhost = "127.0.0.1"
dadhost = "127.0.1.1"
my_port = 13108

# TEST DATA

class Account:
    def __init__(self, newUsername, newHashedPassword, newSalt, newLocked):
        self.username = newUsername
        self.hashedpassword = newHashedPassword
        self.salt = newSalt
        self.locked = newLocked

# this represents my database
accounts = {
    "existinguser1": Account("existinguser1", "2adab35acedea9f643c441921a70156c1280860ab22db8d85a9a2f5dc1f07776",
                             "31975e6429893d51f4eeecd793dc4235", False),
    "janeSmith123": Account("janeSmith123", "61dbb73c56a7b89c7eda3fc7a71f5ebb6d3962b4450da2bcfb3c51807cf70c9a",
                            "a2597646e630b7905301ed9495f55796", True),
    "marsjdriver": Account("marsjdriver", "f611bf33a30e39a21d3cd46bfe1e0bbde2179769f9c79d97a776520b86553e0b",
                           "eff83ac16979a3737bc1d0501a9b6a73", False), "admin": Account("admin", "", "", False)
}

print(gui.GUI_signup_login(accounts, homehost, my_port))
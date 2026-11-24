from GUI import gui # my gui.py file

# CONSTANTS
HOMEHOST = "192.168.1.122"
SCHOOLHOST = "10.56.83.181"
LOCALHOST = "127.0.0.1"
GRANNYHOST = "192.168.1.138"
MARSHOST = "10.58.50.14"
MY_PORT = 13108

currenthost = SCHOOLHOST

# test data

class Account:
    def __init__(self, new_username, new_hashed_password, new_salt, new_locked):
        self.username = new_username
        self.hashed_password = new_hashed_password
        self.salt = new_salt
        self.locked = new_locked

# this represents my database
accounts = {
    "existinguser1": Account("existinguser1", "2adab35acedea9f643c441921a70156c1280860ab22db8d85a9a2f5dc1f07776", "31975e6429893d51f4eeecd793dc4235", False), # password: correctPassw0rd!
    "janeSmith123": Account("janeSmith123", "61dbb73c56a7b89c7eda3fc7a71f5ebb6d3962b4450da2bcfb3c51807cf70c9a", "a2597646e630b7905301ed9495f55796",True), # password: super_Secure123
    "marsjdriver": Account("marsjdriver", "f611bf33a30e39a21d3cd46bfe1e0bbde2179769f9c79d97a776520b86553e0b", "eff83ac16979a3737bc1d0501a9b6a73", False) # password: Tp1tmlltwfmiatsnwy!mb
}

gui.GUI_main(accounts, currenthost, MY_PORT)


#todo: working on getting messaging page to constantly update & changing texts on screen to be one scrollable thing
from GUI import gui # my gui.py file

# CONSTANTS
HOMEHOST = "192.168.1.122"
SCHOOLHOST = "10.56.83.181"
LOCALHOST = "127.0.0.1"
GRANNYHOST = "192.168.1.138"
MARSHOST = "10.58.50.14"
MY_PORT = 13108

currenthost = HOMEHOST

# test data

class Account:
    def __init__(self, new_username, new_hashed_password, new_salt, new_locked):
        self.username = new_username
        self.hashed_password = new_hashed_password
        self.salt = new_salt
        self.locked = new_locked

gui.GUI_main(currenthost, MY_PORT)

# accounts info for testing:
# existinguser1, correctPassw0rd!
# janeSmith123, super_Secure123, LOCKED
# marsjdriver, Tp1tmlltwfmiatsnwy!mb

# todo: improve database interaction, add dms, note: for finished product remove sending username to server
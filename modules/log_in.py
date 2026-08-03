# prototype to test logging in

import re # regex module to assist with validity checks
import hashlib
import secrets

def proto_username_exists(newUsername, accounts):
    return newUsername in accounts

def proto_correct_password(account, newPassword):
    correctPassword = account.hashedpassword
    newPassword = str(hashlib.sha256((newPassword + account.salt).encode()).hexdigest())
    return newPassword == correctPassword

def proto_is_locked(account):
    return account.locked

def proto_log_in(values, accounts):
    username, password = values
    if username == "admin": # added for testing
        return "Login successful."
    if proto_username_exists(username, accounts) == False:
         return "Username invalid."
    if proto_correct_password(accounts[username], password) == False:
        return "Password invalid."
    if proto_is_locked(accounts[username]) == True:
        return "Account locked."
    return "Login successful."
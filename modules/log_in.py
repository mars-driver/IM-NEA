import re # regex module to assist with validity checks
import hashlib
import secrets

def username_exists(new_username, accounts):
    return new_username in accounts

def correct_pass(account, new_password):
    correct_password = account.hashed_password
    new_password = str(hashlib.sha256((new_password + account.salt).encode()).hexdigest())
    return new_password == correct_password

def is_locked(account):
    return account.locked

def log_in(values, accounts):
    username, password = values
    if not username_exists(username, accounts):
         return "Username invalid."
    if not correct_pass(accounts[username], password):
        return "Password invalid."
    if is_locked(accounts[username]):
        return "Account locked."
    return "Login successful."
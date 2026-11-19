import re # regex module to assist with validity checks
import hashlib
import secrets

def username_exists(new_username, accounts):
    """
    returns whether or not a username already exists in the database
    """
    return new_username in accounts

def correct_pass(account, new_password):
    """
    salts and hashes the given password and returns whether or not it matches the corresponding one stored in the database for the given account
    """
    correct_password = account.hashed_password
    new_password = str(hashlib.sha256((new_password + account.salt).encode()).hexdigest())
    return new_password == correct_password

def is_locked(account):
    """
    returns whether or not the account is locked
    """
    return account.locked

def log_in(values, accounts):
    """
    takes in the values and the existing accounts and returns the result of a log in attempt
    """
    username, password = values
    if not username_exists(username, accounts):
         return "Username invalid."
    if not correct_pass(accounts[username], password):
        return "Password invalid."
    if is_locked(accounts[username]):
        return "Account locked."
    return "Login successful."
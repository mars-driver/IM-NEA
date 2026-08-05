# prototype to test logging in

import re # regex module to assist with validity checks
import hashlib
import secrets
from database import db_calls

def username_exists(new_username):
    return db_calls.username_in_db(new_username)

def correct_pass(username, new_password):
    correct_password = db_calls.get_details(username, "hashed_password")
    salt = db_calls.get_details(username, "salt")
    new_password = str(hashlib.sha256((new_password + salt).encode()).hexdigest())
    return new_password == correct_password

def is_locked(username):
    return db_calls.get_details(username, "locked")

def log_in(values):
    username, password = values
    if username == "admin": # added for testing
        return "Login successful."
    if not username_exists(username):
         return "Username invalid."
    if not correct_pass(username, password):
        return "Password invalid."
    if is_locked(username):
        return "Account locked."
    return "Login successful."
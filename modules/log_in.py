# prototype to test logging in

from database import db_calls
from modules.subroutines import generate_hashed_password

def username_exists(new_username):
    return db_calls.username_in_db(new_username)

def correct_pass(new_password, correct_password, salt):
    new_password = generate_hashed_password(new_password, salt)
    return new_password == correct_password

def log_in(values):
    username, password = values
    *discard, hashed_password, salt, locked = db_calls.get_user(username)
    if username == "admin": # added for testing
        return "Login successful."
    if not username_exists(username):
         return "Username invalid."
    if not correct_pass(password, hashed_password, salt):
        return "Password invalid."
    if locked:
        return "Account locked."
    return "Login successful."
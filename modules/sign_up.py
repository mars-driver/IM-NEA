from re import search # regex module to assist with validity checks
from secrets import token_hex # module to generate cryptographically secure numbers
from modules.subroutines import generate_hashed_password
from database import db_calls

def valid_new_username(new_username):
    print(new_username)
    return new_username.isalnum() and not db_calls.username_in_db(new_username)

def valid_email(new_email):
    new_email = new_email.split("@")
    if len(new_email) != 2:
        return False
    if "." not in new_email[1]:
        return False
    return True

def valid_password(new_password):
    if (len(new_password) >= 8
        and search("[a-z]", new_password)
        and search("[A-Z]", new_password)
        and search("[0-9]", new_password)
        and search("[`!\"£$%^&*()_+{}\[\]~:;@'|<,>.?/]", new_password)):
        return True
    return False

def sign_up(values):
    username, email, password, password_again = values
    if username == "admin": # added for testing
        return "Sign up successful."
    if not valid_new_username(username):
         return "Username invalid."
    if not valid_email(email):
        return "Email address invalid."
    if not valid_password(password):
        return "Password invalid."
    if password != password_again:
        return "Passwords do not match."
    new_salt = generate_salt()
    hashed_password = generate_hashed_password(password, new_salt)
    db_calls.add_user(username, email, hashed_password, new_salt)
    return "Sign up successful."

def generate_salt():
    len_salt = 8
    new_salt = token_hex(len_salt)
    return new_salt
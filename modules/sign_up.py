import re # regex module to assist with validity checks
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
        and re.search("[a-z]", new_password)
        and re.search("[A-Z]", new_password)
        and re.search("[0-9]", new_password)
        and re.search("[`!\"£$%^&*()_+{}\[\]~:;@'|<,>.?/]", new_password)):
        return True
    return False

def sign_up(values):
    username, email, password, password_again = values
    if username == "admin": # added for testing
        return "Sign up successful."
    while not valid_new_username(username):
         return "Username invalid."
    while not valid_email(email):
        return "Email address invalid."
    while not valid_password(password):
        return "Password invalid."
    while password != password_again:
        return "Passwords do not match."
    return "Sign up successful."
import re # regex module to assist with validity checks
from secrets import token_hex # module to generate cryptographically secure numbers
from hashlib import sha256

def valid_new_username(new_username):
    """
    function to check if a username is valid based on the following conditions:
    - must be alphanumeric
    - must not already exist in the database
    """
    return new_username.isalnum()

def valid_email(new_email):
    """
    function to check if an email is valid based on the following conditions:
    - must contain a '@' which is not at the beginning or end
    - must contain a '.' at some point after the '@'
    """
    new_email = new_email.split("@")
    if len(new_email) != 2:
        return False
    if "." not in new_email[1]:
        return False
    return True

def valid_password(new_password):
    """
    function to check if a password is valid based on the following conditions:
    - must be at least 8 characters
    - must contain an uppercase & lowercase character, a number, and a symbol
    """
    if (len(new_password) >= 8
        and re.search("[a-z]", new_password)
        and re.search("[A-Z]", new_password)
        and re.search("[0-9]", new_password)
        and re.search("[`!\"£$%^&*()_+{}\[\]~:;@'|<,>.?/]", new_password)):
        return True
    return False

def generate_salt():
    len_salt = 8
    new_salt = token_hex(len_salt)
    return new_salt

def generate_hashed_password(password, salt):
    return str(sha256((password + salt).encode()).hexdigest())

def sign_up(values):
    """
    takes in the values and the existing accounts and returns the result of a sign up attempt
    """
    username, email, password, password_again = values
    values_dict = None
    if not valid_new_username(username):
        message = "Username invalid."
    elif not valid_email(email):
        message = "Email address invalid."
    elif not valid_password(password):
        message = "Password invalid."
    elif password != password_again: # added logic
        message = "Passwords do not match."
    else:
        message = "Sign up successful."
        new_salt = generate_salt()
        hashed_password = generate_hashed_password(password, new_salt)
        values_dict = {
            "username": username,
            "email": email,
            "salt": new_salt,
            "hashed_password": hashed_password
        }
    return values_dict, message
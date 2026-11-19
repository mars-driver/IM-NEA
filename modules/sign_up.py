import re # regex module to assist with validity checks

def valid_new_username(new_username, accounts):
    """
    function to check if a username is valid based on the following conditions:
    - must be alphanumeric
    - must not already exist in the database
    """
    return new_username.isalnum() and new_username not in accounts

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

def sign_up(values, accounts):
    """
    takes in the values and the existing accounts and returns the result of a sign up attempt
    """
    username, email, password, password_again = values
    if not valid_new_username(username, accounts):
         return "Username invalid."
    if not valid_email(email):
        return "Email address invalid."
    if not valid_password(password):
        return "Password invalid."
    if password != password_again: # added logic
        return "Passwords do not match."
    return "Sign up successful."
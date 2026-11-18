import re # regex module to assist with validity checks

def valid_new_username(new_username, accounts):
    return new_username.isalnum() and new_username not in accounts

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

def sign_up(values, accounts):
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
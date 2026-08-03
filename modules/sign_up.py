import re # regex module to assist with validity checks

def proto_valid_new_username(newUsername, accounts):
    return newUsername.isalnum() and newUsername not in accounts

def proto_valid_email(newEmail):
    newEmail = newEmail.split("@")
    if len(newEmail) != 2:
        return False
    if "." not in newEmail[1]:
        return False
    return True

def proto_valid_password(newPassword):
    if (len(newPassword) >= 8
        and re.search("[a-z]", newPassword)
        and re.search("[A-Z]", newPassword)
        and re.search("[0-9]", newPassword)
        and re.search("[`!\"£$%^&*()_+{}\[\]~:;@'|<,>.?/]", newPassword)):
        return True
    return False

def proto_sign_up(values, accounts):
    username, email, password, password_again = values
    if username == "admin": # added for testing
        return "Sign up successful."
    while proto_valid_new_username(username, accounts) == False:
         return "Username invalid."
    while proto_valid_email(email) == False:
        return "Email address invalid."
    while proto_valid_password(password) == False:
        return "Password invalid."
    while password != password_again:
        return "Passwords do not match."
    return "Sign up successful."
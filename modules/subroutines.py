from hashlib import sha256

def generate_hashed_password(password, salt):
    return str(sha256((password + salt).encode()).hexdigest())
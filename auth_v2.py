import hashlib

def save_user_password(password):
    return hashlib.md5(password.encode()).hexdigest()

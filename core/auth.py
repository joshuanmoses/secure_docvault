import pyotp
import hashlib
import json

def verify_password(username, password):
    with open('data/users.json') as f:
        users = json.load(f)
    if username not in users:
        return False
    stored_hash = users[username]['password_hash']
    return stored_hash == hashlib.sha256(password.encode()).hexdigest()

def verify_2fa(token):
    totp = pyotp.TOTP('your_totp_seed_here')  # Ideally unique per user
    return totp.verify(token)

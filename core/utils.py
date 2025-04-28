import hashlib
import os
import secrets

def hash_password(password: str) -> str:
    """
    Generate a SHA-256 hash of a password.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def generate_aes_key() -> bytes:
    """
    Generate a random 32-byte AES key for AES-256 encryption.
    """
    return os.urandom(32)

def generate_totp_seed() -> str:
    """
    Generate a random TOTP (Time-based One-Time Password) seed for 2FA.
    """
    return secrets.token_hex(10)  # 20 hex characters (~10 bytes)

def random_token(length=16) -> str:
    """
    Generate a secure random token, useful for session management or password resets.
    """
    return secrets.token_hex(length)

def sanitize_filename(filename: str) -> str:
    """
    Sanitize a filename to avoid path traversal or injection attacks.
    """
    return "".join(c for c in filename if c.isalnum() or c in (' ', '.', '_')).rstrip()

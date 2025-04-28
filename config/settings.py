SECRET_KEY = "your_flask_secret_key_here"
ENCRYPTION_KEY = b'your_32_byte_aes_key_here___'  # Must be 32 bytes for AES-256
TWO_FACTOR_SECRET = "your_totp_seed_here"

ROLES = {
    "admin": ["read", "write", "delete"],
    "editor": ["read", "write"],
    "viewer": ["read"]
}

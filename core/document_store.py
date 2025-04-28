import os
from core.encryptor import encrypt_data, decrypt_data

def save_document(folder, filename, content):
    os.makedirs(f"data/vault/{folder}", exist_ok=True)
    encrypted = encrypt_data(content.encode())
    with open(f"data/vault/{folder}/{filename}.enc", 'wb') as f:
        f.write(encrypted)

def load_document(folder, filename):
    with open(f"data/vault/{folder}/{filename}.enc", 'rb') as f:
        encrypted = f.read()
    return decrypt_data(encrypted).decode()

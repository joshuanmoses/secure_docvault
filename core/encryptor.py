from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from config.settings import ENCRYPTION_KEY
import os

def encrypt_data(data):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(ENCRYPTION_KEY), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    return iv + encryptor.update(padded_data) + encryptor.finalize()

def decrypt_data(enc_data):
    iv = enc_data[:16]
    cipher = Cipher(algorithms.AES(ENCRYPTION_KEY), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(enc_data[16:]) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(padded_data) + unpadder.finalize()

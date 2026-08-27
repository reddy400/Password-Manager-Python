import base64
import hashlib

from cryptography.fernet import Fernet


def derive_key(master_password):
    key = hashlib.sha256(
        master_password.encode()
    ).digest()

    return base64.urlsafe_b64encode(key)


def encrypt_password(password, master_password):
    key = derive_key(master_password)

    cipher = Fernet(key)

    encrypted = cipher.encrypt(
        password.encode()
    )

    return encrypted.decode()


def decrypt_password(encrypted_password, master_password):
    key = derive_key(master_password)

    cipher = Fernet(key)

    decrypted = cipher.decrypt(
        encrypted_password.encode()
    )

    return decrypted.decode()
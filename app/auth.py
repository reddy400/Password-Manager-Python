from argon2 import PasswordHasher

ph = PasswordHasher()


def hash_master_password(password):
    return ph.hash(password)


def verify_master_password(stored_hash, password):
    try:
        ph.verify(stored_hash, password)
        return True
    except Exception:
        return False
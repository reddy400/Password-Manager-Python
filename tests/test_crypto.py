from app.crypto import encrypt_password, decrypt_password


def test_encryption():

    original = "MySecretPassword123!"

    encrypted = encrypt_password(
        original,
        "MasterPassword"
    )

    assert encrypted != original

    decrypted = decrypt_password(
        encrypted,
        "MasterPassword"
    )

    assert decrypted == original
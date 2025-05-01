from cryptography.fernet import Fernet
import os

KEY_PATH = "data/secret.key"

def generate_key():
    """Generate and save a new Fernet key if it doesn't exists."""
    if not os.path.exists ("data"):
        os.makedirs("data")
    if not os.path.exists(KEY_PATH):
        key = Fernet.generate_key()
        with open (KEY_PATH, "wb") as key_file:
            key_file.write(key)

def load_key():
    """Load the Fernet key from file"""
    if not os.path.exists(KEY_PATH):
        raise FileNotFoundError("Encryption key not found. Generate it first.")
    with open(KEY_PATH, "rb")as key_file:
        return key_file.read()
    
def encrypt_password(password: str ) -> str:
    """Encrypt a password and return it as a string."""
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())
    return encrypted.decode()

def decrypt_password(encrypted_password: str) -> str:
    """Decrypt an encrypted password string."""
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password.encode())
    return decrypted.decode()
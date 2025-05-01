#Authentication

import hashlib
from database.db_handler import get_connection

def hash_password (password: str) -> str:
    #Hash the master password using SHA-256.
    return hashlib.sha256(password.encode()).hexdigest()

def is_master_password_set() -> bool:
    #Check if the master password has already been set in the database.
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("Select COUNT(*) FROM master_password")
    result = cursor.fetchone()
    conn.close()
    return result[0]>0

def set_master_password(password: str):
    #Store the hashed master password in the database.
    hashed = hash_password(password)
    conn=get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO master_password(password_hash) VALUES (?)", (hashed,))
    conn.commit()
    conn.close()

def verify_master_pasword(password: str) -> bool:
    #Verify input password against the stored hashed password.
    hashed = hash_password(password)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM master_password LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    return hashed == result[0] if result else False

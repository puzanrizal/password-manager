from database.db_handler import get_connection
from core.encryption import encrypt_password, decrypt_password

def add_password(service: str, username: str, plain_password: str):
    """Encrypt and store a password."""
    conn = get_connection()
    cursor = conn.cursor()
    encrypted = encrypt_password(plain_password)
    
    cursor.execute("""
        INSERT INTO passwords(service, username, password)
        VALUES(?,?,?)
    """, (service, username, encrypted))
    conn.commit()
    conn.close()
    
def get_password(service: str):
    """Retrieve and decrypt the passowrd for the given service."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT username, password FROM passwords WHERE service = ?
    """,(service,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        username, encrypted_password = result
        return username, decrypt_password(encrypted_password)
    else:
        return None
    
def delete_password(service: str):
    """Delete a saved password from the service."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM passwords WHERE service = ?", (service,))
    conn.commit()
    conn.close()
    
def list_services():
    """List all the stored services."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT service FROM passwords")
    results = cursor.fetchall()
    conn.close()
    return[row[0] for row in results]
#Database Handler

import sqlite3
import os

DB_PATH = "data/password.db"

def get_connection():
    '''Get connection to the SQLite database.'''
    if not os.path.exists("data"):
        os.makedirs("data")
    conn = sqlite3.connect(DB_PATH)
    return conn

def initialize_database():
    '''Initialize the database schema if not exists.'''
    conn = get_connection()
    cursor = conn.cursor()
    
    #Table to store the master password
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS master_password (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        password_hash TEXT NOT NULL)
        """)

    #Table to store encrypted password entries
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL)
            """)
    conn.commit()
    conn.close()
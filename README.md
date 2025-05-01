# Password Manager

A secure, lightweight password manager built with Python and Kivy, designed for desktop, laptop, and mobile use (Windows for now). It uses SQLite to store passwords securely with encryption and master password protection.

---

## Features

- Master password authentication 
- AES-encrypted password storage 
- Password generator for strong, random passwords 
- Securely add, retrieve, and list saved credentials 
- Modular and scalable project structure 
- Designed with cross-platform support in mind 

---

## Project Structure
PasswordManager/
│
├── 📁 core/                  # Core logic: encryption, password handling
│   ├── __init__.py
│   ├── encryption.py         # Handles encrypt/decrypt
│   ├── password_manager.py   # Password CRUD operations (add, retrieve, delete)
│   ├── auth.py               # Master password setup, login, hashing
│
├── 📁 ui/                    # Kivy App UI components
│   ├── __init__.py
│   ├── main_screen.kv        # Kivy Language (KV) file for main UI
│   ├── login_screen.kv       # Login screen UI
│   ├── add_password_screen.kv # Add password screen UI
│   ├── screens.py            # Python screen manager
│
├── 📁 database/              # Data storage layer
│   ├── __init__.py
│   ├── db_handler.py         # Handles encrypted database or JSON file
│
├── 📁 assets/                # Icons, logos, images
│   ├── logo.png
│   ├── app_icon.ico
│
├── 📁 utils/                 # Utilities, helpers
│   ├── __init__.py
│   ├── password_generator.py # Random password generator
│
├── main.py                   # App entry point
├── requirements.txt          # Python dependencies
├── README.md                 # Project overview and instructions
└── LICENSE                   # (Optional) Open source license


---

## Installation

### 1. Clone the repository

git clone https://github.com/your-username/password-manager.git <br>
cd password-manager

### 2. Create and activate a virtual environment
python -m venv venv <br>
venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run the application
python main.py

---

## Author 
**Pujan Rijal** <br>
Github: [@puzanrizal](https://github.com/puzanrizal)
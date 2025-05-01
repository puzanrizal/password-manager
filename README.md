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
password-manager/ │ ├── core/ # Core logic for encryption and password management │ ├── init.py │ ├── encryption.py # Handles encryption/decryption │ ├── password_manager.py # Add/retrieve/list passwords │ └── auth.py # Master password setup and verification │ ├── database/ # SQLite database handler │ ├── init.py │ └── db_handler.py │ ├── ui/ # Kivy UI components │ ├── init.py │ ├── main_screen.kv │ ├── login_screen.kv │ ├── add_password_screen.kv │ └── screens.py │ ├── utils/ # Utility modules │ ├── init.py │ └── password_generator.py # Random password suggestion logic │ ├── assets/ # Images, icons, etc. │ ├── logo.png │ └── app_icon.ico │ ├── main.py # Application entry point ├── requirements.txt # Project dependencies ├── README.md # Project overview and setup guide └── .gitignore # Ignored files and folders


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
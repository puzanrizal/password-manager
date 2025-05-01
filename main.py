from core.auth import is_master_password_set, set_master_password, verify_master_pasword
from core.encryption import generate_key
from database.db_handler import initialize_database
from core.password_manager import add_password, get_password, list_services

def main():
    generate_key()
    initialize_database()
    
    if not is_master_password_set():
        pwd = input("Set a master password: ")
        confirm = input("Confirm master password: ")
        if pwd == confirm:
            set_master_password(pwd)
            print("Master password set successfully!")
        else:
            print("Password doesn't match.")
    else:
        pwd = input("Enter master password: ")
        if verify_master_pasword(pwd):
            print("Access Granted!")
        else:
            print("Incorrect password.")

    while True:
        print("\nOptions:\n1. Add\n2. Retrieve\n3. List\n4. Exit")
        choice = input("Choose: ").strip()
        
        if choice =="1":
            service = input("Service: ")
            username = input("Username: ")
            password = input("Password: ")
            add_password(service, username, password)
            print("Password saved.")
        elif choice =="2":
            service = input("Service to retrieve: ")
            result = get_password(service)
            if result:
                print(f"Username: {result[0]}, Password: {result[1]}")
            else:
                print("Not found")
        elif choice == "3":
            services = list_services()
            print("Saved services:",",".join(services) if services else "None")
        elif choice == "4":
            break
        else:
            print("Invalid Choice.")
            
if __name__ == "__main__":
    main()
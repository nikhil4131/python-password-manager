import getpass
import json

from cryptography.fernet import Fernet

with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

def show_menu():
    print("\n===== PASSWORD MANAGER =====")
    print("1. Add a password")
    print("2. View saved accounts")
    print("3. Search for an account")
    print("4. Delete an account")
    print("5. Update an account")
    print("6. Reveal a password")
    print("7. Exit")

def add_account():
    website = input("Enter website name: ").strip()
    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password: ").strip()

    if not website or not username or not password:
        print("Error: All fields are required.")
        return

    for existing_account in accounts:
        if existing_account["website"].strip().lower() == website.lower():
            print("Error: This website already exists.")
            return

    encrypted_password = cipher.encrypt(password.encode()).decode()

    account = {
        "website": website,
        "username": username,
        "password": encrypted_password
    }

    accounts.append(account)
    save_account()
    print("Account added successfully!")

def view_account():
    if not accounts:
        print("No accounts saved yet.")
        return
    for account in accounts:
        print("\nWebsite:", account["website"])
        print("Username:", account["username"])

def search_account():
    website = input("Enter website to search: ").strip().lower()

    found = False

    for account in accounts:
        if account["website"].lower() == website:
            print("Website:", account["website"])
            print("Username:", account["username"])
            found = True
            break

    if not found:
        print("Account not found.")

def save_account():
    with open("password.json", "w") as file:
        json.dump(accounts, file, indent=4)

def load_account():
    try:
        with open("password.json", "r") as file:
            data = json.load(file)

            if isinstance(data,list):
                return data
            print("Warning: Invalid account data format.")
            return[]

    except FileNotFoundError:
        return[]

    except json.JSONDecodeError:
        print("Warning: password.json contains invalid JSON.")
        return []

def decrypt_password(encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()

def reveal_password():
    website = input("enter website: ").strip().lower()

    for account in accounts:
        if account["website"].strip().lower() == website:
            try:
                password = decrypt_password(account["password"])
                print("Username:", account["username"])
                print("Password:", password)

            except Exception:
                print("Unable to decrypt this password.")
            return

    print("Account not found.")

def delete_account():
    website = input("Enter website to delete: ").strip().lower()

    for account in accounts:
        if account["website"].lower() == website:
            accounts.remove(account)
            save_account()
            print("Account deleted successfully!")
            return

    print("Account not found.")

def update_account():
    website = input("Enter website to update: ").strip().lower()

    for account in accounts:
        if account["website"].strip().lower() == website:
            new_username = input(
                "Enter new username (press Enter to keep current): "
            ).strip()

            new_password = getpass.getpass(
                "Enter new password (press Enter to keep current): "
            ).strip()

            if new_username:
                account["username"] = new_username

            if new_password:
                account["password"] = cipher.encrypt(
                    new_password.encode()
                ).decode()

            save_account()
            print("Account updated successfully!")
            return

    print("Account not found.")

accounts = load_account()

while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_account()

    elif choice == "2":
        view_account()

    elif choice == "3":
        search_account()

    elif choice == "4":
        delete_account()

    elif choice == "5":
        update_account()

    elif choice == "6":
        reveal_password()

    elif choice == "7":
        print("goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")

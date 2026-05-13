import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts[name] = phone
    save_contacts(contacts)
    print("Contact saved!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Deleted!")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\n1. View\n2. Add\n3. Delete\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

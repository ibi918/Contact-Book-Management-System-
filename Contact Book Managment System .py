import json
import os

FILE_NAME = "contacts.json"


# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# Add new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully!")


# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for contact in contacts:
        print("--------------------")
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])


# Search contact
def search_contact(contacts):
    name = input("Enter name to search: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            print("Contact found!")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            return

    print("Contact not found.")


# Update contact
def update_contact(contacts):
    name = input("Enter name to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contact["phone"] = input("Enter new phone: ")
            contact["email"] = input("Enter new email: ")

            save_contacts(contacts)
            print("Contact updated successfully!")
            return

    print("Contact not found.")


# Delete contact
def delete_contact(contacts):
    name = input("Enter name to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")


# Main program
def main():
    contacts = load_contacts()

    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            update_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            print("Thank you for using Contact Book!")
            break

        else:
            print("Invalid choice. Try again.")


main()
# ================================
# Contact Book
# By: Fitsum
# ================================

import json   # To save contacts to a file
import os     # To check if file exists

# File where contacts are saved
FILE = "contacts.json"

# Load contacts from file if it exists
def load_contacts():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            return json.load(f)
    return {}  # Return empty dict if no file yet

# Save contacts to file
def save_contacts(contacts):
    with open(FILE, 'w') as f:
        json.dump(contacts, f, indent=4)
    print(" Contacts saved.")

# Add a new contact
def add_contact(contacts):
    print("\n--- ADD CONTACT ---")
    name = input("Name: ").strip()

    if name in contacts:
        print("⚠  Contact already exists!")
        return

    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    # Save as a dictionary inside contacts
    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)
    print(f" {name} added!")

# View all contacts
def view_contacts(contacts):
    print("\n--- ALL CONTACTS ---")

    if not contacts:
        print("No contacts yet.")
        return

    # Loop through and print each contact
    for i, (name, info) in enumerate(contacts.items(), 1):
        print(f"\n{i}. {name}")
        print(f"    {info['phone']}")
        print(f"    {info['email']}")

# Search for a contact
def search_contact(contacts):
    print("\n--- SEARCH ---")
    query = input("Enter name to search: ").strip().lower()

    # Check each contact name
    found = False
    for name, info in contacts.items():
        if query in name.lower():
            print(f"\n Found: {name}")
            print(f"   {info['phone']}")
            print(f"   {info['email']}")
            found = True

    if not found:
        print("No contact found.")

# Delete a contact
def delete_contact(contacts):
    print("\n--- DELETE CONTACT ---")
    name = input("Enter name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"  {name} deleted.")
    else:
        print(" Contact not found.")

# Main menu
def main():
    print("=" * 35)
    print("        CONTACT BOOK ")
    print("=" * 35)

    # Load saved contacts at startup
    contacts = load_contacts()

    while True:
        print("\nMenu:")
        print("  1. Add Contact")
        print("  2. View All Contacts")
        print("  3. Search Contact")
        print("  4. Delete Contact")
        print("  5. Exit")

        choice = input("\nChoose (1-5): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("\nGoodbye! ")
            break
        else:
            print("Invalid choice. Try again.")

# Start the app
main()
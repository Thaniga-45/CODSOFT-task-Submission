contacts = {}

def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address (optional): ").strip()

    contacts[name] = {
        "Phone": phone,
        "Email": email if email else "N/A"
    }
    print(f"Contact '{name}' added successfully!\n")

def view_contacts():
    if not contacts:
        print("Contact book is empty.\n")
        return

    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['Phone']}")
        print(f"Email: {info['Email']}")
        print("---------------------")
    print()

def search_contact():
    name = input("Enter the name to search: ").strip()
    if name in contacts:
        print(f"\nContact found for '{name}':")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}\n")
    else:
        print(f"No contact found for '{name}'.\n")

def delete_contact():
    name = input("Enter the name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.\n")
    else:
        print(f"No contact found with name '{name}'.\n")

def main():
    while True:
        print("------ Contact Book ------")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

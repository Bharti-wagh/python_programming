contacts = {}

def show_menu():
    print("\n=== Contact Book Menu ===")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        if not contacts:
            print("No contacts found!")
        else:
            print("\nYour Contacts:")
            for name, number in contacts.items():
                print(f"{name}: {number}")

    elif choice == "2":
        name = input("Enter name: ").strip()
        number = input("Enter phone number: ").strip()
        contacts[name] = number
        print("Contact added successfully!")

    elif choice == "3":
        name = input("Enter name to search: ").strip()
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found!")

    elif choice == "4":
        name = input("Enter name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1-5.")

def display_menu():
    """Prints the main menu options to the console."""
    print("\n" + "="*30)
    print("      CONTACT BOOK MENU")
    print("="*30)
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    print("="*30)


def add_contact(contacts):
    """Prompts for name and phone, adding it if the name is unique."""
    name = input("Enter contact name: ").strip()
    
    # Validation: Ensure name isn't empty
    if not name:
        print("❌ Error: Name cannot be empty.")
        return

    # Check for duplicates (case-insensitive check is best practice)
    # Using a case-insensitive check ensures "John" and "john" are treated as duplicates
    name_lower = name.lower()
    if any(existing_name.lower() == name_lower for existing_name in contacts):
        print(f"❌ Error: A contact named '{name}' already exists.")
        return

    phone = input("Enter phone number: ").strip()
    if not phone:
        print("❌ Error: Phone number cannot be empty.")
        return

    contacts[name] = phone
    print(f"✅ Contact '{name}' added successfully!")


def view_all_contacts(contacts):
    """Displays all contacts in a formatted list."""
    if not contacts:
        print("📭 Your contact list is empty.")
        return

    print("\n--- Current Contacts ---")
    # Loop through and cleanly format the output
    for name, phone in contacts.items():
        print(f"👤 Name: {name} | 📞 Phone: {phone}")


def search_contact(contacts):
    """Searches for contacts allowing partial, case-insensitive matches."""
    query = input("Enter name (or partial name) to search: ").strip().lower()
    
    if not query:
        print("❌ Error: Search query cannot be empty.")
        return

    # Find all contacts where the query is a substring of the key
    results = {name: phone for name, phone in contacts.items() if query in name.lower()}

    if not results:
        print(f"🔍 No contacts found matching '{query}'.")
    else:
        print(f"\n🔍 Found {len(results)} match(es):")
        for name, phone in results.items():
            print(f"👤 Name: {name} | 📞 Phone: {phone}")


def delete_contact(contacts):
    """Removes a contact by name if it exists."""
    name_to_delete = input("Enter the name of the contact to delete: ").strip()
    
    # Look for an exact match (or case-insensitive exact match)
    # We find the actual case-sensitive key first to properly delete it from the dict
    target_key = None
    for name in contacts:
        if name.lower() == name_to_delete.lower():
            target_key = name
            break

    if target_key:
        del contacts[target_key]
        print(f"🗑️ Contact '{target_key}' has been deleted.")
    else:
        print(f"❌ Error: Contact '{name_to_delete}' not found.")


def main():
    # Dictionary to store data -> Key: Name (Str), Value: Phone (Str)
    contacts = {}
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_all_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == choice == "5":
            print("\n👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
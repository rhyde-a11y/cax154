import os

# Filename for saving data
DATA_FILE = "contacts.txt"

def load_contacts():
    """Loads contacts from a file on startup. Returns a dictionary."""
    contacts = {}
    if not os.path.exists(DATA_FILE):
        return contacts  # Return empty dict if file doesn't exist yet
    
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line or "::" not in line:
                    continue
                # Split name and the comma-separated phone numbers
                name, numbers_str = line.split("::", 1)
                # Convert numbers back into a list
                numbers_list = [num.strip() for num in numbers_str.split(",")]
                contacts[name] = numbers_list
    except (IOError, ValueError) as e:
        print(f"⚠️ Warning: Could not load contacts completely ({e}). Starting fresh.")
    return contacts


def save_contacts(contacts):
    """Saves the current contacts dictionary to a file."""
    try:
        with open(DATA_FILE, "w") as file:
            for name, numbers in contacts.items():
                # Join multiple numbers with commas, separate from name with '::'
                numbers_str = ",".join(numbers)
                file.write(f"{name}::{numbers_str}\n")
    except IOError:
        print("❌ Error: Could not save contacts to file.")


def is_valid_phone(phone):
    """Validates that a phone number contains only digits, dashes, or spaces, and is long enough."""
    # Strip common formatting characters to check if it's mostly numeric
    clean_phone = phone.replace("-", "").replace(" ", "")
    return clean_phone.isdigit() and len(clean_phone) >= 7


def add_contact(contacts):
    """Prompts for name and one or more numbers, updating the dictionary."""
    name = input("Enter contact name: ").strip()
    if not name:
        print("❌ Error: Name cannot be empty.")
        return

    # Case-insensitive duplicate check
    name_lower = name.lower()
    if any(existing_name.lower() == name_lower for existing_name in contacts):
        print(f"❌ Error: A contact named '{name}' already exists.")
        return

    numbers = []
    # Loop to allow entering multiple phone numbers
    while True:
        phone = input("Enter phone number: ").strip()
        if not is_valid_phone(phone):
            print("❌ Error: Invalid phone number. It must contain only digits/dashes and be at least 7 digits.")
            continue
        
        numbers.append(phone)
        
        # Ask if they want to add another number for this specific contact
        more = input("Add another number for this contact? (y/n): ").strip().lower()
        if more != 'y':
            break

    contacts[name] = numbers
    save_contacts(contacts)  # Save instantly
    print(f"✅ Contact '{name}' added successfully!")


def view_all_contacts(contacts):
    """Displays all contacts, automatically sorted alphabetically by name."""
    if not contacts:
        print("📭 Your contact list is empty.")
        return

    print("\n--- Current Contacts (Alphabetical) ---")
    # Sorting keys alphabetically
    for name in sorted(contacts.keys()):
        # Join the list of numbers into a readable, comma-separated string
        numbers_str = ", ".join(contacts[name])
        print(f"👤 Name: {name} | 📞 Phone(s): {numbers_str}")


def search_contact(contacts):
    """Searches for contacts using partial, case-insensitive matching."""
    query = input("Enter name (or part of a name) to search: ").strip().lower()
    if not query:
        print("❌ Error: Search query cannot be empty.")
        return

    results = {name: nums for name, nums in contacts.items() if query in name.lower()}

    if not results:
        print(f"🔍 No contacts found matching '{query}'.")
    else:
        print(f"\n🔍 Found {len(results)} match(es):")
        for name in sorted(results.keys()):
            numbers_str = ", ".join(results[name])
            print(f"👤 Name: {name} | 📞 Phone(s): {numbers_str}")


def delete_contact(contacts):
    """Deletes a contact by name (case-insensitive exact match)."""
    name_to_delete = input("Enter the name of the contact to delete: ").strip()
    
    target_key = None
    for name in contacts:
        if name.lower() == name_to_delete.lower():
            target_key = name
            break

    if target_key:
        del contacts[target_key]
        save_contacts(contacts)  # Update file data
        print(f"🗑️ Contact '{target_key}' has been deleted.")
    else:
        print(f"❌ Error: Contact '{name_to_delete}' not found.")


def main():
    # Load any existing data right when the program spins up
    contacts = load_contacts()
    
    while True:
        print("\n" + "="*30)
        print("      CONTACT BOOK MENU")
        print("="*30)
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        print("="*30)
        
        try:
            choice_input = input("Enter your choice (1-5): ").strip()
            # Convert to integer to utilize try/except block validation
            choice = int(choice_input)
            
            if choice == 1:
                add_contact(contacts)
            elif choice == 2:
                view_all_contacts(contacts)
            elif choice == 3:
                search_contact(contacts)
            elif choice == 4:
                delete_contact(contacts)
            elif choice == 5:
                print("\n👋 Exiting Contact Book. Your data is safely saved. Goodbye!")
                break
            else:
                print("❌ Invalid menu range. Please enter a number between 1 and 5.")
                
        except ValueError:
            print("❌ Invalid input type. Please enter a valid integer (1-5).")
        except Exception as e:
            # Catch-all block for any unhandled catastrophic execution errors
            print(f"🚨 An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contact_list(self):
        if self.contacts:
            print("\nContact List:")
            for i, contact in enumerate(self.contacts):
                print(f"{i+1}. {contact.name} - {contact.phone_number}")
        else:
            print("No contacts found.")

    def search_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                print(f"\nName: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print(f"Address: {contact.address}")
                found = True
        if not found:
            print("No matching contacts found.")

    def update_contact(self, index, new_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = new_contact
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            print("Contact deleted successfully.")
        else:
            print("Invalid contact index.")

def main():
    contact_list = ContactList()
    
    while True:
        print("\nContact Management Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_list.add_contact(new_contact)
        elif choice == '2':
            contact_list.view_contact_list()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_list.search_contact(search_term)
        elif choice == '4':
            index = int(input("Enter index of contact to update: ")) - 1
            if 0 <= index < len(contact_list.contacts):
                name = input("Enter name: ")
                phone_number = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                updated_contact = Contact(name, phone_number, email, address)
                contact_list.update_contact(index, updated_contact)
            else:
                print("Invalid contact index.")
        elif choice == '5':
            index = int(input("Enter index of contact to delete: ")) - 1
            contact_list.delete_contact(index)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

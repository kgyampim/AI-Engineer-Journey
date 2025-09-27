#Data storage
contacts = [] 

#functions
def add_contact():
    name = input('Contact name: ')
    phone = input('Phone number: ')
    email = input('Enter contact email: ') 

    contact = {'name': name, 'phone': phone, 'email': email}
    contacts.append(contact)
    print(f'\n Contact {name} added sucessfully!')

def view_contact():
    if not contacts:
        print('\n No contacts here')
        return 
    print('\n Contact list:')
    for i, contact in enumerate(contacts, start= 1):
        print(f'{i}. {contact['name']}| {contact['phone']} | {contact['email']}')

def search_contact():
    if not contacts:
        print("\n No contacts to search.")
        return 
    name = input('Enter name to search: ')
    found = False 

    for contact in contacts:
        if contact['name'] == name:
            print(f'\n Found: {contact['name']} | {contact['phone']} | {contact['email']}')
            found = True
            break 
    if not found:
        print(f'\n No contacts found with name {name}.')

def update_contact():
    if not contacts:
        print('\n No contacts to update.')
        return
    name = input('Enter contact name to update: ')
    for contact in contacts:
        if contact['name'] == name:
            new_phone = input('Enter new phone number (leave blank to keep current): ')
            new_email = input('Enter new email (leave blank to keep current): ')
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            print(f'\n Contact {name} updated successfully!')
            return

def delete_contact():
    if not contacts:
        print('\n No contacts to delete.')
        return 
    name = input('Enter contact name to delete: ')
    for i, contact in enumerate(contacts):
        if contact['name'] == name:
            del contacts[i]
            print(f'\n Contact {name} deleted successfully!')
            return 
    print(f'\n No contacts found with name {name}.')

def menu():
    print('\n Contact List')
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

while True:
    menu()
    choice = input('What do you want to do: ')

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting... Goodbye!")
        break
    else:
        print('Try Again')


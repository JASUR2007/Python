import os


class ContactsBook:
    def __init__(self):
        self.contacts = []
        self.language = "ru"

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def display_menu(self):
        menu = {
            "en": [
                "1. Add a new contact",
                "2. Update a contact",
                "3. Delete a contact",
                "4. Search for a contact",
                "5. Show all contacts",
                "6. Exit"
            ],
            "ru": [
                "1. Добавить новый контакт",
                "2. Обновить контакт",
                "3. Удалить контакт",
                "4. Найти контакт",
                "5. Показать все контакты",
                "6. Выход"
            ]
        }

        print("-" * 20)
        for item in menu[self.language]:
            print(item)
        print("-" * 20)

    def select_language(self):
        self.clear_screen()
        print("Select Language / Выберите язык:")
        print("1. English")
        print("2. Русский")
        choice = input("Enter choice/ Выберите: ")
        if choice == "2":
            self.language = "ru"
        else:
            self.language = "en"

    def add_contact(self):
        prompts = {
            "en": [
                "Add a New Contact:",
                "Enter Name: ",
                "Enter Phone Number! Phone number must start with '+', followed by digits: ",
                "Please enter a valid phone number!",
                "Enter Email Address! Email address must contain '@': ",
                "Invalid email. Please enter a valid email address.",
                "Enter Address: ",
                "Contact '{name}' added successfully!",
                "Press '0' to go back or Enter to add another contact: "
            ],
            "ru": [
                "Добавить новый контакт:",
                "Введите имя: ",
                "Введите номер телефона! Номер телефона должен начинаться с '+', за которым следуют цифры: ",
                "Пожалуйста, введите правильный номер телефона!",
                "Введите адрес электронной почты! Адрес должен содержать '@': ",
                "Неверный email. Пожалуйста, введите правильный адрес электронной почты.",
                "Введите адрес: ",
                "Контакт '{name}' успешно добавлен!",
                "Нажмите '0', чтобы вернуться, или Enter, чтобы добавить еще один контакт: "
            ]
        }

        messages = prompts[self.language]

        self.clear_screen()
        while True:
            print(messages[0])
            name = input(messages[1])
            phone = input(messages[2])
            while not (phone.startswith("+") and phone[1:].isdigit()):
                print(messages[3])
                phone = input(messages[2])

            email = input(messages[4])
            while "@" not in email:
                print(messages[5])
                email = input(messages[4])

            address = input(messages[6])

            self.contacts.append({
                "Name": name,
                "Phone": phone,
                "Email": email,
                "Address": address
            })

            print(messages[7].format(name=name))
            if input(messages[8]) == "0":
                break

    def find_contact(self, search_term):
        for contact in self.contacts:
            if contact["Name"] == search_term or contact["Phone"] == search_term:
                return contact
        return None
    
    def display_contact(self, contact):
        if self.language == "en":
            print("Contact Details:")
            print(f"Name: {contact['Name']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            print(f"Address: {contact['Address']}")
        elif self.language == "ru":
            print("Детали контакта:")
            print(f"Имя: {contact['Name']}")
            print(f"Телефон: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            print(f"Адрес: {contact['Address']}")

    def update_contact(self):
        self.clear_screen()
        while True:
            search_term = input("Enter Name or Phone Number to update or '0' to go back: ")
            if search_term == "0":
                break

            contact = self.find_contact(search_term)

            if contact:
                print("\nFound Contact:")
                print(f"Name: {contact['Name']}")
                print(f"Phone: {contact['Phone']}")
                print(f"Email: {contact['Email']}")
                print(f"Address: {contact['Address']}\n")

                def update_field(fieldName, currentValue, validater=None):
                    print(f"Current {fieldName}: {currentValue}")
                    choice = input(f"Enter new {fieldName} or Press '1' to skip, '0' to cancel: ")
                    if choice == "0":
                        return None  
                    if choice == "1":
                        return currentValue 
                    if validater and not validater(choice):
                        print(f"Invalid {fieldName}. Please enter a valid value.")
                        return currentValue
                    return choice

                def validate_phone(phone):
                    return phone.startswith("+") and phone[1:].isdigit()

                def validate_email(email):
                    return "@" in email

                new_name = update_field("Name", contact["Name"], None)
                if new_name is None:
                    print("Update canceled.")
                    break
                contact["Name"] = new_name

                new_phone = update_field("Phone", contact["Phone"], validate_phone)
                if new_phone is None:
                    print("Update canceled.")
                    break
                contact["Phone"] = new_phone

                new_email = update_field("Email", contact["Email"], validate_email)
                if new_email is None:
                    print("Update canceled.")
                    break
                contact["Email"] = new_email

                new_address = update_field("Address", contact["Address"], None)
                if new_address is None:
                    print("Update canceled.")
                    break
                contact["Address"] = new_address

                print("Contact updated successfully!")
            else:
                print("Contact not found!")

    def delete_contact(self):
        self.clear_screen()
        while True:
            search_term = input("Enter Name or Phone Number to delete or '0' to go back: ")
            if search_term == "0":
                break

            contact = self.find_contact(search_term)

            if contact:
                self.contacts.remove(contact)
                print(f"Contact '{contact['Name']}' deleted successfully!")
            else:
                print("Contact not found!")

    def search_contact(self):
        self.clear_screen()
        prompts = {
            "en": "Enter Name or Phone Number to search or '0' to go back: ",
            "ru": "Введите имя или номер телефона для поиска или '0', чтобы вернуться: "
        }

        while True:
            search_term = input(prompts[self.language])
            if search_term == "0":
                break

            contact = self.find_contact(search_term)

            if contact:
                self.display_contact(contact)
            else:
                if self.language == "en":
                    print("Contact not found!")
                elif self.language == "ru":
                    print("Контакт не найден!")

    def show_all_contacts(self):
        self.clear_screen()
        if not self.contacts:
            if self.language == "en":
                print("No contacts available!")
            elif self.language == "ru":
                print("Контакты отсутствуют!")
        else:
            if self.language == "en":
                print("All Contacts:")
            elif self.language == "ru":
                print("Все контакты:")

            index = 1
            for contact in self.contacts:
                print(10 * '-',index, 10 * '-')
                print(f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}")
                index += 1
        input("Press Enter to go back..." if self.language == "en" else "Нажмите Enter, чтобы вернуться...")

    def run(self):
        self.select_language()
        self.clear_screen()
        while True:
            self.display_menu()
            choice = input("Select a menu option: " if self.language == "en" else "Выберите пункт меню: ")
            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.update_contact()
            elif choice == "3":
                self.delete_contact()
            elif choice == "4":
                self.search_contact()
            elif choice == "5":
                self.show_all_contacts()
            elif choice == "6":
                if self.language == "en":
                    print("Thank you for using the Contacts Book. Goodbye!")
                elif self.language == "ru":
                    print("Спасибо за использование книги контактов. До свидания!")
                break
            else:
                if self.language == "en":
                    print("Invalid option. Please try again.")
                elif self.language == "ru":
                    print("Неверный вариант. Попробуйте снова.")


contacts_book = ContactsBook()
contacts_book.run()

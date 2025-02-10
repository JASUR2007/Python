import os

class Contact:
    def __init__(self):
        self.contacts = [] 
        self.language = "ru"

    def set_language(self):
        lang_choice = input("Choose language / Выберите язык (ru/eng): ").strip().lower()
        while lang_choice not in ['ru', 'eng']:
            print("Invalid choice! Please choose 'ru' for Russian or 'eng' for English.")
            lang_choice = input("Choose language / Выберите язык (ru/eng): ").strip().lower()
        self.language = lang_choice

    def add_contact(self):
        name = input(self.get_message("Enter contact name / Введите имя контакта: "))
        phone_number = input(self.get_message("Enter phone number, start with '+', followed by digits / Введите номер телефона (должен начинаться с '+', за ним идут цифры): "))
        while not self.is_valid_phone_number(phone_number):
            print(self.get_message("Invalid number! It should start with '+' and contain only digits. / Неверный номер телефона! Он должен начинаться с '+' и содержать только цифры."))
            phone_number = input(self.get_message("Enter phone number / Введите номер телефона: "))

        email = input(self.get_message("Enter email (should contain '@') / Введите email (должен содержать '@'): "))
        while not self.is_valid_email(email):
            print(self.get_message("Invalid email! It should contain '@' / Неверный email! Он должен содержать '@'."))
            email = input(self.get_message("Enter email / Введите email: "))

        address = input(self.get_message("Enter address / Введите адрес: "))
        self.contacts.append({
            'name': name,
            'phone_number': phone_number,
            'email': email,
            'address': address
        })
        print(self.get_message(f"Contact {name} added. / Контакт {name} добавлен."))

    def update_contact(self):
        if not self.contacts:
            print(self.get_message("No contacts to update. / Нет контактов для обновления."))
            return

        search_term = input(self.get_message("Enter name or phone number to search or '0' to exit / Введите имя или номер телефона для поиска или '0' для выхода: "))
        if search_term == '0':
            return

        contact = None
        for c in self.contacts:
            if c['name'] == search_term or c['phone_number'] == search_term:
                contact = c
                break

        if contact:
            print(f"{self.get_message('Found contact: / Найден контакт: ')} {contact}")
            update_field = input(self.get_message("What do you want to update (name, phone_number, email, address)? / Что хотите обновить (name, phone_number, email, address)? "))
            if update_field in contact:
                new_value = input(self.get_message(f"Enter new value for {update_field} / Введите новое значение для {update_field}: "))
                if update_field == 'phone_number' and not self.is_valid_phone_number(new_value):
                    print(self.get_message("Invalid phone number! / Неверный номер телефона!"))
                elif update_field == 'email' and not self.is_valid_email(new_value):
                    print(self.get_message("Invalid email! / Неверный email!"))
                else:
                    contact[update_field] = new_value
                    print(self.get_message("Contact updated. / Контакт обновлен."))
            else:
                print(self.get_message("Invalid field! / Неверное поле!"))
        else:
            print(self.get_message("Contact not found. / Контакт не найден."))

    def delete_contact(self):
        if not self.contacts:
            print(self.get_message("No contacts to delete. / Нет контактов для удаления."))
            return

        search_term = input(self.get_message("Enter name or phone number to delete or '0' to exit / Введите имя или номер телефона для удаления или '0' для выхода: "))
        if search_term == '0':
            return

        contact_to_delete = None
        for i in self.contacts:
            if i['name'] == search_term or i['phone_number'] == search_term:
                contact_to_delete = i
                break

        if contact_to_delete:
            self.contacts.remove(contact_to_delete)
            print(self.get_message(f"Contact {contact_to_delete['name']} deleted. / Контакт {contact_to_delete['name']} удален."))
        else:
            print(self.get_message("Contact not found. / Контакт не найден."))

    def search_contact(self):
        if not self.contacts:
            print(self.get_message("No contacts to search. / Нет контактов для поиска."))
            return

        search_term = input(self.get_message("Enter name or phone number to search or '0' to exit / Введите имя или номер телефона для поиска или '0' для выхода: "))
        if search_term == '0':
            return

        contact_found = None
        for c in self.contacts:
            if c['name'] == search_term or c['phone_number'] == search_term:
                contact_found = c
                break

        if contact_found:
            print(f"{self.get_message('Found contact: / Найден контакт: ')} {contact_found}")
        else:
            print(self.get_message("Contact not found. / Контакт не найден."))

    def show_contacts(self):
        if not self.contacts:
            print(self.get_message("No contacts to display. / Нет контактов для отображения."))
        else:
            print("\n" + self.get_message("All contacts: / Все контакты:"))
            for item in self.contacts:
                print(f"Name: {item['name']}, Phone: {item['phone_number']}, Email: {item['email']}, Address: {item['address']}")

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear") 

    def is_valid_phone_number(self, phone_number):
        return phone_number.startswith('+') and phone_number[1:].isdigit() 

    def is_valid_email(self, email):
        return '@' in email 

    def get_message(self, message):
        if self.language == 'ru':
            return message
        elif self.language == 'eng':
            return message
    def run(self):
        print(self.get_message("\nContact Book: / Контактная книга:"))
        print(self.get_message("1. Add contact / Добавить контакт"))
        print(self.get_message("2. Update contact / Обновить контакт"))
        print(self.get_message("3. Delete contact / Удалить контакт"))
        print(self.get_message("4. Search contact / Найти контакт"))
        print(self.get_message("5. Show all contacts / Показать все контакты"))
        print(self.get_message("6. Exit / Выйти"))
    def menu(self):
        while True:
            self.run()
            choice = input(self.get_message("Choose option: / Выберите опцию: "))
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.update_contact()
            elif choice == '3':
                self.delete_contact()
            elif choice == '4':
                self.search_contact()
            elif choice == '5':
                self.show_contacts()
            elif choice == '6':
                break
            else:
                print(self.get_message("Invalid choice. Try again. / Неверный выбор. Попробуйте снова."))

contact = Contact()
contact.set_language()  
contact.menu()

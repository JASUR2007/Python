import sqlite3
from datetime import datetime
import re
from prettytable import PrettyTable
from colorama import Fore, Style
import bcrypt
import os

class Database:
    def __init__(self, db_name="license_plate_sales.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def initialize(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS LicensePlate (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                plate_number TEXT UNIQUE NOT NULL,
                price REAL NOT NULL,
                status TEXT NOT NULL,
                owner_id INTEGER DEFAULT NULL,
                created_at TEXT DEFAULT (DATETIME('now')),
                deleted_at TEXT,
                changed_at TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS User (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL CHECK(role IN ('admin', 'user')),
                created_at TEXT DEFAULT (DATETIME('now')),
                deleted_at TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                plate_id INTEGER,
                user_id INTEGER,
                date TEXT NOT NULL,
                deleted_at TEXT,
                FOREIGN KEY (plate_id) REFERENCES LicensePlate (id),
                FOREIGN KEY (user_id) REFERENCES User (id)
            )
        ''')

        conn.commit()
        conn.close()

class LicensePlate:
    def __init__(self, db):
        self.db = db

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")
    def validate_plate_number(self, plate_number, plate_type="personal"):
        if plate_type == "personal":
            pattern = r"^\d{2}[A-Z]{1}\d{3}[A-Z]{2}$"
            if not re.match(pattern, plate_number):
                print(Fore.RED + "Invalid format for personal plate. The number should consist of two digits, one letter, three digits, and two letters. Format: 00A505AA" + Style.RESET_ALL)
                return False
        elif plate_type == "organization":
            pattern = r"^\d{5}[A-Z]{3}$"
            
            if not re.match(pattern, plate_number):
                print(Fore.RED + "Invalid format for organizational plate. The number should consist of two digits, three digits, and three letters. Format: 00600AAA" + Style.RESET_ALL)
                return False
        
        if 'I' in plate_number:
            print(Fore.RED + "'I' is not allowed in the plate number." + Style.RESET_ALL)
            return False

        return True

    def add(self, owner_id=None):
        self.clear_screen()
        while True:
            plate_type = input(Fore.GREEN + "Enter plate type (personal/organization) or type 'back' to cancel: " + Style.RESET_ALL).lower()
            if plate_type == "back":
                return
            if plate_type not in ["personal", "organization"]:
                print(Fore.RED + "Invalid plate type. Please choose 'personal' or 'organization'." + Style.RESET_ALL)
                continue

            plate_number = input(Fore.GREEN + "Enter plate number or type 'back' to cancel: " + Style.RESET_ALL)
            if plate_number.lower() == "back":
                return
            if not self.validate_plate_number(plate_number, plate_type):
                continue
            break

        price = input(Fore.GREEN + "Enter price or type 'back' to cancel: " + Style.RESET_ALL)
        if price.lower() == "back":
            return
        try:
            price = float(price)
        except ValueError:
            print(Fore.RED + "Invalid price. Please enter a valid number." + Style.RESET_ALL)
            return

        status = "Available"

        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO LicensePlate (plate_number, price, status, owner_id) VALUES (?, ?, ?, ?)",
                        (plate_number, price, status, owner_id))
            conn.commit()
            print(Fore.GREEN + "License plate added successfully." + Style.RESET_ALL)
        except sqlite3.IntegrityError:
            print(Fore.RED + "Error: Plate number already exists." + Style.RESET_ALL)
        finally:
            conn.close()

    def view_all(self, include_unavailable=True):
        self.clear_screen()
        conn = self.db.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM LicensePlate"
        if not include_unavailable:
            query += " WHERE status = 'Available'"
        cursor.execute(query)
        plates = cursor.fetchall()

        table = PrettyTable()
        table.field_names = [Fore.YELLOW + Style.BRIGHT + "ID", "Plate", "Price", "Status", "Owner ID" + Style.RESET_ALL]
        for plate in plates:
            table.add_row([plate[0], plate[1], f"${plate[2]}", plate[3], plate[4]])

        print(Fore.GREEN + "\nLicense Plates:" + Style.RESET_ALL)
        print(table)
        conn.close()

    def update(self, user_id=None, is_admin=False):
        self.clear_screen()
        conn = self.db.connect()
        cursor = conn.cursor()

        if is_admin:
            cursor.execute("SELECT * FROM LicensePlate WHERE status = 'Available'")
        else:
            cursor.execute("SELECT * FROM LicensePlate WHERE owner_id = ?", (user_id,))

        plates = cursor.fetchall()

        if not plates:
            print(Fore.RED + "No license plates found." + Style.RESET_ALL)
            conn.close()
            return

        table = PrettyTable()
        table.field_names = [Fore.YELLOW + Style.BRIGHT + "ID", "Plate", "Price", "Status", "Owner ID" + Style.RESET_ALL]
        for plate in plates:
            table.add_row([plate[0], plate[1], f"${plate[2]}", plate[3], plate[4]])

        print(Fore.GREEN + "\nLicense Plates:" + Style.RESET_ALL)
        print(table)

        plate_id = input(Fore.GREEN + "Enter the ID of the license plate to edit (press Enter to return or type 'back' to cancel): " + Style.RESET_ALL)
        if plate_id.lower() == "back" or not plate_id:
            conn.close()
            return

        try:
            plate_id = int(plate_id)
        except ValueError:
            print(Fore.RED + "Invalid ID. Please enter a valid number." + Style.RESET_ALL)
            conn.close()
            return

        if not is_admin:
            cursor.execute("SELECT * FROM LicensePlate WHERE id = ? AND owner_id = ?", (plate_id, user_id))
        else:
            cursor.execute("SELECT * FROM LicensePlate WHERE id = ?", (plate_id,))

        plate = cursor.fetchone()
        if not plate:
            print(Fore.RED + "Error: Plate ID does not exist or is not accessible." + Style.RESET_ALL)
            conn.close()
            return

        new_plate_type = input(Fore.GREEN + "Enter new plate type (personal/organization) or press Enter to keep current: " + Style.RESET_ALL).lower()
        if new_plate_type and new_plate_type not in ["personal", "organization"]:
            print(Fore.RED + "Invalid plate type. Please choose 'personal' or 'organization'." + Style.RESET_ALL)
            conn.close()
            return
        new_plate_number = input(Fore.GREEN + "Enter new plate number (press Enter to keep current, or type 'back' to cancel): " + Style.RESET_ALL)
        if new_plate_number.lower() == "back":
            conn.close()
            return
        if new_plate_number and not self.validate_plate_number(new_plate_number, new_plate_type):
            conn.close()
            return

        new_price = input(Fore.GREEN + "Enter new price (press Enter to keep current, or type 'back' to cancel): " + Style.RESET_ALL)
        if new_price.lower() == "back":
            conn.close()
            return

        if not new_plate_number and not new_price and not new_plate_type:
            print(Fore.YELLOW + "No changes made." + Style.RESET_ALL)
            conn.close()
            return

        if new_plate_number:
            cursor.execute("UPDATE LicensePlate SET plate_number = ? WHERE id = ?",
                        (new_plate_number, plate_id))
        if new_price:
            cursor.execute("UPDATE LicensePlate SET price = ? WHERE id = ?",
                        (float(new_price), plate_id))
        if new_plate_type:
            print(Fore.YELLOW + "Note: Plate type is not stored in the database." + Style.RESET_ALL)

        conn.commit()
        print(Fore.GREEN + "License plate updated successfully." + Style.RESET_ALL)
        conn.close()
    def delete(self, user_id=None, is_admin=False):
        self.clear_screen()
        conn = self.db.connect()
        cursor = conn.cursor()

        if is_admin:
            cursor.execute("SELECT * FROM LicensePlate WHERE status = 'Available'")
        else:
            cursor.execute("SELECT * FROM LicensePlate WHERE owner_id = ?", (user_id,))

        plates = cursor.fetchall()

        if not plates:
            print(Fore.RED + "No license plates found." + Style.RESET_ALL)
            conn.close()
            return

        table = PrettyTable()
        table.field_names = [Fore.YELLOW + Style.BRIGHT + "ID", "Plate", "Price", "Status", "Owner ID" + Style.RESET_ALL]
        for plate in plates:
            table.add_row([plate[0], plate[1], f"${plate[2]}", plate[3], plate[4]])

        print(Fore.GREEN + "\nLicense Plates:" + Style.RESET_ALL)
        print(table)

        plate_id = input(Fore.GREEN + "Enter the ID of the license plate to delete (press Enter to return): " + Style.RESET_ALL)
        if not plate_id:
            conn.close()
            return

        plate_id = int(plate_id)
        if not is_admin:
            cursor.execute("SELECT * FROM LicensePlate WHERE id = ? AND owner_id = ?", (plate_id, user_id))
        else:
            cursor.execute("SELECT * FROM LicensePlate WHERE id = ?", (plate_id,))

        plate = cursor.fetchone()
        if not plate:
            print(Fore.RED + "Error: Plate ID does not exist or is not accessible." + Style.RESET_ALL)
            conn.close()
            return

        cursor.execute("DELETE FROM LicensePlate WHERE id = ?", (plate_id,))
        conn.commit()
        print(Fore.GREEN + "License plate deleted successfully." + Style.RESET_ALL)
        conn.close()

    def buy(self, user_id):
        self.clear_screen()
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM LicensePlate WHERE status = 'Available'")
        plates = cursor.fetchall()

        if not plates:
            print(Fore.RED + "No available license plates for purchase." + Style.RESET_ALL)
            conn.close()
            return

        table = PrettyTable()
        table.field_names = [Fore.YELLOW + Style.BRIGHT + "ID", "Plate", "Price", "Status" + Style.RESET_ALL]
        for plate in plates:
            table.add_row([plate[0], plate[1], f"${plate[2]}", plate[3]])

        print(Fore.GREEN + "\nAvailable License Plates:" + Style.RESET_ALL)
        print(table)

        plate_id = input(Fore.GREEN + "Enter the ID of the license plate to purchase: " + Style.RESET_ALL)
        if not plate_id:
            conn.close()
            return

        plate_id = int(plate_id)
        cursor.execute("SELECT * FROM LicensePlate WHERE id = ? AND status = 'Available'", (plate_id,))
        plate = cursor.fetchone()

        if not plate:
            print(Fore.RED + "Error: Plate ID does not exist or is not available." + Style.RESET_ALL)
            conn.close()
            return

        cursor.execute("UPDATE LicensePlate SET status = 'Unavailable', owner_id = ? WHERE id = ?", (user_id, plate_id))
        cursor.execute("INSERT INTO Sales (plate_id, user_id, date) VALUES (?, ?, ?)",
                    (plate_id, user_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        print(Fore.GREEN + "Purchase completed successfully." + Style.RESET_ALL)
        conn.close()

    def view_user_plates(self, user_id):
        self.clear_screen()
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM LicensePlate WHERE owner_id = ?", (user_id,))
        plates = cursor.fetchall()

        if not plates:
            print(Fore.YELLOW + "You don't own any license plates yet." + Style.RESET_ALL)
            conn.close()
            return

        table = PrettyTable()
        table.field_names = [Fore.YELLOW + Style.BRIGHT + "ID", "Plate", "Price", "Status" + Style.RESET_ALL]
        for plate in plates:
            table.add_row([plate[0], plate[1], f"${plate[2]}", plate[3]])

        print(Fore.GREEN + "\nYour License Plates:" + Style.RESET_ALL)
        print(table)
        conn.close()


class User:
    def __init__(self, db):
        self.db = db

    def authenticate(self):
        username = input(Fore.GREEN + "Enter name: " + Style.RESET_ALL)
        password = input(Fore.GREEN + "Enter password: " + Style.RESET_ALL)

        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user:
            hashed_password = user[2]  
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                print(Fore.GREEN + "Login successful." + Style.RESET_ALL)
                return user
            else:
                print(Fore.RED + "Invalid password. Please try again." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid username. Please try again." + Style.RESET_ALL)
        return None

    def register(self):
        username = input(Fore.GREEN + "Enter new user: " + Style.RESET_ALL)
        password = input(Fore.GREEN + "Enter new password: " + Style.RESET_ALL)
        role = input(Fore.GREEN + "Enter role (admin/user): " + Style.RESET_ALL).lower()

        if role not in ["admin", "user"]:
            print(Fore.RED + "Invalid role. Please choose 'admin' or 'user'." + Style.RESET_ALL)
            return

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO User (username, password, role) VALUES (?, ?, ?)",
                (username, hashed_password.decode('utf-8'), role),
            )
            conn.commit()
            print(Fore.GREEN + "User registered successfully." + Style.RESET_ALL)
        except sqlite3.IntegrityError:
            print(Fore.RED + "Error: Username already exists." + Style.RESET_ALL)
        finally:
            conn.close()

class LicensePlateSalesSystem:
    def __init__(self):
        self.db = Database()
        self.license_plate = LicensePlate(self.db)
        self.user = User(self.db)


    def admin_menu(self):
        while True:
            table = PrettyTable()
            table.field_names = [Fore.YELLOW + Style.BRIGHT + "Admin Menu" + Style.RESET_ALL]
            table.add_rows(
                [
                    [Fore.GREEN + "1. Add License Plate" + Style.RESET_ALL],
                    [Fore.GREEN + "2. Edit License Plate" + Style.RESET_ALL],
                    [Fore.GREEN + "3. Delete License Plate" + Style.RESET_ALL],
                    [Fore.GREEN + "4. All License Plates" + Style.RESET_ALL],
                    [Fore.GREEN + "5. All Users" + Style.RESET_ALL],
                    [Fore.GREEN + "6. All Purchases" + Style.RESET_ALL],
                    [Fore.GREEN + "7. User Purchases" + Style.RESET_ALL],
                    [Fore.GREEN + "8. Log Out" + Style.RESET_ALL]
                ]
            )
            print(table)

            choice = input(Fore.GREEN + "Enter your choice: " + Style.RESET_ALL)
            if choice == '1':
                self.license_plate.add()
            elif choice == '2':
                self.license_plate.update(is_admin=True)
            elif choice == '3':
                self.license_plate.delete(is_admin=True)
            elif choice == '4':
                self.license_plate.view_all()
            elif choice == '5':
                self.view_all_users()
            elif choice == '6':
                self.view_all_purchases()
            elif choice == '7':
                self.view_user_purchases()
            elif choice == '8':
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

    def user_menu(self, user_id):
        while True:
            table = PrettyTable()
            table.field_names = [Fore.YELLOW + Style.BRIGHT + "User Menu" + Style.RESET_ALL]
            table.add_rows(
                [
                    [Fore.GREEN + "1. Buy License Plate" + Style.RESET_ALL],
                    [Fore.GREEN + "2. All License Plates" + Style.RESET_ALL],
                    [Fore.GREEN + "3. Delete License Plate" + Style.RESET_ALL],
                    [Fore.GREEN + "4. Log Out" + Style.RESET_ALL]
                ]
            )
            print(table)

            choice = input(Fore.GREEN + "Enter your choice: " + Style.RESET_ALL)
            if choice == '1':
                self.license_plate.buy(user_id)
            elif choice == '2':
                self.license_plate.view_user_plates(user_id)
            elif choice == '3':
                self.license_plate.delete(user_id=user_id)
            elif choice == '4':
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

    def view_all_users(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, role FROM User")
        users = cursor.fetchall()

        table = PrettyTable()
        table.field_names = [Fore.YELLOW + Style.BRIGHT + "ID", "Username", "Role" + Style.RESET_ALL]
        for user in users:
            table.add_row([user[0], user[1], user[2]])

        print(Fore.GREEN + "\nAll Users:" + Style.RESET_ALL)
        print(table)
        conn.close()

    def view_all_purchases(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute('''SELECT Sales.id, LicensePlate.plate_number, User.username, Sales.date 
                          FROM Sales 
                          JOIN LicensePlate ON Sales.plate_id = LicensePlate.id 
                          JOIN User ON Sales.user_id = User.id''')
        purchases = cursor.fetchall()

        table = PrettyTable()
        table.field_names = [Fore.YELLOW + Style.BRIGHT + "Purchase ID", "Plate Number", "Buyer",
                             "Date" + Style.RESET_ALL]
        for purchase in purchases:
            table.add_row([purchase[0], purchase[1], purchase[2], purchase[3]])

        print(Fore.GREEN + "\nAll Purchases:" + Style.RESET_ALL)
        print(table)
        conn.close()

    def view_user_purchases(self):
        username = input(Fore.GREEN + "Enter the username to view purchases: " + Style.RESET_ALL)
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute('''SELECT Sales.id, LicensePlate.plate_number, Sales.date 
                          FROM Sales 
                          JOIN LicensePlate ON Sales.plate_id = LicensePlate.id 
                          JOIN User ON Sales.user_id = User.id 
                          WHERE User.username = ?''', (username,))
        purchases = cursor.fetchall()

        if purchases:
            table = PrettyTable()
            table.field_names = [Fore.YELLOW + Style.BRIGHT + "Purchase ID", "Plate Number",
                                 "Date" + Style.RESET_ALL]
            for purchase in purchases:
                table.add_row([purchase[0], purchase[1], purchase[2]])

            print(Fore.GREEN + f"\nPurchases by {username}:" + Style.RESET_ALL)
            print(table)
        else:
            print(Fore.RED + f"No purchases found for user: {username}" + Style.RESET_ALL)
        conn.close()

    def main_menu(self):
        self.db.initialize()
        while True:
            print(Fore.GREEN + "\nWelcome!" + Style.RESET_ALL)
            table = PrettyTable()
            table.field_names = [Fore.YELLOW + Style.BRIGHT + "Menu" + Style.RESET_ALL]
            table.add_rows(
                [
                    [Fore.GREEN + "1. Sign in" + Style.RESET_ALL],
                    [Fore.GREEN + "2. Sign up" + Style.RESET_ALL],
                    [Fore.GREEN + "3. Exit" + Style.RESET_ALL],
                ]
            )
            print(table)

            choice = input(Fore.GREEN + "Enter your choice: " + Style.RESET_ALL)
            if choice == '1':
                user = self.user.authenticate()
                if user:
                    if user[3] == "admin":
                        self.admin_menu()
                    elif user[3] == "user":
                        self.user_menu(user[0])
            elif choice == '2':
                self.user.register()
            elif choice == '3':
                print(Fore.GREEN + "Finished" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "Incorrect choice. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    system = LicensePlateSalesSystem()
    system.main_menu()


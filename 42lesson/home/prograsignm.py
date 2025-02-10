import psycopg2
from datetime import datetime
import re
from prettytable import PrettyTable
from colorama import Fore, Style

class Database:
    def __init__(self, host="localhost", dbname="license_plate_sales", user="your_user", password="your_password"):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password

    def connect(self):
        return psycopg2.connect(
            host=self.host,
            dbname=self.dbname,
            user=self.user,
            password=self.password
        )

    def initialize(self):
        conn = self.connect()
        cursor = conn.cursor()

        # Create License Plate table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS LicensePlate (
                id SERIAL PRIMARY KEY,
                plate_number TEXT UNIQUE NOT NULL,
                price REAL NOT NULL,
                status TEXT NOT NULL,
                owner_id INTEGER DEFAULT NULL
            )
        ''')

        # Create User table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS "User" (
                id SERIAL PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL CHECK(role IN ('admin', 'user'))
            )
        ''')

        # Create Sales table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Sales (
                id SERIAL PRIMARY KEY,
                plate_id INTEGER,
                user_id INTEGER,
                date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (plate_id) REFERENCES LicensePlate (id),
                FOREIGN KEY (user_id) REFERENCES "User" (id)
            )
        ''')

        conn.commit()
        conn.close()


# ------------------------- License Plate Class -------------------------
class LicensePlate:
    def __init__(self, db):
        self.db = db

    def validate_plate_number(self, plate_number):
        """Validate plate number format."""
        pattern = r"^\d{2}[A-Z]{1}\d{3}[A-Z]{2}$"
        if not re.match(pattern, plate_number):
            print(Fore.RED + "Invalid format. Try again. Format: 00A123NN" + Style.RESET_ALL)
            return False
        return True

    def add(self, owner_id=None):
        """Add a new license plate to the system."""
        while True:
            plate_number = input(Fore.GREEN + "Enter plate number: " + Style.RESET_ALL)
            if not self.validate_plate_number(plate_number):
                continue
            break

        price = float(input(Fore.GREEN + "Enter price: " + Style.RESET_ALL))
        status = "Available"

        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO LicensePlate (plate_number, price, status, owner_id) VALUES (%s, %s, %s, %s)",
                           (plate_number, price, status, owner_id))
            conn.commit()
            print(Fore.GREEN + "License plate added successfully." + Style.RESET_ALL)
        except psycopg2.IntegrityError:
            print(Fore.RED + "Error: Plate number already exists." + Style.RESET_ALL)
        finally:
            conn.close()

    def view_all(self, include_unavailable=True):
        """View all available or all license plates."""
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
        """Update license plate details."""
        conn = self.db.connect()
        cursor = conn.cursor()

        if is_admin:
            cursor.execute("SELECT * FROM LicensePlate WHERE status = 'Available'")
        else:
            cursor.execute("SELECT * FROM LicensePlate WHERE owner_id = %s", (user_id,))

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

        plate_id = input(Fore.GREEN + "Enter the ID of the license plate to edit (press Enter to return): " + Style.RESET_ALL)
        if not plate_id:
            conn.close()
            return

        plate_id = int(plate_id)
        if not is_admin:
            cursor.execute("SELECT * FROM LicensePlate WHERE id = %s AND owner_id = %s", (plate_id, user_id))
        else:
            cursor.execute("SELECT * FROM LicensePlate WHERE id = %s", (plate_id,))

        plate = cursor.fetchone()
        if not plate:
            print(Fore.RED + "Error: Plate ID does not exist or is not accessible." + Style.RESET_ALL)
            conn.close()
            return

        # Update logic here (e.g., updating price, status, owner_id)
        new_price = input(Fore.GREEN + "Enter new price (leave empty to keep the same): " + Style.RESET_ALL)
        if new_price:
            cursor.execute("UPDATE LicensePlate SET price = %s WHERE id = %s", (new_price, plate_id))

        new_status = input(Fore.GREEN + "Enter new status (leave empty to keep the same): " + Style.RESET_ALL)
        if new_status:
            cursor.execute("UPDATE LicensePlate SET status = %s WHERE id = %s", (new_status, plate_id))

        new_owner_id = input(Fore.GREEN + "Enter new owner ID (leave empty to keep the same): " + Style.RESET_ALL)
        if new_owner_id:
            cursor.execute("UPDATE LicensePlate SET owner_id = %s WHERE id = %s", (new_owner_id, plate_id))

        conn.commit()
        print(Fore.GREEN + "License plate updated successfully." + Style.RESET_ALL)
        conn.close()

    def sell(self, plate_id, user_id):
        """Sell a license plate."""
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM LicensePlate WHERE id = %s AND status = 'Available'", (plate_id,))
        plate = cursor.fetchone()

        if not plate:
            print(Fore.RED + "This plate is not available for sale." + Style.RESET_ALL)
            conn.close()
            return

        cursor.execute("UPDATE LicensePlate SET status = 'Sold', owner_id = %s WHERE id = %s", (user_id, plate_id))
        cursor.execute("INSERT INTO Sales (plate_id, user_id) VALUES (%s, %s)", (plate_id, user_id))

        conn.commit()
        print(Fore.GREEN + "License plate sold successfully." + Style.RESET_ALL)
        conn.close()

# ------------------------- User Class -------------------------
class User:
    def __init__(self, db):
        self.db = db

    def login(self):
        """Login logic."""
        username = input(Fore.GREEN + "Enter username: " + Style.RESET_ALL)
        password = input(Fore.GREEN + "Enter password: " + Style.RESET_ALL)

        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM \"User\" WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        conn.close()
        if user:
            print(Fore.GREEN + f"Welcome, {username}!" + Style.RESET_ALL)
            return user
        else:
            print(Fore.RED + "Invalid username or password." + Style.RESET_ALL)
            return None

# ------------------------- Main Execution -------------------------
if __name__ == "__main__":
    db = Database()
    db.initialize()

    print(Fore.GREEN + "\nWelcome to the License Plate System!" + Style.RESET_ALL)
    
    user = User(db)
    logged_in_user = user.login()
    if logged_in_user:
        user_id = logged_in_user[0]
        is_admin = logged_in_user[3] == 'admin'

        lp = LicensePlate(db)

        while True:
            print("\n1. Add Plate\n2. View All Plates\n3. Update Plate\n4. Sell Plate\n5. Exit")
            choice = input("Choose an action: ")

            if choice == '1':
                lp.add(owner_id=user_id if not is_admin else None)
            elif choice == '2':
                lp.view_all(include_unavailable=True)
            elif choice == '3':
                lp.update(user_id=user_id, is_admin=is_admin)
            elif choice == '4':
                plate_id = int(input(Fore.GREEN + "Enter Plate ID to sell: " + Style.RESET_ALL))
                lp.sell(plate_id, user_id)
            elif choice == '5':
                print(Fore.GREEN + "Exiting..." + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "Invalid option. Please try again." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Login failed. Exiting..." + Style.RESET_ALL)

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Patient(Person):
    def __init__(self, name, age, gender, ailment):
        super().__init__(name, age, gender)
        self.ailment = ailment
        self.appointment_id = ''

class Doctor(Person):
    def __init__(self, name, age, gender, specialty):
        super().__init__(name, age, gender)
        self.specialty = specialty
        self.schedule = [] 

class Staff:
    def __init__(self, username, password):
        self.username = username
        self.password = password

patients = []
doctors = []
staff_members = [Staff("admin", "admin")]

def register_patient():
    name = input("Enter your name: ")
    age = int(input("Enter age: "))
    gender = input("Enter agegender: ")
    ailment = input("Write your ailment: ")
    new_patient = Patient(name, age, gender, ailment)
    patients.append(new_patient)
    print("Patient registered successfully!\n")

def view_doctors():
    if doctors == []:
        return "Doctors are Empty!"

    print("List of doctors:")
    index = 1
    for doctor in doctors:
        print(f"{index}. Doctor: {doctor.name}.\n Specialty: {doctor.specialty}")
        index += 1
    return
def book_appointment():
    pass;

def view_schedule():
    pass;

def manage_clinic():
    print("Admin Management Panel")
    options = {
        1: ("Add Doctor", add_doctor),
        2: ("Remove Doctor", remove_doctor),
        3: ("View All Records", view_records)
    }

    # Prepare the options list for display
    options_list = []
    for key, value in options.items():
        option_string = f"{key}. {value[0]}"
        options_list.append(option_string)

    options_string = "\n".join(options_list)
    print(options_string)

    choice_input = input("Choose an option: ")

    if choice_input.isdigit():  
        choice = int(choice_input)
        if choice in options: 
            options[choice][1]() 
        else:
            print("Incorrect.")
    else:
        print("Incorrect.")
def add_doctor():
    name = input("Enter d-name: ")
    age = int(input("Enter d-age: "))
    gender = input("Enter d-gender: ")
    specialty = input("Enter d-specialty: ")
    new_doctor = Doctor(name, age, gender, specialty)
    # print(new_doctor)
    doctors.append(new_doctor)
    # print(doctors)
    print("Doctor added")

def remove_doctor():
    view_doctors()
    doctor_index = int(input("Select the doctor to remove by number: ")) - 1
    if 0 <= doctor_index < len(doctors):
        removed_doctor = doctors.pop(doctor_index)
        print(f"Dr. {removed_doctor.name} removed successfully!\n")
    else:
        print("Invalid selection.\n")

def view_records():
    records = [
        f"Patient: Name: {patient.name}, Age: {patient.age}, Gender: {patient.gender}, Ailment: {patient.ailment}" 
        for patient in patients
    ] + [
        f"Doctor: {doctor.name} - {doctor.specialty}, Appointments: {len(doctor.schedule)}"
        for doctor in doctors
    ]
    print("\n".join(records) if records else "No records available.")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    staff = ''
    for arr in staff_members:
        if arr.username == username and arr.password == password:
            staff = arr
            break
    if staff != '':
        print("Login successful!\n")
        manage_clinic()
    else:
        print("Invalid credentials.\n")

def menu():
    options = {
        1: ("Register as a Patient", register_patient),2: ("View Doctors", view_doctors),3: ("Book an Appointment", book_appointment),
        4: ("View Doctor Schedule", view_schedule),5: ("Admin Login", login),6: ("Exit", exit)
    }
    
    while True:
        print("Clinic Management System")
        options_list = []
        for key, value in options.items():
            options_list.append(f"{key}. {value[0]}")
            print(key, value)
        options_string = "\n".join(options_list)
        print(options_string)
        try:
            choice = int(input("Choose an option: "))
            if choice in options:
                options[choice][1]()
                # print(options)
            else:
                print("Incorrect number. Write from 1 to 6.")
        except ValueError:
            print("Incorrect type. Write only numbers!")
menu()

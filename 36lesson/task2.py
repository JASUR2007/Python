# Task 2: Vehicle Rental System
# Create a Vehicle base class with:

# Attributes:
# make (string)
# model (string)
# rental_rate (float)
# Methods:
# display_vehicle_info(): Prints the vehicle details.
# Create subclasses for Car and Motorcycle:

# Car:
# Additional attribute: num_seats (int)
# Override display_vehicle_info() to include the number of seats.
# Motorcycle:
# Additional attribute: engine_capacity (cc, int)
# Override display_vehicle_info() to include engine capacity.
# Add a RentalService class with:

# Attributes:
# vehicles (list of Vehicle objects)
# Methods:
# add_vehicle(vehicle): Adds a vehicle to the list.
# get_all_vehicle_info(): Prints details of all vehicles.
# Objective: Practice inheritance, composition, and method overriding.


class Vehicle:
    def __init__(self, make:str, model:str, rental_rate:float):
        self.make=make
        self.model=model
        self.rental_rate=rental_rate
    def display_vehicle_info(self):
        return f'the vehicle {self.model} was made by {self.make}, rental rate is {self.rental_rate}'

class Car(Vehicle):
    def __init__(self, make:str, model:str, rental_rate:float, num_seats:int):
        super().__init__(make, model, rental_rate)
        self.num_seats=num_seats
    def display_vehicle_info(self):
        return f'{super().display_vehicle_info()}, seats are: {self.num_seats}'
    
    
class Motorcycle(Vehicle):
    def __init__(self, make:str, model:str, rental_rate:float, engine_capacity:int):
        super().__init__(make, model, rental_rate)
        self.engine_capacity=engine_capacity
    def display_vehicle_info(self):
        return f'{super().display_vehicle_info()}, engine capacity is: {self.engine_capacity}'

class RentalService:
    def __init__(self, vehicles: list):
        self.vehicles = vehicles 

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f'Vehicle "{vehicle.make} {vehicle.model}" was added to the list.')

    def get_all_vehicle_info(self):
        for vehicle in self.vehicles:
            print(vehicle.display_vehicle_info())

malibu=Car("UZAUTOMOTORS", "Malibu", 7.8,5)

bmw=Motorcycle('BMW', "motorcyle01s", 9, 150)

rental_service = RentalService([])
rental_service.add_vehicle(malibu)
rental_service.add_vehicle(bmw)
print("\nAll Vehicles:")
rental_service.get_all_vehicle_info()
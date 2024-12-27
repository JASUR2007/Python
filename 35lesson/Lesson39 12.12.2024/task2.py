# 2. Task: VehiclesCreate a parent class Vehicle with attributes like make and model, and a method describe().
# Create child classes Car and Motorcycle, each adding unique methods like play_music() or pop_wheelie().

class VehiclesCreate:
    def __init__(self, make, model):
        self.make=make
        self.model=model
    def describe(self):
        return f'make is {self.make}\nmodedl is {self.model}'
class Car(VehiclesCreate):
    def play_music(self):
        return 'True, plays music'
class Motorcycle(VehiclesCreate):
    def pop_wheelie(self):
        return f'Yes gass motorcycle'

car1=Car('Uzauto', "Jentra")
print(car1.describe())
print(car1.play_music())

motorcycle1=Motorcycle("BMW",4050)
print(car1.describe())
print(motorcycle1.pop_wheelie())
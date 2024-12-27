# 10. Task: Zoo SimulationCreate a parent class Animal with attributes like name and species.
# Create child classes Carnivore and Herbivore.
# Carnivore should add a method hunt().
# Herbivore should add a method graze().
# Create subclasses of Carnivore (like Lion) and Herbivore (like Deer) with their unique behaviors.

class Animal:
    def __init__(self, name, species):
        self.name=name
        self.species=species

class Carnivore(Animal):
    def hunt(self):
        return f'the animal {self.name} is hunting, it is from {self.species}\n'

class Herbivore(Animal):
    def graze(self):
        return f'{self.name} is grazing, it is from {self.species}\n'

class Lion(Carnivore):
    def running(self):
        return f'{super().hunt()}. {self.name} is also running'

class Deer(Herbivore):
    def swimming(self):
        return f'{super().graze()}. {self.name} is also swimming'


tiger=Carnivore('Tiger', 'Carnivore')
print(tiger.hunt())

cow=Herbivore('Cow', "herbiwore")
print(cow.graze())

lion=Lion('Lion', "Herbivore")
print(lion.running())

deer=Deer('Deer', "Herbivore")
print(deer.swimming())
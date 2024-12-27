# Task 4: Animal Kingdom Simulation
# Create an Animal base class with:

# Attributes:
# name (string)
# age (int)
# Methods:
# make_sound(): Prints a generic animal sound.
# Create subclasses for Dog and Cat:

# Dog:
# Additional attribute: breed (string)
# Override make_sound() to print "Woof!"
# Cat:
# Additional attribute: color (string)
# Override make_sound() to print "Meow!"
# Add a Zoo class with:

# Attributes:
# animals (list of Animal objects)
# Methods:
# add_animal(animal): Adds an animal to the zoo.
# make_all_sounds(): Calls make_sound() for every animal in the zoo.
# Objective: Practice method overriding and polymorphism.

class Animal:
    def __init__(self,name:str, age=int):
        self.name=name
        self.age=age
    def make_sound(self):
        return f'name is {self.name}, age is {self.age}. {self.name} makes sound'

class Dog(Animal):
    def __init__(self,name:str, age:int, breed:str):
        super().__init__(name, age)
        self.breed=breed
    def make_sound(self):
        return f'{super().make_sound()}, Woof'
    def all_info(self):
        return f'name is {self.name}, age is {self.age}, breed is {self.breed}, {self.make_sound()}'

class Cat(Animal):
    def __init__(self, name:str, age:int, color:str):
        super().__init__(name, age)
        self.color=color
    def make_sound(self):
        return f'{super().make_sound()}, Meow'
    

class Zoo:
    def __init__(self, animals:list):
        self.animals=animals
    def add_animal(self, animal):
        self.animals.append(animal)
        return f'a new animal {animal.name} has been added'
    def make_all_sounds(self):
        for animal in self.animals:
            print(animal.make_sound())

dog1=Dog('Wolfer', 5, 'big dog')
dog2=Dog('Dalsy', 6, 'american')
cat1=Cat('Aniss', 4, "black-grey")
cat2=Cat('Polis', 2, "black")

zoolist=Zoo([])
print(zoolist.add_animal(dog1))
print(zoolist.add_animal(cat1))
print(zoolist.add_animal(dog2))
print(zoolist.add_animal(cat2))
print('\n')
zoolist.make_all_sounds()

class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


# polymorphism

animals = [Dog, Cat, Animal]

for i in animals:
    print(i().speak())

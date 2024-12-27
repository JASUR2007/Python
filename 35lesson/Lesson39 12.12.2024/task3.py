# 3. Task: Animals and SoundsCreate a parent class Animal with a method sound() that prints a generic sound.
# Create child classes Dog, Cat, and Cow that override the sound() method to print specific sounds (e.g., "Woof", "Meow", "Moo").

class SoundsCreate:
    def sound(self):
        return 'it makes sound'

class Dog(SoundsCreate):
    def sound(self):
        super().sound()
        return 'it is dog-woof'

class Cat(SoundsCreate):
    def sound(self):
        super().sound()
        return 'it is cat-meow'

class Cow(SoundsCreate):
    def sound(self):
        super().sound()
        print( 'it is cow-moo')

dog=Dog()
print(dog.sound())

cat=Cat()
print(cat.sound())

cow=Cow()
cow.sound()

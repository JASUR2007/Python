# 11. Task: Smart DevicesCreate a parent class Device with attributes like brand and model, and a method turn_on().
# Create child classes Phone, Tablet, and Laptop with unique methods like make_call() for Phone or draw() for Tablet.

class Device:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def turn_on(self):
        return f'tuned on'

class Phone(Device):
    def make_call(self):
        return f'{self.brand+' '+self.model} is making call...'

class Tablet(Device):
    def draw(self):
        return f'{self.brand+' '+self.model} is drawing...'

class Laptop(Device):
    def opening(self):
        return f'{self.brand+' '+self.model} is opening 180*...'

iphone=Phone('Apple', '16 pro max')
print(iphone.make_call())

samsung=Tablet('Samsung', 'Tablet A70')
print(samsung.draw())

lenovo=Laptop('Lenovo', "S450")
print(lenovo.opening())
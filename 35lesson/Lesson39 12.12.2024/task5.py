# 5. Task: Online StoreCreate a parent class Product with attributes like name and price.
# Create child classes Clothing and Electronics.
# Clothing should have a size attribute.
# Electronics should have a warranty attribute.
# Add a method to display the details of each product.

class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price
    def show_info(self):
        return f'the name is {self.name}, price is ${self.price}'

class Clothing(Product):
    def __init__(self, name,price, size):
        super().__init__(name,price)
        self.size=size
    def show_info(self):
        return f'{super().show_info()},size is {self.size}'

class Electronics(Product):
    def __init__(self, name,price, warranty):
        super().__init__(name,price)
        self.warranty=warranty
    def show_info(self):
        return f'{super().show_info()}, is {self.warranty} months'

tshirt=Clothing('Nike', 45, 44)
print(tshirt.show_info())

watch=Electronics('Apple watch',220, 24)
print(watch.show_info())

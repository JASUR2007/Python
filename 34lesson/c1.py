class RectangeArea:
    def __init__(self, lenght, width):
        self.length = lenght
        self.width = width
    def area(self):
        return f"Area: {self.length * self.width}"
    
rec = RectangeArea(4,9)
print(rec.area())
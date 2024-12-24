class SafeBox:
    def __init__(self, pin_code):
        self.__pin_code = pin_code
    def check_pin(self, pincode):
        return self.__pin_code == pincode
    
pin = SafeBox('0000')
print(pin.check_pin('000'))